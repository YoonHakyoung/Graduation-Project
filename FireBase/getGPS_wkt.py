from getGPS import get_gps
from time import sleep

while True:
    startGPS, endGPS = get_gps()
    print(startGPS, endGPS)
    # 1초 동안 대기
    sleep(1)