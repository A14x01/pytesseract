from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER_NAME\AppData\Local\Tesseract-OCR\tesseract.exe'

img = Image.open('example.png')
text = pytesseract.image_to_string(img)

print(text)