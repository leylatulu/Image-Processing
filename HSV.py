# Ödev: HLS Trackbarı Oluşturma

# Bu ödevde, OpenCV'nin renk uzaylarından biri olan HLS (Hue, Lightness, Saturation) üzerinde çalışacağız.
# OpenCV kütüphanesi, görüntü işleme uygulamalarında renklerin farklı bileşenlerini ayrıştırmak için HLS renk uzayını sıklıkla kullanır.
# Bu ödevde, HSV trackbarından farklı olarak HLS trackbarı oluşturmanızı istiyoruz.

# Aşağıdaki adımları izleyerek HLS trackbarını oluşturmanız beklenmektedir:

# Bir OpenCV projesi başlatın ve bir görüntüyü yükleyin.
# 2.Görüntüyü HLS renk uzayına dönüştürün.
# HLS renk uzayındaki bileşenleri (Hue, Lightness, Saturation) görselleştirmek için üç ayrı trackbar oluşturunuz.
# Trackbarları görüntü penceresine ekleyin ve kullanıcıdan her bir bileşenin değerini ayarlamasını isteyin.
# Sonuç görüntüsünü ekranda gösterin ve kullanıcının trackbarları kullanarak farklı renk bileşenlerini ayarlamasına izin verin.
# Kullanıcı trackbarları hareket ettirdikçe, görüntünün HLS renk uzayındaki değişimini gösteren bir sonuç görüntüsü oluşturun.
# Sonuç görüntüsünü ekranda gösterin ve kullanıcının trackbarları kullanarak farklı renk bileşenlerini ayarlamasına izin verin.
# Bu ödevde, trackbarların doğru şekilde çalıştığından ve görüntünün HLS renk uzayında beklenen şekilde değiştiğinden emin olun. Ayrıca, kullanıcı arayüzüne uygun şekilde düzenlenmiş bir pencere oluşturmayı da unutmayın.
# Not: Ödevi tamamlarken, trackbar değerlerini kullanarak görüntü üzerinde gerçek zamanlı bir güncelleme sağlamayı deneyebilirsiniz. Böylece, trackbarları hareket ettirdikçe anlık olarak görüntünün değişimini görebilirsiniz.

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



################################################
# Ödev: Pikselin HSV Renk Değerlerini Almak

#Bu ödevde, öğrencilere bir resim üzerinde tıklanan bir noktanın HSV (Hue, Saturation, Value) renk değerlerini bulmayı ve ekrana yazdırmayı istiyoruz.

#Aşağıdaki adımları izleyerek bu ödevi tamamlayabilirsiniz:

#Bir OpenCV projesi başlatın ve bir resim yükleyin.
# Fare tıklamasını takip etmek için bir fare olayı işleyicisi (event handler) oluşturun.
# Fare olayı işleyicisini görüntü penceresine bağlayın.
# Fare olayı işleyicisinde, tıklanan noktanın koordinatlarını alın.
# Tıklanan noktanın piksel değerlerini bulmak için OpenCV'nin cv2.cvtColor() fonksiyonunu kullanarak resmi HSV renk uzayına dönüştürün.
# Tıklanan noktanın HSV renk değerlerini alın.
# Elde edilen HSV renk değerlerini ekrana yazdırın.
#Kullanıcı tıkladıkça, yeni noktaların HSV renk değerlerini alarak ekrana yazdırmaya devam edin.

#Bu ödevde, fare olaylarına yanıt verme, piksel değerlerini bulma ve renk uzaylarını kullanma becerilerinizi geliştirme fırsatı bulacaksınız. Ayrıca, kullanıcıdan alınan verileri işleyerek sonuçları görüntülemek için OpenCV'nin işlevlerini kullanma pratiği yapabileceksiniz.

#Not: HSV renk uzayında, renk değerleri genellikle 0-360 arasında bir aralıkta ifade edilirken, doygunluk ve değer (saturasyon ve value) değerleri genellikle 0-1 aralığında ifade edilir. Bu nedenle, elde edilen renk değerlerinin doğru bir şekilde yazdırıldığından emin olun.



############
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










