import cv2
import numpy as np

img = cv2.imread("yumushan.jpg")
x = img.shape[1]
y = img.shape[0]

# resize
new_x = 450
new_y = int(new_x * y / x)
img = cv2.resize(img, (new_x, new_y))

hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# trackbar window boyutu ayarlama
cv2.namedWindow("HLS Trackbar")
cv2.resizeWindow("HLS Trackbar", 200, 10)

# global features
h_low = 0
h_high = 179
l_low = 0
l_high = 255
s_low = 0
s_high = 255

# trackbar functions
cv2.createTrackbar("H Low", "HLS Trackbar", h_low, 179, lambda x: x)
cv2.createTrackbar("H High", "HLS Trackbar", h_high, 179, lambda x: x)
cv2.createTrackbar("L Low", "HLS Trackbar", l_low, 255, lambda x: x)
cv2.createTrackbar("L High", "HLS Trackbar", l_high, 255, lambda x: x)
cv2.createTrackbar("S Low", "HLS Trackbar", s_low, 255, lambda x: x)
cv2.createTrackbar("S High", "HLS Trackbar", s_high, 255, lambda x: x)

while True:
    h_low = cv2.getTrackbarPos("H Low", "HLS Trackbar")
    h_high = cv2.getTrackbarPos("H High", "HLS Trackbar")
    l_low = cv2.getTrackbarPos("L Low", "HLS Trackbar")
    l_high = cv2.getTrackbarPos("L High", "HLS Trackbar")
    s_low = cv2.getTrackbarPos("S Low", "HLS Trackbar")
    s_high = cv2.getTrackbarPos("S High", "HLS Trackbar")

    lower = np.array([h_low, l_low, s_low])
    upper = np.array([h_high, l_high, s_high])

    mask = cv2.inRange(hls_img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("HLS Trackbar", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()










