import cv2
import numpy as np

class ProcessImage():
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

        low_g = np.array([35, 150, 50])
        high_g = np.array([85, 255, 255])
        self.mask_green = cv2.inRange(self.hsv, low_g, high_g)

        low_b = np.array([90, 150, 50])
        high_b = np.array([140, 255, 255])
        self.mask_blue = cv2.inRange(self.hsv, low_b, high_b)

        low_r1 = np.array([0, 200, 50])
        high_r1 = np.array([10, 255, 255])
        low_r2 = np.array([150, 200, 50])
        high_r2 = np.array([179, 255, 255])
        self.mask_red = cv2.inRange(self.hsv, low_r1, high_r1) + cv2.inRange(self.hsv, low_r2, high_r2)

        self.mask = self.mask_green + self.mask_blue + self.mask_red 

    def show_image(self):
        cv2.imshow("Original", self.bgr)
        cv2.imshow("Mask",self.mask)

def main():
    objeto = ProcessImage()
    webcam = cv2.VideoCapture(0)
    while True:
        val, image = webcam.read()
        objeto.run_image(image)
        objeto.show_image()
        if cv2.waitKey(1) == 13: # Aguarda 1 ms pela tecla 'ESC'
            break
        
  
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
