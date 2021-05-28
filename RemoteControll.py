##!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SolarBoatProject2021

from Params import Params
from PwmOut import PwmOut
from PwmRead import PwmRead


import sys


class RemoteControll:
    def __init__(self):
        self._params = Params()
        self._pwm_read = PwmRead(
            self._params.pin_mode_in,
            self._params.pin_servo_in,
            self._params.pin_thruster_in,
            self._params.pin_or,
        )
        self._pwm_out = PwmOut(
            self._params.pin_servo_out, self._params.pin_thruster_out
        )
