import cv2

scale_percent = 50
source = "Agartala.jpg"
destination = "newImage.png"

image = cv2.imread("Agartala.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)
cv2.waitKey(0)

new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)

dsize = (new_width,new_height)
output = cv2.resize(image,(new_width,new_height))
cv2.imwrite('destination', output)
cv2.waitKey(0)
