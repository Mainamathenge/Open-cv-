import cv2
print (cv2.__version__)
dispW=320
dispH=240
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)
boxw=int(0.2*dispW)
boxh=int(0.3*dispH)
posx=10
posy=270
dx=2
dy=2
print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()
    roi=frame[posy:posy+boxh,posx:posx+boxw].copy()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    roi=frame[posy:posy+boxh,posx:posx+boxw]
    cv2.rectangle(frame,(posx,posy),(posx+boxw,posy+boxh),(0,0,255),2)
    cv2.imshow('picam',frame)
    posx=posx+dx
    posy=posy+dken
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
