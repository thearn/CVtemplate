import cv2
import numpy as np

def stop():
    """
    Used to terminate loop
    """
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    return False

class Camera(object):

    def __init__(self, camera=0):
        self.cam = cv2.VideoCapture(camera)
        if not self.cam:
            raise Exception("Camera not accessible")

        self.shape = self.get_frame().shape

    def get_frame(self):
        _, frame = self.cam.read()
        return frame

if __name__ == "__main__":

    cam = Camera()

    while True:
        frame = cam.get_frame()
        cv2.imshow('Live', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
