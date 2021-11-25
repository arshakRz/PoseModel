import numpy as np
from matplotlib import pyplot as plt
import cv2

Video_FILE = "/Mon_vid.mp4"
mask = cv2.imread('4.png',0)

fourcc = cv2.VideoWriter_fourcc(*'MPV4')
#fourcc = cv2.cv.CV_FOURCC(*'XVID')
video_out = cv2.VideoWriter('new_video.mp4', fourcc, 30, (480,848))

counter = 0


for frame in get_frames(Video_FILE):
    if frame is None:
        break

    dst = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)
    #dst = cv2.inpaint(frame, mask, 3, cv2.INPAINT_NS)

    video_out.write(dst)
    counter += 1
video_out.release()


def get_frames(filename):
    video=cv2.VideoCapture(filename)
    while video.isOpened():
        rete,frame=video.read()
        if rete:
            yield frame
        else:
            break
        video.release()
        yield None