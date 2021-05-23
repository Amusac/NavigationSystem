#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PwmOutthruster.py
#
# Solar-boat Project 2021

import pigpio  # pigpioモジュールを使用
import time
from Params import Params

# pigpioの準備
pi = pigpio.pi()


class PwmOutthruster:
    # [thruster]
    #
    # [ ESC]
    # Max Update Rate : 400 Hz
    # Stopped     : 1500 microseconds
    # Max forward : 1900 microseconds
    # Max reverse : 1100 microseconds

    frequency = 50

    def __init__(self, pin_servo, pin_thruster):
        # GPIO number
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.servo_pulse_width = 1500
        self.thruster_pulse_width = 1500

        # Setup for Out
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_servo, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_thruster, pigpio.OUTPUT)
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500)  # neutral
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
    params = Params()
    sample = PwmOutthruster(params.pin_servo_out, params.pin_thruster_out)
    resolution = 5
    pwm_range = 1900 - 1500
    dp = pwm_range / resolution
    servo_pulse_width = 1500
    thruster_pulse_width = 1500
    try:
        # move thruster
        print("Turning thruster on")
        pi.write(sample.pin_thruster,1)
        time.sleep(resolution)
        print("Turning thruster off")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        sample.finalize()
