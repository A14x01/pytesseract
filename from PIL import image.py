from PIL import Image
import pytesseract

print('Type the path to the file')
print("Example: E:/x/x/x.exe")

user_path = input(r'')

pytesseract.pytesseract.tesseract_cmd = user_path

print('Please put your picture in the same folder as your python code')
user_image = input('Type name of the .png file')

img = Image.open(user_image)
text = pytesseract.image_to_string(img)

print(text)
