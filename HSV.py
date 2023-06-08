import cv2

# load image
img = cv2.imread("yumushan.jpg")

# get image size
x = img.shape[1]
y = img.shape[0]

# resize
new_x = 450
new_y = int(new_x * y / x)
img = cv2.resize(img, (new_x, new_y))

# convert to hsv color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV:", hsv[y, x])
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        hsv_space = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(img, hsv_space, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.imshow("Image", img)

# Show image
cv2.imshow("Image", img)

# Assign a pointer to track mouse events
cv2.setMouseCallback("Image", click)

while True:
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()










