import cv2
print (cv2.__version__)
dispW=240
dispH=180
flip = 2
cvlogo=cv2.imread('cv.jpg')
cvlogo=cv2.resize(cvlogo,(240,180))
cvlogoGray=cv2.cvtColor(cvlogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('LOGO gray',cvlogoGray)
cv2.moveWindow('LOGO gray',0,220)

_,BGmask=cv2.threshold(cvlogoGray,155,255,cv2.THRESH_BINARY)
cv2.imshow('BG MASK',BGmask)
cv2.moveWindow('BG MASK',300,0)

FGmask=cv2.bitwise_not(BGmask)
cv2.imshow('FGmask',FGmask)
cv2.moveWindow('FGmask',600,0)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#cam=cv2.VideoCapture(0)
print(f'this is the result {cam.read()}')
while True:
    ret , frame = cam.read()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    BG=cv2.bitwise_and(frame,frame,mask=BGmask)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',300,180)


    #frame=cv2.rectangle(frame,(140,100),(180,140),(255,0,0),4)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
