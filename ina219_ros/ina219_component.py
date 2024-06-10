# MIT License

# Copyright (c) 2024 Takumi Asada

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# https://www.dfrobot.com/product-1827.html
from rclpy.node import Node
from std_msgs.msg import Float32

from .DFRobot_INA219 import INA219

import time

class PowerComponent(Node):
    def __init__(self):
        super().__init__('ina219_node')
        self.pub_voltage = self.create_publisher(Float32, "/ina219/voltage", 10)
        self.pub_current = self.create_publisher(Float32, "/ina219/current", 10)
        self.pub_power = self.create_publisher(Float32, "/ina219/power", 10)

        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.ina219_reading_mA = 1000
        self.ext_meter_reading_mA = 1000
        self.ina = INA219(1, INA219.INA219_I2C_ADDRESS4)
        while not self.ina.begin():
                time.sleep(2)
        self.ina.linear_cal(self.ina219_reading_mA, self.ext_meter_reading_mA)
        #begin return True if succeed, otherwise return False
        # while not self.ina.begin():

    def timer_callback(self):
        msg_voltage = Float32()
        msg_current = Float32()
        msg_power = Float32()
        msg_voltage.data = float(round(self.ina.get_bus_voltage_V(), 2))
        msg_current.data = float(round(self.ina.get_current_mA(), 2))
        msg_power.data = float(round(self.ina.get_power_mW(), 3))
        print ("Shunt Voltage : %.2f mV" % self.ina.get_shunt_voltage_mV())
        print ("Bus Voltage   : %.3f V" % self.ina.get_bus_voltage_V())
        print ("Current       : %.f mA" % self.ina.get_current_mA())
        print ("Power         : %.f mW" % self.ina.get_power_mW())
        print (" ")
        self.pub_voltage.publish(msg_voltage)
        self.pub_current.publish(msg_current)
        self.pub_power.publish(msg_power)
