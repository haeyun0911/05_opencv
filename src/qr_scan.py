import cv2
import matplotlib.pyplot as plt
import pyzbar.pyzbar as pyzbar
import webbrowser
import time

#img = cv2.imread('../img/frame.png')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

last_scan_time = 0
cooldown_period = 5

#plt.imshow(img)
#plt.imshow(gray,cmap='gray')
#plt.show()
while(cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



    #디코딩
    decoded = pyzbar.decode(gray)
    #print(decoded)

    if decoded and (time.time()-last_scan_time)>cooldown_period:
        for d in decoded:
            x,y,w,h = d.rect
            #print(d.data.decode('utf-8'))
            barcode_data = d.data.decode('utf-8')
            #print(d.type)
            barcode_type=d.type

            text = '%s(%s)' % (barcode_data, barcode_type)

            #cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0]+d.rect[2], d.rect[1]+d.rect[3]), (0,255,0),20)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.putText(img,text,(d.rect[0],d.rect[1]-50), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0),2,cv2.LINE_AA)
            cv2.putText(img,text,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 2, cv2.LINE_AA)
       
            if not is_opened:
                url=barcode_data
                webbrowser.open(url)
                is_opened = True

    cv2.imshow('camera', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()

#plt.imshow(img)
#plt.show()

#cv2.waitKey(0)
cv2.destroyAllWindows()
