
# read data.txt and return the image, top, left, boxWidth, boxHeight
def get_image():
    with open('image.txt', 'r') as file:
        data = file.readlines()
    return data[0]

def get_top():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    return data[0]

def get_left():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    return data[1]

def get_boxWidth():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    return data[2]

def get_boxHeight():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    return data[3]

def write_image(image):
    with open('image.txt', 'w') as file:
        file.write(image + "\n")

def write_coordinates(top, left, boxWidth, boxHeight):
    with open('data.txt', 'w') as file:
        file.write(str(top) + "\n")
        file.write(str(left) + "\n")
        file.write(str(boxWidth) + "\n")
        file.write(str(boxHeight) + "\n")
