import cv2
print (cv2.__version__)
dispW=240
dispH=180
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)
print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #frame=cv2.rectangle(frame,(140,100),(180,140),(255,0,0),4)
    print(gray.shape)
    b=cv2.split(frame)[0]
    cv2.imshow('blue',b)
    cv2.moveWindow('blue',300,0)
    #cv2.imshow('GRAY',gray)
    #cv2.moveWindow('GRAY',300,0)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
