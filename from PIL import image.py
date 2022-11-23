from PIL import Image
import pytesseract

print('This python code can read text from files and convert it to just a text')

while True:
    print('If you want to contineu type (1).\nIf you want to exit type (2)')
    user_answer = input('')
    if user_answer == '1':
        try:
            print('Type the path to the tesseract.exe file: ')
            print("Example: E:/x/x/x.exe")

            user_path = input(r'')

            pytesseract.pytesseract.tesseract_cmd = user_path

            print('Please put your picture in the same folder as your python code')
            user_image = input('Type name of the .png file:\n')

            img = Image.open(user_image)
            text = pytesseract.image_to_string(img)

            print('Please wait\n')

            print(text)
        except:
            print("Wrong path to file or name of the .png file")
            continue
    elif user_answer == '2':
        quit()
    else:
        print("Wrong number")
