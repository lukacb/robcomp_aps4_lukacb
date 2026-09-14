import cv2
print ("OpenCV Version : %s " % cv2.__version__)

class ProcessImage:
    def __init__(self):
        self.bgr = None


    def load_image(self, path):
        self.bgr = cv2.imread(path)

    def show_image(self):
        cv2.imshow("IMAGEM BGR", self.bgr)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def show_channels(self):
        imagem_b,imagem_g,imagem_r = cv2.split(self.bgr)
        cv2.imshow("IMAGEM B", imagem_b)
        cv2.imshow("IMAGEM G", imagem_g)
        cv2.imshow("IMAGEM R", imagem_r)
        cv2.waitKey()
        cv2.destroyAllWindows()

def main():
    objeto = ProcessImage()
    objeto.load_image("img/arara.jpg")
    objeto.show_image()
    objeto.show_channels()

main()