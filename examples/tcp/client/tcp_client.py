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
import adafruit_wizfiatcontrol.adafruit_wizfiatcontrol_socket as socket
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

# How long between queries
TIME_BETWEEN_QUERY = 60  # in seconds

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
TARGET_IP = "192.168.11.3"
TARGET_PORT = 5000
print("Target info: ", TARGET_IP, ":", TARGET_PORT, sep="")

print("Resetting WizFi360 module")
wizfi.hard_reset()

is_socket_connected = False
while True:
    try:
        print("Checking connection...")
        while not wizfi.is_connected:
            print("Connecting to AP...")
            wizfi.connect(secrets)
        while not is_socket_connected:
            print("Connecting to target...")
            is_socket_connected = wizfi.socket_connect(
                "TCP", TARGET_IP, TARGET_PORT)
            if is_socket_connected:
                print("Connected to ", TARGET_IP, ":", TARGET_PORT, sep="")
        data = b"Hello, World!\r\n"
        is_socket_sent = wizfi.socket_send(data)
        if is_socket_sent:
            print("Send OK")
        print("Sleeping for: {0} Seconds".format(TIME_BETWEEN_QUERY))
        time.sleep(TIME_BETWEEN_QUERY)
    except (ValueError, RuntimeError, adafruit_wizfiatcontrol.OKError) as e:
        print("Failed to get data, retrying\n", e)
        print("Resetting WizFi360 module")
        wizfi.hard_reset()
        continue
