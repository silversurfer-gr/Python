import RPi.GPIO as GPIO
import time

ledPin = 5    # RPI Board pin17
dauer  = 5

def setup():
    print("setup ist entert")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led print ('using pin%d'%ledPin)
        # Numbers GPIOs by physical location # Set ledPin's mode is output

def loop():
    print("loop is entert")
    while True:
        print("is looping LED-Pin: "+str(ledPin))
        GPIO.output(ledPin, GPIO.HIGH) # led on print ('...led on')
        print("LED on")
        time.sleep(dauer)
        GPIO.output(ledPin, GPIO.LOW) # led off print ('led off...')
        print("LED off")
        time.sleep(dauer)

def destroy():
    print("destroy is entert")
    GPIO.output(ledPin, GPIO.LOW) # led off
    GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()
