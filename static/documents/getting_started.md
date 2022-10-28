# Getting Started

These sections will guide you through a series of steps from configuring development environment to running RP2040 & WizFi360 examples with CircuitPython.

- [**Hardware Requirements**](#hardware_requirements)
- [**Development Environment Configuration**](#development_environment_configuration)
    - [**Installing CircuitPython**](#installing_circuitpython)
    - [**Setup Libraries**](#setup_libraries)
- [**Example Structure**](#example_structure)
- [**Example Testing**](#example_testing)



<a name="hardware_requirements"></a>
## Hardware Requirements

- [**WizFi360-EVB-Pico**][link-wizfi360-evb-pico]
- **Desktop** or **Laptop**
- **USB Type-B Micro 5 Pin Cable**



<a name="development_environment_configuration"></a>
## Development Environment Configuration

To test the examples, the development environment must be configured to use Raspberry Pi Pico or WizFi360-EVB-Pico.

The examples were tested by configuring the development environment for **Windows**. Please refer to the below and configure accordingly.



<a name="installing_circuitpython"></a>
### Installing CircuitPython

Install CircuitPython on Raspberry Pi Pico by referring to the link below.

- [**Installing CircuitPython**][link-installing_circuitPython]

Prototyping is easier than ever, with no software download required. Simply copy and edit the files to the **CIRCUITPY** drive, and repeat it.

![][link-circuitpy_1]

![][link-circuitpy_2]

Edit and save the code in **code.py**, your code will run on the WizFi360-EVB-Pico.

Let's check if CircuitPython is properly installed in your WizFi360-EVB-Pico with a simple blink example by referring to the link below.

- [**Blinky and a Button**][link-blinky_and_a_button]



<a name="setup_libraries"></a>
### Setup Libraries

To use Wi-Fi and additional functions of WizFi360-EVB-Pico, copy and paste the libraries included in the '[**WizFi360-EVB-Pico-CircuitPython/libraries**][link-libraries]' directory into the '**CIRCUITPY/lib**' directory.

<p align="center"><img src="https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/images/getting_started/copy_and_paste_library.png"></p>



<a name="example_structure"></a>
## Example Structure

Examples are available at '[**WizFi360-EVB-Pico-CircuitPython/examples**][link-examples]' directory. As of now, following examples are provided.

- [**Blink**][link-blink]
- [**HTTP**][link-http]
    - [**Request**][link-http_request]
- [**Loopback**][link-loopback]
- [**MQTT**][link-mqtt]
    - [**Publish**][link-mqtt_publish]
    - [**Publish & Subscribe**][link-mqtt_publish_subscribe]
    - [**Subscribe**][link-mqtt_subscribe]
- [**Ping**][link-ping]
- [**SNTP**][link-sntp]
- [**TCP**][link-tcp]
	- [**Client**][link-tcp_client]
- [**Wi-Fi**][link-wi-fi]



<a name="example_testing"></a>
## Example Testing

Please refer to 'README.md' in each example directory to detail guide for testing examples.



<!--
Link
-->

[link-wizfi360-evb-pico]: https://docs.wiznet.io/Product/Open-Source-Hardware/wizfi360-evb-pico
[link-installing_circuitpython]: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython
[link-circuitpy_1]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/images/getting_started/circuitpy_1.png
[link-circuitpy_2]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/images/getting_started/circuitpy_2.png
[link-blinky_and_a_button]: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/blinky-and-a-button
[link-libraries]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/libraries
[link-copy_and_paste_library]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/blob/main/static/images/getting_started/copy_and_paste_library.png
[link-examples]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples
[link-blink]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/blink
[link-http]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/http
[link-http_request]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/http/request
[link-loopback]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/loopback
[link-mqtt]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/mqtt
[link-mqtt_publish]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/mqtt/publish
[link-mqtt_publish_subscribe]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/mqtt/publish_subscribe
[link-mqtt_subscribe]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/mqtt/subscribe
[link-ping]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/ping
[link-sntp]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/sntp
[link-tcp]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/tcp
[link-tcp_client]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/tcp/client
[link-wi-fi]: https://github.com/Wiznet/WizFi360-EVB-Pico-CircuitPython/tree/main/examples/wi-fi
