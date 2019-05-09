from PIL import Image


import os

img = Image.open('ins.jpg')
# img = Image.new( 'RGB', (250,250), "black")
pixels = img.load()
print(img.size[0], 'x', img.size[1])

# ycbcr abaixo
# HSI foi feito em sala no usuario temporario, lembro de ter mostrado e comentado sobre
for x in range(img.size[0]):
    for y in range(img.size[1]):
        # print(x, y, pixels[x, y])
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]

        y = r*0.2568 + g*0.5041 + b*0.0979 + 16
        cb = -r*0.1482 - g*0.2910 + b*0.4392 + 128
        cr = r*0.4392 - g*0.3678 - b*0.0714 + 128

        pixels[x, y] = (int(y), int(cb), int(cr))
        # pixels[x,y]/=4

img.save('outs.bmp')
