# ina219_ros

This is a ROS 2 package for the TI INA219 current/power monitoring chip with a 10mΩ shunt resistor.

## Supported ROS 2 distributions

[![humble][humble-badge]][humble]
[![ubuntu22][ubuntu22-badge]][ubuntu22]

## Requirements
- Ubuntu OS PC
  - Ubuntu 22.04 Humble

## Usage

```sh: Terminal
sudo apt install python3-smbus
```

```sh: Terminal
sudo i2cdetect -y -r 1

```
I2C Address: Four options 0x40, 0x41, 0x44, 0x45, default is `0x45`.


```sh: Terminal
. install/setup.bash
ros2 run ina219_ros power_node
```

## Reference

[Gravity: I2C Digital Wattmeter](https://www.dfrobot.com/product-1827.html)


## License
This repository is licensed under the MIT license, see LICENSE.

[humble-badge]: https://img.shields.io/badge/-HUMBLE-orange?style=flat-square&logo=ros
[humble]: https://docs.ros.org/en/humble/index.html

[ubuntu22-badge]: https://img.shields.io/badge/-UBUNTU%2022%2E04-blue?style=flat-square&logo=ubuntu&logoColor=white
[ubuntu22]: https://releases.ubuntu.com/jammy/
