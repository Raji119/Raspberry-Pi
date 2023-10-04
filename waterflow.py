import RPi.GPIO as GPIO
import time

# Pin connected to the YF-S201 sensor's output
FLOW_SENSOR_PIN = 17

# Define water flow variables
total_flow = 0.0
last_time = time.time()

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def count_pulse(channel):
    global total_flow, last_time
    total_flow += 1
    current_time = time.time()
    flow_rate = 1.0 / (current_time - last_time)
    last_time = current_time
    print(f"Flow rate: {flow_rate:.2f} L/s")

# Add an event listener for the sensor pulses
GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.FALLING, callback=count_pulse)

try:
    while True:
        # Main loop - You can add your billing calculation logic here
        # For example, calculate total consumption over time and apply rate

        time.sleep(1)  # You can adjust the interval for calculations

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
