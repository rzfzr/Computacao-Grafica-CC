from PIL import Image


import os

img = Image.open('ins.jpg')
# img = Image.new( 'RGB', (250,250), "black")
pixels = img.load()
print(img.size[0], 'x', img.size[1])


for x in range(img.size[0]):
    for y in range(img.size[1]):
        # print(x, y, pixels[x, y])
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]

        avg = int((r+g+b)/3)

        pixels[x, y] = (avg, avg, avg)
        # pixels[x,y]/=4

img.save('outs.bmp')
