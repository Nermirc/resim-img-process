import cv2

#içe aktarma
img = cv2.imread("C:/Users/rakri/.spyder-py3/imgprocess/messi.jpg", 0)

#görsellestirme
cv2.imshow("Messi", img)
k = cv2.waitKey(0)  &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): #s
    save_path = "C:/Users/rakri/.spyder-py3/imgprocess/messi_gray.png"
    cv2.imwrite("messi _gray.png", img)
    cv2.destroyAllWindows()
    