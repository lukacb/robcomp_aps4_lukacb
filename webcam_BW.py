import cv2

class ProcessImage():
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image
        self.gray = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2GRAY)
        
        self.processada = self.gray.copy()
        self.processada[self.processada >= 128] = 255
        self.processada[self.processada < 128] = 0

    def show_image(self):
        cv2.imshow("",self.processada)

def main():
    objeto = ProcessImage()
    webcam = cv2.VideoCapture(0)
    while True:
        val, image = webcam.read()
        if val:
            objeto.run_image(image)
            objeto.show_image()
        if cv2.waitKey(1) == 27: # Aguarda 1 ms pela tecla 'ESC'
            break
        
    cv2.destroyAllWindows()
    webcam.release()

main()
