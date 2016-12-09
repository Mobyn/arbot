import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import random
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering
import math

class sensors():
  def __init__(self):
    self.LEFT_TRIG = 5
    self.LEFT_ECHO = 12
    self.RIGHT_TRIG = 17
    self.RIGHT_ECHO = 23
    self.RADAR_TRIG = 20
    self.RADAR_ECHO = 21
    self.OTHER_TRIG = 19
    self.OTHER_ECHO = 16

    GPIO.setup(self.LEFT_TRIG, GPIO.OUT)
    GPIO.setup(self.LEFT_ECHO, GPIO.IN)
    GPIO.setup(self.RIGHT_TRIG, GPIO.OUT)
    GPIO.setup(self.RIGHT_ECHO, GPIO.IN)
    GPIO.setup(self.RADAR_TRIG, GPIO.OUT)
    GPIO.setup(self.RADAR_ECHO, GPIO.IN)
    GPIO.setup(self.OTHER_TRIG, GPIO.OUT)
    GPIO.setup(self.OTHER_ECHO, GPIO.IN)

    self.right_sensor = [self.RIGHT_TRIG, self.RIGHT_ECHO]
    self.left_sensor = [self.LEFT_TRIG, self.LEFT_ECHO]
    self.other_sensor = [self.OTHER_TRIG, self.OTHER_ECHO]

  def get_distance(self, (TRIG, ECHO)):

    pulse_start = time.time()
    pulse_end = time.time()
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
      pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
      pulse_end = time.time()
      if  pulse_end - pulse_start > 0.00587:
        return 200

    distance = ((pulse_end - pulse_start) * 34300) / 2
    time.sleep(.01)

    return distance

  def average_distance(self, sensor):
    sampled_distance = lambda n: sum([self.get_distance(sensor) for n in range(n)]) / float(n)
    distance = sampled_distance(100)
    return distance


    """
    reading = None
    av_distance = []
    for i in range(1, 8):
      if reading is None:
        reading = self.get_distance(sensor)
        print "reading %s = %s" % (i, reading)
      else:
        reading2 = self.get_distance(sensor)
        if reading2 <= (reading * 3) or reading2 >= reading * .25:
          reading = reading2
        else:
          reading = None
        print "reading %s = %s" % (i, reading)
      if reading is not None:
        av_distance.append(reading)
    print av_distance
    if len(av_distance) > 1:
      return sum(av_distance) / float(len(av_distance))
    else:
      return None
    """

  def forward_left(self):

    left = self.get_distance(self.left_sensor)
    return left

  def forward_right(self):
    right = self.get_distance(self.right_sensor)
    return right

  def other_sen(self):
    other = self.get_distance(self.other_sensor)
    return other


  def pulse(self, TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
      pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
      pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)
    if distance > 2 and distance < 400:  # Check whether the distance is within range
      return distance - 0.5
    else:
      return None













