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
        self.pi.set_servo_pulsewidth(self.pin_thruster, 1100)  # neutral
        return

    def update_pulse_width(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, self.servo_pulse_width)
        self.pi.set_servo_pulsewidth(self.pin_thruster, self.thruster_pulse_width)
        return


# test code
if __name__ == "__main__":

    try:
        # pigpioの準備
        pi = pigpio.pi()

        params = Params()
        minPulse = 700
        maxPulse = 2000

        print("Initialaze Brushless Motor. Please remove the battery.")

        pi.set_servo_pulsewidth(params.pin_thruster_out, maxPulse)

        print("Connect the battery and press Enter.")
        inp = input()
        if inp == "":
            pi.set_servo_pulsewidth(params.pin_thruster_out, minPulse)
            time.sleep(3)

        print('"stop"')
        print('"u" to up speed')
        print('"d" to down speed')
        speed = 1000
        print("speed = %d" % speed)
        while True:
            pi.set_servo_pulsewidth(params.pin_thruster_out, speed)
            inp = input()
            if inp == "d":
                speed -= 100
                print("speed = %d" % speed)
            elif inp == "u":
                speed += 100  # incrementing the speed like hell
                print("speed = %d" % speed)
            elif inp == "stop":
                speed = 0
                pi.set_servo_pulsewidth(params.pin_thruster_out, 0)
                break
            else:
                print("stop or u or d!")
        pi.stop()
        print("Execution Successed.")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        print("Execution finished.")
