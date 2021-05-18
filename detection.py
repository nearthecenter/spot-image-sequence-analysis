import cv2
import numpy as np

def blob_detection(image, raw):
    components = cv2.connectedComponentsWithStats(image, 8, cv2.CV_32S)
    (numLabels, labels, stats, centroids) = components
    
    output = raw.copy()

    for i in range(0, numLabels):
        #exclude backgrouund
        if (i==0): continue

        #get bounding box
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]

        #get centroids
        (centroid_x, centroid_y) = centroids[i]

        #get component mask
        component_mask = (labels == i).astype("uint8") * 255

        #generate random color for each blob
        color_list = (list(np.random.choice(range(256), size=3)))  
        random_color = (int(color_list[0]), int(color_list[1]), int(color_list[2]))

        #color the blob
        output[(component_mask != 0)] = random_color

    cv2.imwrite(f"output.jpg", output)
    return output


def main():
    image = cv2.imread('asset/sample.jpg')

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3,3),np.uint8)
    img_mt = cv2.erode(img_binary, kernel)
    blob_detection(255 - img_mt, image)


if __name__ == "__main__":
    main()