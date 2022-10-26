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
import adafruit_requests.adafruit_requests as requests
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
TARGET_URL = "http://wifitest.adafruit.com/testwifi/index.html"
print("Target info:", TARGET_URL)

print("Resetting WizFi360 module")
wizfi.hard_reset()

requests.set_socket(socket, wizfi)

while True:
    try:
        print("Checking connection...")
        while not wizfi.is_connected:
            print("Connecting to AP...")
            wizfi.connect(secrets)
        # great, lets get the data
        print("Retrieving URL...", end="")
        r = requests.get(TARGET_URL)
        print("Status:", r.status_code)
        print("Content type:", r.headers["content-type"])
        print("Content size:", r.headers["content-length"])
        print("Encoding:", r.encoding)
        print("Text:", r.text)
        print("Sleeping for: {0} Seconds".format(TIME_BETWEEN_QUERY))
        time.sleep(TIME_BETWEEN_QUERY)
    except (ValueError, RuntimeError, adafruit_wizfiatcontrol.OKError) as e:
        print("Failed to get data, retrying\n", e)
        print("Resetting WizFi360 module")
        wizfi.hard_reset()
        continue
