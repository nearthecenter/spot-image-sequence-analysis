import numpy as np
import cv2

cap = cv2.VideoCapture("physci-edited.m4v")
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # The declaration of CLAHE 
    # clipLimit -> Threshold for contrast limiting
  clahe = cv2.createCLAHE(clipLimit = 1)
  final_img = clahe.apply(gray) + 1
    # Showing all the images
  cv2.imshow("CLAHE", final_img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
