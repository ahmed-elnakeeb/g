import pytesseract
import numpy as np
import cv2 as cv
from operations import Operations

class myOCR:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        custom_config = r'--oem 3 --psm 6'

    def solveOut(self,imagepath):
        o=Operations()
        real=cv.imread(imagepath)
        img=cv.imread(imagepath,cv.IMREAD_GRAYSCALE)
        img=self.remove_noise(img)
        th=self.thresholding(img)
        th=self.remove_noise(th)
        dl=self.canny(th)

        text=pytesseract.image_to_string(dl)

        h, w= dl.shape
        boxes = pytesseract.image_to_boxes(dl) 
        for b in boxes.splitlines():
            b = b.split(' ')
            real = cv.rectangle(real, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 255, 0), 2)

        o.showImg(real,"")
        return text




    # noise removal
    def remove_noise(self,image):
        return cv.medianBlur(image,5)
    
    #thresholding
    def thresholding(self,image):
        return  cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,1)


    #dilation
    def dilate(self,image):
        kernel = np.ones((4,4),np.uint8)
        return cv.dilate(image, kernel, iterations = 1)
        
    #erosion
    def erode(self,image):
        kernel = np.ones((4,4),np.uint8)
        return cv.erode(image, kernel, iterations = 1)

    #opening - erosion followed by dilation
    def opening(self,image):
        kernel = np.ones((4,4),np.uint8)
        return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

    #canny edge detection
    def canny(self,image):
        return cv.Canny(image, 100, 200)

    #skew correction
    def deskew(self,image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv.warpAffine(image, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
        return rotated

    #template matching
    def match_template(self,image, template):
        return cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)    