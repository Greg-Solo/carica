from pathlib import Path

import cv2
import time

# Path("train").mkdir(exist_ok=True)
# Path("test").mkdir(exist_ok=True)

cam = cv2.VideoCapture(0)

print("Cam warmup...")
for i in range(50):
    ret, _ = cam.read()
    time.sleep(10 / 1000)

print("Taking train data: ")
for i in range(70):
    print(f"take " + str(i))
    ret, img = cam.read()
    cv2.imwrite("./train/capture_" + str(i) + ".jpg", img)
    time.sleep(500 / 1000)

time.sleep(5)

print("Taking test data: ")
for i in range(30):
    print(f"take " + str(i))
    ret, img = cam.read()
    cv2.imwrite("./test/capture_" + str(i) + ".jpg", img)
    time.sleep(500 / 1000)

print("DONE")
cam.release()
