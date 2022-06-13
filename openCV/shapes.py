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
    frame=cv2.rectangle(frame,(140,100),(180,140),(255,0,0),4)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picom',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
