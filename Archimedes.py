import math
import time

precision = 10000

for growingNumber in range(1, precision):
    divisionResult = (180 / growingNumber)
    convertRadian = math.radians(divisionResult)
    findSin = math.sin(convertRadian)
    pi = growingNumber * findSin
    print(pi)
    time.sleep(0.00001)
