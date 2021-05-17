import cv2

def blob_detection(image):
    return


def main():
    image = cv2.imread('asset/sample.jpg')

    img_gray = cv2.cvtColor(image, cv2.BGR2GRAY)
    
    blob_detection(image)


if __name__ == "__main__":
    main()