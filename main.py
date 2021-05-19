import cv2
def morphological(frame1, frame2):
    motionDiff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(motionDiff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)

    _, th = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(th, None, iterations=3)
    cntr, _ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in cntr:
        [intX, intY, intW, intH] = cv.boundingRect(c)
        cv.rectangle(frame1,  (intX, intY),(intX+intW, intY+intH),(0,255,0),2)
    return frame1
