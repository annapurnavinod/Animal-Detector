import cv2

cap = cv2.VideoCapture(0)

ret,frame1 = cap.read()
ret,frame2 = cap.read()
while (cap.isOpened):
    cv2.putText(frame1,"To quit:{}".format("Press 'q'"), (480,470),cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    ret,thr = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilute = cv2.dilate(thr,None,iterations = 3)
    contour,hierarcy = cv2.findContours(dilute, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contour:
        (x,y,w,h) = cv2.boundingRect(i)
        if cv2.contourArea(i) < 10000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,0,255),3)
        cv2.putText(frame1, "status:{}".format('Movement'), (10,20),cv2.FONT_HERSHEY_SIMPLEX,1, (255,0,0),3)
    cv2.imshow("output", frame1)
    frame1 = frame2
    ret,frame2 = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
