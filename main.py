import RPi.GPIO as GPIO
import time
import datetime

# Setup global
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

class Motion():
    '''Motion class for finding'''
    def __init__(self):
        '''Constructor'''
        self.last_detected = ''
        self.initialised   = True

    def motion(self, pin):
        '''Motion detection'''
        detected = datetime.datetime.now()
        if self.initialised:
            self.last_detected = datetime.datetime.now()
            print('Motion First Detected: {}'.format(detected))
            self.initialised = False
            return
        delta = detected - self.last_detected
        if delta.total_seconds() > 60:
            self.last_detected = datetime.datetime.now()
            print('New Motion Detected: {}'.format(detected))

    def loop(self):
        '''Loop and wait for event'''
        print('PIR Module Test(CTRL+C to exit)')
        time.sleep(2)
        try:
            GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=self.motion)
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            print('Quit')
            GPIO.cleanup()

motion = Motion()
motion.loop()