from PIL import Image
img = Image.open('ins.jpg')
# img = Image.new( 'RGB', (250,250), "black")
pixels = img.load()
print(img.size[0], 'x', img.size[1])


# mask = [[0, 1, 0],
#         [1, 1, 1],
#         [0, 1, 0]]


mask = [[-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]]


def returnChannel(pixels, x, y, off):
    print(x, y)
    g = 0
    m = 0
    if x > 0:
        g += pixels[x-1, y][off]
        m += mask[1][0]
        if y > 0:
            g += pixels[x-1, y-1][off]
            m += mask[0][0]

        if y < 0:
            g += pixels[x-1, y+1][off]
            m += mask[2][0]

    if x < img.size[0]-1:
        g += pixels[x+1, y][off]
        m += mask[2][1]

        if y > 0:
            g += pixels[x+1, y-1][off]
            m += mask[0][1]

        if y < 0:
            g += pixels[x+1, y+1][off]
            m += mask[3][1]

    if y > 0:
        g += pixels[x, y-1][off]
        m += mask[0][1]

        if x > 0:
            g += pixels[x-1, y-1][off]
        if x < 0:
            g += pixels[x+1, y-1][off]
    if y < img.size[1]-1:
        g += pixels[x, y+1][1]
        if x > 0:
            g += pixels[x-1, y+1][off]
        if x < 0:
            g += pixels[x+1, y+1][off]

        g /= 8
        g = int(g)

        print('return', g)
        return g


for x in range(img.size[0]):
    for y in range(img.size[1]):
        # print (x,y,pixels[x,y])

        # sumMask= (sum(mask[0])+sum(mask[1])+sum(mask[2]))
        # sumMask
        # m = 0
        # off = 1
        # print(pixels[x, y][0])

        # r = returnChannel(pixels, x, y, 0)
        g = returnChannel(pixels, x, y, 1)
        # b = returnChannel(pixels, x, y, 2)
        # print(r, g, b)
        print(g)

        pixels[x, y] = (g, g, g)
        # pixels[x,y]/=4

img.save('outs.bmp')
