import cv2
# import os.path as osp
path = "ins.png"
imgMatrix = cv2.imread(path)
pastaresult= "res/"

width = len(imgMatrix)
height = len(imgMatrix[0])

print(width,'+',height)


newpatch = cv2.resize(imgMatrix, (200,200))

cv2.imwrite('outs.png')











