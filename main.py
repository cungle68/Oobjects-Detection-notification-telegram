import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

# Check camera
video = VideoStream(src=0).start()

# Contains user-selected points, to create a polygon
points = []

# New model
model = YoloDetect()

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0, 0, 255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255, 0, 0), thickness=2)
    return frame


detect = False

while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)

    # draw ploygon
    frame = draw_polygon(frame, points)

    if detect:
        #frame = model.detect(frame, points)
        frame = model.detect(frame=frame, points=points)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        points.append(points[0])
        detect = True

    # Output to the screen
    cv2.imshow("Intrusion Warning", frame)
    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

video.stop()
#video.release()
cv2.destroyAllWindows()


