import numpy as np
import cv2
import os

def Histogram(img_1):
    imgarray = np.array(img_1)
    HisArray = []
    AimArray = []
    TmpImg = []
    index = imgarray.shape
    for i in range(256):
        HisArray.append(int(0))
        AimArray.append(int(0))
    for x in range(index[0]):
        for y in range(index[1]):
            HisArray[imgarray[x][y]] += 1
            TmpImg.append(int(0))
    LastImg = np.array(TmpImg).reshape(index[0],index[1])
    AllInx = index[0] * index[1]
    for x in range(256):
        for y in range(x):
            AimArray[x] += HisArray[y]
    for i in range(256):
       AimArray[i] = int(AimArray[i] / AllInx * 255)
    for x in range(index[0]):
        for y in range(index[1]):
            tmp = imgarray[x][y]
            LastImg[x][y] = AimArray[tmp]
    cv2.imwrite('aim.png',np.array(LastImg))
    #print(AimArray)
    #print(np.array(AimArray))
                
def main():
    Img_1 = cv2.imread('E:\\Microsoft VS Code\\MyPython\\Demo_1\\sourse.png',2|4)
    Histogram(Img_1)
    #cv2.imshow('asd.png',Img_2)
    #os.system('pause')
    return None

if __name__ == '__main__':
    main()


