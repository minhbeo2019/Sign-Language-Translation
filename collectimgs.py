import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3 # classes for each gesture in the alphabet. testing so its just 3 for now
dataset_size = 100 ## number of pictures taken for each class

cap = cv2.VideoCapture(0) # opens camera
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))): # creating folders for classes
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press C to initiate ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('c'): # bam C thi bat dau lenh chup anh
            break

    counter = 0 ## dem anh
    while counter < dataset_size: #dem den khi du 100 buc,
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
