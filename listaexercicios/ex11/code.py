from PIL import Image
img = Image.open('ins.jpg')
# img = Image.new( 'RGB', (250,250), "black")
pixels = img.load()
print(img.size[0], 'x', img.size[1])


# def apply4(pixels, color):
#     r = 0
#     offset = 0
#     if color == g:
#             offset = 1
#     if color == b:
#             offset = 2

#         if x > 0:
#             c += pixels[x-1, y][offset]
#         if x < img.size[0]-1:
#             c += pixels[x+1,y][offset]
#         if y > 0:
#             c += pixels[x,y-1][offset]
#         if y < img.size[1]-1:
#             c += pixels[x,y+1][offset]

#         return int(r/4)


for x in range(img.size[0]):
    for y in range(img.size[1]):
        print(x, y, pixels[x, y])
        r = 0
        if x > 0:
            r += pixels[x-1, y][1]
        if x < img.size[0]-1:
            r += pixels[x+1, y][1]
        if y > 0:
            r += pixels[x, y-1][1]
        if y < img.size[1]-1:
            r += pixels[x, y+1][1]
        r /= 4
        r = int(r)
        g = 0
        if x > 0:
            g += pixels[x-1, y][1]
        if x < img.size[0]-1:
            g += pixels[x+1, y][1]
        if y > 0:
            g += pixels[x, y-1][1]
        if y < img.size[1]-1:
            g += pixels[x, y+1][1]
        g /= 4
        g = int(g)
        b = 0
        if x > 0:
            b += pixels[x-1, y][2]
        if x < img.size[0]-1:
            b += pixels[x+1, y][2]
        if y > 0:
            b += pixels[x, y-1][2]
        if y < img.size[1]-1:
            b += pixels[x, y+1][2]
        b /= 4
        b = int(b)
        pixels[x, y] = (r, g, b)

        # pixels[x,y]/=4
img.save('outs.bmp')
