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
import rtc

from adafruit_wizfiatcontrol import (
    adafruit_wizfiatcontrol,
    adafruit_wizfiatcontrol_wifimanager,
)


# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("Wi-Fi secrets are kept in secrets.py, please add them there!")
    raise

# Debug Level
# Change the Debug Flag if you have issues with AT commands
debugflag = False

# How Long to sleep between polling
sleep_duration = 60  # in seconds

# WizFi360 configuration
RX = board.GP5
TX = board.GP4
resetpin = DigitalInOut(board.GP20)
rtspin = False
uart = busio.UART(TX, RX, baudrate=11520,
                  receiver_buffer_size=2048)
status_light = None

print("WizFi360 AT commands")
wizfi = adafruit_wizfiatcontrol.WizFi_ATcontrol(
    uart, 115200, reset_pin=resetpin, rts_pin=rtspin, debug=debugflag
)
print("AT software version:", wizfi.get_version())

wifi = adafruit_wizfiatcontrol_wifimanager.WizFiAT_WiFiManager(
    wizfi, secrets, status_light)

# Target settings
TARGET_URL = "http://worldtimeapi.org/api/ip"
print("Target info:", TARGET_URL)

print("Resetting WizFi360 module")
wizfi.hard_reset()

print("WizFi360 local time")

the_rtc = rtc.RTC()

response = None
while True:
    try:
        print("Fetching json from", TARGET_URL)
        response = wifi.get(TARGET_URL)
        break
    except (ValueError, RuntimeError, adafruit_wizfiatcontrol.OKError) as e:
        print("Failed to get data, retrying\n", e)
        continue

json = response.json()
current_time = json["datetime"]
the_date, the_time = current_time.split("T")
year, month, mday = [int(x) for x in the_date.split("-")]
the_time = the_time.split(".")[0]
hours, minutes, seconds = [int(x) for x in the_time.split(":")]

# We can also fill in these extra nice things
year_day = json["day_of_year"]
week_day = json["day_of_week"]
is_dst = json["dst"]

now = time.struct_time(
    (year, month, mday, hours, minutes, seconds, week_day, year_day, is_dst)
)
print(now)
the_rtc.datetime = now

while True:
    print(time.localtime())
    print("Sleeping for: {0} Seconds".format(sleep_duration))
    time.sleep(sleep_duration)
