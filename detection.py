import cv2

def blob_detection(image):
    output = cv2.connectedComponentsWithStats(image, cv2.CV_32S)
    (numLabels, labels, stats, centroids) = output
    
    cv2.imwrite('sample_output.jpg', image)


def main():
    image = cv2.imread('asset/sample.jpg')

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

    blob_detection(img_binary)


if __name__ == "__main__":
    main()