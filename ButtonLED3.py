import RPi.GPIO as GPIO
import time

ledPin = 11    # define the ledPin
buttonPin = 12    # define the buttonPin
status = False

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set buttonPin's mode is input, and pull up to high level(3.3V)

def loop(status):
    while True:
        #print("status: "+str(status))
        if GPIO.input(buttonPin)==GPIO.LOW:
            if status == False:
                status = True
            else:
                status = False
            time.sleep(0.5)

        if status == True:
            GPIO.output(ledPin, GPIO.HIGH)
            print("led an!")
        else:
            GPIO.output(ledPin, GPIO.LOW)
            print("led aus!")
                  

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        print ('Program loops')
        loop(status)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
