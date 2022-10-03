import random
import time
import datetime

def process1():
    t1 = random.randint(0,1)
    print("Waiting for "+str(t1)+" seconds")
    time.sleep(t1)
    print(datetime.datetime.now())