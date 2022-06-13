import cv2
print (cv2.__version__)
dispW=320
dispH=240
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)
print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.imshow('picam2',frame)
    cv2.moveWindow('picam2',340,0)
    cv2.moveWindow('picam',0,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayvid',gray)
    cv2.imshow('grayvid2',gray)
    cv2.moveWindow('grayvid',0,250)
    cv2.moveWindow('grayvid2',340,250)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()