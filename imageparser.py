from PIL import Image
import pytesseract

def parse_image(tcmd, file):
    return parse_image_as_image(tcmd, Image.open(file))
    
def parse_image_as_image(tcmd, img):
    pytesseract.pytesseract.tesseract_cmd = tcmd
    s = pytesseract.image_to_string(img)
    return s
