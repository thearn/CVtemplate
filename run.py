from camera import Camera, cv2, np, stop

cam = Camera()

while True:
    frame = cam.get_frame()

    cv2.imshow('Live', frame)

    if stop():
        break
