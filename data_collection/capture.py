from pathlib import Path

import cv2
import time


def main():
    Path("train").mkdir(exist_ok=True)
    Path("test").mkdir(exist_ok=True)

    cam = cv2.VideoCapture(0)

    print("Cam warmup...")
    for i in range(50):
        ret, _ = cam.read()
        time.sleep(10 / 1000)

    print("\nTaking train data: ")
    for i in range(150):
        print(f"take " + str(i + 1))
        ret, img = cam.read()
        cv2.imwrite("./train/capture_" + str(i + 1) + ".jpg", img)
        time.sleep(100 / 1000)

    print("\nSaving...")
    time.sleep(5)

    print("\nTaking test data: ")
    for i in range(50):
        print(f"take " + str(i + 1))
        ret, img = cam.read()
        cv2.imwrite("./test/capture_" + str(i + 1) + ".jpg", img)
        time.sleep(100 / 1000)

    print("\nDONE")
    cam.release()


if __name__ == "__main__":
    main()
