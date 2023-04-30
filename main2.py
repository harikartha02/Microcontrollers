#from machine import Pin
from time import sleep
from hx711 import HX711

# Set up the stepper motor driver
step_pin = Pin(22, Pin.OUT)
dir_pin = Pin(21, Pin.OUT)
enable_pin = Pin(20, Pin.OUT)
dir_pin.value(1)  # set the initial direction of rotation
enable_pin.value(0)  # enable the driver

# Set up the weight sensor
hx = HX711(dout_pin=5, pd_sck_pin=6)
hx.set_scale(1)  # adjust this value to calibrate the sensor
hx.reset()
hx.tare()

# Define the weight thresholds for full and empty
full_weight = 500  # adjust this value to match your pill container
empty_weight = 100  # adjust this value to match your pill container

# Dispense a pill
def dispense():
    steps_per_revolution = 200  # adjust this value to match your stepper motor
    steps = steps_per_revolution * 2  # rotate the motor 2 full revolutions
    for i in range(steps):
        step_pin.value(1)
        sleep(0.001)
        step_pin.value(0)
        sleep(0.001)

# Main loop
while True:
    weight = hx.get_weight()
    if weight > full_weight:
        print("Container is full")
    elif weight < empty_weight:
        print("Container is empty, dispensing a pill")
        dispense()
    else:
        print("Container is partially full")

    sleep(1)  # adjust this value to control the frequency of weight measurements
