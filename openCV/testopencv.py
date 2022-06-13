import cv2
print (cv2.__version__)
goflag=0
def mouse_click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goflag
    if event==cv2.EVENT_LBUTTONDOWN:
        
        x1=x
        y1=y
        goflag=0
    if event==cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y
        goflag=1
cv2.namedWindow('picam')
cv2.setMouseCallback('picam',mouse_click)
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
    if goflag==1:
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),4)
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('ROI',roi)
        cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
