#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TestThruster.py
#
# Solar-boat Project 2021

import pigpio  # pigpioモジュールを使用
import time
from Params import Params


class TestThruster:
    # [thruster]
    #
    # [ ESC]
    # Max Update Rate : 400 Hz
    # Stopped     : 1500 microseconds
    # Max forward : 1900 microseconds
    # Max reverse : 1100 microseconds

    frequency = 50

    def __init__(self, pin_thruster):
        # GPIO number
        self.pin_thruster = pin_thruster

        # Setup for Out
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_thruster, pigpio.OUTPUT)
        self.pi.set_servo_pulsewidth(self.pin_thruster, 1500)  # neutral
        return

    def finalize(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500)  # neutral
        self.pi.set_servo_pulsewidth(self.pin_thruster, 1500)  # neutral
        return

    def update_pulse_width(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, self.servo_pulse_width)
        self.pi.set_servo_pulsewidth(self.pin_thruster, self.thruster_pulse_width)
        return


# test code
if __name__ == "__main__":

    # pigpioの準備
    pi = pigpio.pi()

    params = Params()
    sample = TestThruster(params.pin_thruster_out)
    testtime = 5
    freq = 2  # frequency
    duty = 500000  # duty
    thruster_pulse_width = 1500
    try:
        # move thruster
        print("Turning thruster on")
        pi.hardware_PWM(params.pin_thruster_out, freq, duty)
        time.sleep(testtime)
        print("Turning thruster off")
        pi.stop()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        print("Execution finished.")
        sample.finalize()
