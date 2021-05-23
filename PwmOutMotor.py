#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PwmOutMotor.py
#
# Solar-boat Project 2021

import pigpio
import time
from Params import Params


class PwmOutMotor:
    # [Motor]
    #
    # [ ESC]
    # Max Update Rate : 400 Hz
    # Stopped     : 1500 microseconds
    # Max forward : 1900 microseconds
    # Max reverse : 1100 microseconds

    frequency = 50

    def __init__(self, pin_servo, pin_motor):
        # GPIO number
        self.pin_servo = pin_servo
        self.pin_motor = pin_motor
        self.servo_pulse_width = 1500
        self.motor_pulse_width = 1500

        # Setup for Out
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_servo, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_motor, pigpio.OUTPUT)
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500)  # neutral
        self.pi.set_servo_pulsewidth(self.pin_motor, 1500)  # neutral
        return

    def finalize(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500)  # neutral
        self.pi.set_servo_pulsewidth(self.pin_motor, 1500)  # neutral
        return

    def update_pulse_width(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, self.servo_pulse_width)
        self.pi.set_servo_pulsewidth(self.pin_motor, self.motor_pulse_width)
        return


# test code
if __name__ == "__main__":
    params = Params()
    sample = PwmOutMotor(params.pin_servo_out, params.pin_motor_out)
    resolution = 20
    pwm_range = 1900 - 1500
    dp = pwm_range / resolution
    servo_pulse_width = 1500
    motor_pulse_width = 1500
    try:
        # move servo motor
        for i in range(resolution):
            time.sleep(0.5)
            servo_pulse_width += dp
            sample.motor_pulse_width = servo_pulse_width
            sample.update_pulse_width()
            print(sample.motor_pulse_width)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        sample.finalize()
