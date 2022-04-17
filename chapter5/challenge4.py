from distutils.log import error


d = {
    "height": 179.5,
    "weight": 60,
    "color": "blue"
}

i = input('>')

try:
    print(d[i])
except:
    print('Did not match')
