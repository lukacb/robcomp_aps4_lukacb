import cv2
import numpy as np
import time
print ("OpenCV Version : %s " % cv2.__version__)


class ProcessImage():
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        self.bgr_lida = cv2.imread(self.bgr)
        
        height, width, channels = self.bgr_lida.shape

        self.bgr_lida[:int(height/2), int(width/3):int((width/3)*2),:] = 0
        self.bgr_lida[int(height/2):,:int(width/3),:] = 0
        self.bgr_lida[int(height/2):,int((width/3)*2):,:] = 0
        
    
        cv2.imshow("", self.bgr_lida)
        cv2.waitKey()
        cv2.destroyAllWindows()
        print(width)

def main():
    objeto = ProcessImage()
    objeto.run_image('img/arara.jpg')
    objeto.show_image()
    objeto.show_channels()

main()

