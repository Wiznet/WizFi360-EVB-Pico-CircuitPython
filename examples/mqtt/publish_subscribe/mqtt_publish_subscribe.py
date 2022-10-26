#
# Copyright(c) 2022 WIZnet Co., Ltd
#
# SPDX-License-Identifier: BSD-3-Clause
#

import time
import board
import busio
from digitalio import DigitalInOut
from digitalio import Direction
from adafruit_wizfiatcontrol import adafruit_wizfiatcontrol


# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("Wi-Fi secrets are kept in secrets.py, please add them there!")
    raise

# Debug Level
# Change the Debug Flag if you have issues with AT commands
debugflag = False

# WizFi360 configuration
RX = board.GP5
TX = board.GP4
resetpin = DigitalInOut(board.GP20)
rtspin = False
uart = busio.UART(TX, RX, baudrate=11520,
                  receiver_buffer_size=2048)

print("WizFi360 AT commands")
wizfi = adafruit_wizfiatcontrol.WizFi_ATcontrol(
    uart, 115200, reset_pin=resetpin, rts_pin=rtspin, debug=debugflag
)
print("AT software version:", wizfi.get_version())

# Target settings
BROKER_IP = "192.168.11.3"
BROKER_PORT = 1883
print("Target info: ", BROKER_IP, ":", BROKER_PORT, sep="")

# Client settings
USERNAME = "wiznet"
PASSWORD = "0123456789"
CLIENT_ID = "rpi-pico"
print("Username: ", USERNAME, "\n", "Password: ", PASSWORD, "\n", "Client ID: ", CLIENT_ID, sep="")

# Keep Alive settings
KEEP_ALIVE = 60
print("Keep Alive:", KEEP_ALIVE)

# QoS settings
QOS = 0
print("QoS:", QOS)

# Topic settings
PUBLISH_TOPIC = "publish_topic"
SUBSCRIBE_TOPIC = "subscribe_topic"
print("Publish topic: ", PUBLISH_TOPIC, "\n", "Subscribe topic: ", SUBSCRIBE_TOPIC, sep="")

# Authentication settings
AUTH_ENABLE = 0
print("Authentication: ", "Enable" if AUTH_ENABLE else "Disable", sep="")

# Publish interval settings
PUBLISH_PERIOD = 60  # in seconds

print("Resetting WizFi360 module")
wizfi.hard_reset()

wizfi.set_mqtt_config(USERNAME, PASSWORD, CLIENT_ID, KEEP_ALIVE)
wizfi.set_mqtt_qos(QOS)
wizfi.set_mqtt_topic(PUBLISH_TOPIC, SUBSCRIBE_TOPIC)

is_broker_connected = False
start = 0
elapsed = 0
while True:
    try:
        print("Checking connection...")
        while not wizfi.is_connected:
            print("Connecting to AP...")
            wizfi.connect(secrets)
        while not is_broker_connected:
            print("Connecting to broker...")
            is_broker_connected = wizfi.mqtt_connect(
                AUTH_ENABLE, BROKER_IP, BROKER_PORT)
            if is_broker_connected:
                print("Connected to ", BROKER_IP, ":", BROKER_PORT, sep="")
        elapsed = time.monotonic()
        if(elapsed > start + PUBLISH_PERIOD):
            data = "Hello, World!"
            is_socket_sent = wizfi.mqtt_publish(data)
            if is_socket_sent:
                print("Send OK")
            start = time.monotonic()
        data = wizfi.mqtt_subscribe()
        print(data, end="")
    except (ValueError, RuntimeError, adafruit_wizfiatcontrol.OKError) as e:
        print("Failed to get data, retrying\n", e)
        print("Resetting WizFi360 module")
        wizfi.hard_reset()
        continue
