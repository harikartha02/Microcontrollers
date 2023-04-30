# from machine import Pin
from time import sleep
from hx711 import HX711

# Set up the stepper motor driver
step_pin = Pin(2, Pin.OUT)
dir_pin = Pin(1, Pin.OUT)
enable_pin = Pin(4, Pin.OUT)
dir_pin.value(1)  # set the initial direction of rotation
enable_pin.value(0)  # enable the driver
buz_pin = Pin(34, Pin.OUT)  # buzzer

# Set up the weight sensor
pin_OUT = Pin(7, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(9, Pin.OUT)
hx = HX711(pin_SCK, pin_OUT)
hx.tare()
hx.set_scale(1)  # adjust this value to calibrate the sensor

# Define the weight thresholds for full and empty
full_weight = 1  # adjust this value to match your pill container
empty_weight = 0.5  # adjust this value to match your pill container

# Dispense a pill


def dispense():
    steps_per_revolution = 200  # adjust this value to match your stepper motor
    # rotate the motor 2 full revolutions (90 degree - edit)
    steps = steps_per_revolution * 1/4
    for i in range(steps):
        step_pin.value(1)
        time.sleep(3)
        step_pin.value(0)
        time.sleep(3)


# Main loop
while True:
    weight = hx.read()
    if weight > full_weight:
        print("Container is full")
    elif weight < empty_weight:
        print("Container is empty, dispensing a pill")
        dispense()
        buz_pin.value(1)  # buzzer
        sleep(5)
        step_pin.value(0)
        sleep(5)
    else:
        print("Container is partially full")

    sleep(1)  # adjust this value to control the frequency of weight measurements
