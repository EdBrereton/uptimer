#!/usr/bin/env python3

"""
A small script to continuously ping an IFTT endpoint 
to log how long an RPi Zero stays up for when running on battery
"""
import requests
import time

def main():
    while True:
        requests.get("https://maker.ifttt.com/trigger/pi_log/with/key/XXXXXXXXXX")
        time.sleep(60)

if __name__ == '__main__':
    main()