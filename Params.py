#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Params.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#


class Params:
    def __init__(self):
        # pin assign (GPIO)
        self.pin_mode_in = 7  # GPIO  4 # PIN  7
        self.pin_servo_in = 15  # GPIO  22 # PIN  15
        self.pin_thruster_in = 13  # GPIO  27 # PIN  13
        self.pin_servo_out = 16  # GPIO 23 # PIN 16
        self.pin_thruster_out = 18  # GPIO 24 # PIN 18
        self.pin_or = 36  # GPIO 16 # PIN 36 # for OutOfRange signal, not for control


if __name__ == "__main__":
    params = Params()
