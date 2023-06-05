import cv2

# Bir görüntüyü yükle
img = cv2.imread("yumushan.jpg")

x = img.shape[1]
y = img.shape[0]

# resize
new_x = 450
new_y = int(new_x * y / x)
img = cv2.resize(img, (new_x, new_y))

# Görüntüyü HSV renk uzayına dönüştür
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV:", hsv[y, x])
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        hsv_uzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(img, hsv_uzayi, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.imshow("Image", img)


# Görüntüyü ekranda göster
cv2.imshow("Image", img)

# Fare olaylarını takip etmek için bir işaretçi ata
cv2.setMouseCallback("Image", click)

# ESC tuşuna basılana kadar döngüyü devam ettir
while True:
    if cv2.waitKey(1) == 27:
        break
# Pencereyi kapat
cv2.destroyAllWindows()










