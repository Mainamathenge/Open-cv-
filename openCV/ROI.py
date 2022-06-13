import cv2
print (cv2.__version__)
dispW=320
dispH=200
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)

print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()
    roi=frame[50:150,150:200]
    roigray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',roigray)
    cv2.imshow('picam',frame)
    cv2.imshow('roi',roi)
    cv2.moveWindow('picam',0,0)
    cv2.moveWindow('roi',450,0) 
    cv2.moveWindow('roigray',450,450)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
