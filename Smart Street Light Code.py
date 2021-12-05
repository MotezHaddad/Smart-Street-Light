import time
import board                     #Library of board
import adafruit_bh1750           #Library of Brightness sensor
import digitalio               
import RPi.GPIO as GPIO  


def Config_LED():
    LED=25                       # pin number
    GPIO.setmode (GPIO.BOARD)    # choose BCM or BOARD numbering schemes. I use BCM  
    GPIO.setup (LED, GPIO.OUT)   # set GPIO 25 as output for white led  
    PWM_LED = GPIO.PWM(LED, 100) # create object PWM_LED for PWM on port 25 at 100 Hertz  
    PWM_LED.start(0)             # off


def Config_BH1750():
    i2c = board.I2C()            # Pin I2C 
    
    # Setup LUX sensor:
    sensor = adafruit_bh1750.BH1750(i2c)


def Config_PIR():
    PIR_PIN = board.D2           # Pin number connected to PIR sensor output wire.
     
    # Setup digital input for PIR sensor:
    pir = digitalio.DigitalInOut(PIR_PIN)
    pir.direction = digitalio.Direction.INPUT

# setup all components



Config_LED()
Config_BH1750()
Config_PIR()



def Duty_steps():
    i=30
    while i < 100:
        time.sleep(0.3)
        i+=2
        PWM_LED.ChangeDutyCycle(i)


def Duty_steps_1():
    i=100
    while i > 30:
        time.sleep(0.3)
        i-=2
        PWM_LED.ChangeDutyCycle(i)


def Movement_Detection ():
    pir_value = pir.value
        
    if pir_value:
        # PIR is detecting movement! Turn on LED on 100 %
        if old_value!=pir_value:
            Duty_steps()
        time.sleep(300)
       
    else:
        # PIR is not detecting movement. Turn LED on 30 %
        if old_value !=pir_value:
            Duty_steps_1()
    old_value=pir_value
        


# Main


while True:

    while sensor.lux < 400:
        Movement_Detection()
    PWM_LED.ChangeDutyCycle(0)

