# RP2040 & WizFi360 Examples with CircuitPython

- [**Overview**](#overview)
- [**Getting Started**](#getting_started)
- [**Directory Structure**](#directory_structure)



<a name="overview"></a>
## Overview

The RP2040 & WizFi360 examples with CircuitPython use **WizFi360-EVB-Pico** - Wi-Fi I/O module built on [**RP2040**][link-rp2040] and WIZnet's [**WizFi360**][link-wizfi360] Wi-Fi module.

- [**WizFi360-EVB-Pico**][link-wizfi360-evb-pico]

![][link-wizfi360-evb-pico_main]



<a name="getting_started"></a>
## Getting Started

Please refer to [**Getting Started**][link-getting_started] for how to configure development environment or examples usage.



<a name="directory_structure"></a>
## Directory Structure

```
WizFi360-EVB-Pico-CircuitPython
┣ examples
┃   ┣ blink
┃   ┣ http
┃   ┃   ┗ request
┃   ┣ loopback
┃   ┣ mqtt
┃   ┃   ┣ publish
┃   ┃   ┣ publish_subscribe
┃   ┃   ┗ subscribe
┃   ┣ ping
┃   ┣ sntp
┃   ┣ tcp
┃   ┃   ┗ client
┃   ┗ wi-fi
┣ libraries
┃   ┣ adafruit_requests
┃   ┗ adafruit_wizfiatcontrol
┗ static
    ┣ documents
    ┗ images
```



<!--
Link
-->

[link-rp2040]: https://www.raspberrypi.org/products/rp2040/
[link-wizfi360]: https://docs.wiznet.io/Product/Wi-Fi-Module/WizFi360/wizfi360
[link-wizfi360-evb-pico]: https://docs.wiznet.io/Product/Open-Source-Hardware/wizfi360-evb-pico
[link-wizfi360-evb-pico_main]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/images/wizfi360-evb-pico_main.png
[link-getting_started]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/documents/getting_started.md
