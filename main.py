import requests
from PIL import Image


def img_request(txt):
    response = requests.get("https://source.unsplash.com/1920x1080?{0}".format(txt))
    file = open('image.jpg', 'wb')
    file.write(response.content)
    img = Image.open(r"image.jpg")
    img.show()
    file.close()


print("""Select an animal!!!!!
    1. Hedgehog
    2. Dog
    3. Cat
    4. Goat
    5. Cow
    6. Fish
    7. HighlandCow
    8. Piggy
    9. Duck
    10. Close
    """)

ans = input()

if 'Hedgehog' in ans or '1' in ans:
    print("Please wait while we fetch an Hedgehog image.")
    img_request('Hedgehog')
elif 'Dog' in ans or '2' in ans:
    print("Please wait while we fetch an Dog image.")
    img_request('Dog')
elif 'Cat' in ans or '3' in ans:
    print("Please wait while we fetch an Cat image.")
    img_request('Cat')
elif 'Goat' in ans or '4' in ans:
    print("Please wait while we fetch an Goat image.")
    img_request('Goat')
elif 'Cow' in ans or '5' in ans:
    print("Please wait while we fetch an Cow image.")
    img_request('Cow')
elif 'Fish' in ans or '6' in ans:
    print("Please wait while we fetch an Fish image.")
    img_request('Fish')
elif 'HighlandCow' in ans or '7' in ans:
    print("Please wait while we fetch an HighlandCow image.")
    img_request('Highlandcow')
elif 'Piggy' in ans or '8' in ans:
    print("Please wait while we fetch an Piggy image.")
    img_request('Pig')
elif 'Duck' in ans or '9' in ans:
    print("Please wait while we fetch an Duck image.")
    img_request('Duck')
elif 'Close' in ans or '10' in ans:
    exit()
else:
    print("Error... please try again .-. ")
