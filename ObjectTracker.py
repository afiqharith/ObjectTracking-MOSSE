import cv2
import winsound

BLUE = (255,0,0)
VIDEOPATH = 'video.mp4'
CAMERA = False
FREQUENCY = 2700
DURATION = 50

if CAMERA == True:
    video = cv2.VideoCapture(0)
else:
    video = cv2.VideoCapture(VIDEOPATH)

tracker = cv2.TrackerMOSSE_create()

ret, frame = video.read()
bbox = cv2.selectROI('Tracker', frame, False)

tracker.init(frame, bbox)

while video.isOpened():

    ret, frame = video.read()

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE, 2)

    else:
        winsound.Beep(FREQUENCY, DURATION)
        print(f'[ERROR] Object tracked lost.')


    cv2.imshow('Tracker', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break