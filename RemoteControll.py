##!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SolarBoatProject2021

from Params import Params
from PwmOut import PwmOut
from PwmRead import PwmRead


import sys
import time


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

    def do_operation(self):
        # update pwm
        # Read pwm pulse width
        self._pwm_read.measure_pulse_width()
        # Set the readout signals as the output signals
        self._pwm_out.servo_pulse_width = self._pwm_read.pulse_width["servo"]
        self._pwm_out.thruster_pulse_width = self._pwm_read.pulse_width["thruster"]

        # self._update_mode()

        # for test
        self._pwm_read.print_pulse_width()

        # mode = self._status.mode
        # if mode == "RC":
        #     pass
        # elif mode == "AN":
        #     self._auto_navigation()
        # elif mode == "OR":
        #     self._out_of_range_operation()

        self._pwm_out.update_pulse_width()
        # self._print_log()
        # time.sleep(self._sleep_time)

    # def _update_mode(self):
    #     mode_duty_ratio = self._pwm_read.pulse_width["mode"]
    #     or_pulse = self._pwm_read.pulse_width["OR"]
    #     # OR mode
    #     if or_pulse < 1300 or (1500 <= mode_duty_ratio and self._or_experienced):
    #         if not self._or_experienced:
    #             self._status.update_way_point()
    #         self._status.mode = "OR"
    #         self._or_experienced = True
    #     # RC mode
    #     elif 0 < mode_duty_ratio < 1500:
    #         self._status.mode = "RC"
    #     # AN mode
    #     elif 1500 <= mode_duty_ratio and not self._or_experienced:
    #         self._status.mode = "AN"
    #     else:
    #         print("Error: mode updating failed", file=sys.stderr)

    def finalize(self):
        self._pwm_read.finalize()
        self._pwm_out.finalize()
        return


if __name__ == "__main__":
    print("RemoteControll.py")
    driver = RemoteControll()
    try:
        # Control Loop
        driver.do_operation()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        # If you finalize this program,
        # this program set the system to stop
        driver.finalize()
        print("finish")
