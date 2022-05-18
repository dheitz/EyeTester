import cv2
image = cv2.imread("DSC_0808.JPG")
print(image.shape)
cv2.imshow("Image", image)
cv2.waitKey(0)
scaled_image = cv2.resize(image, 
[224,224])
cv2.imshow("Scaled Image Bilinear", scaled_image)
cv2.waitKey(0)
scaled_image = cv2.resize(image, [224,224], 
interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Scaled Image Lanczos", scaled_image)
cv2.waitKey(0)
