import cv2
import numpy
import os
from scipy import ndimage
def randomImage():

    randomByteArray = bytearray(os.urandom(120000))
    flatNumpyArray = numpy.array(randomByteArray)

    grayImage = flatNumpyArray.reshape(300,400)
    cv2.imwrite("RandomGray.png",grayImage)
    bgrImage = flatNumpyArray.reshape(100,400,3)
    cv2.imwrite("RandomColor.png",bgrImage)

def test1():
   
    kernel_3x3 = numpy.array([[-1,-1,-1],
                            [-1,8,-1],
                            [-1,-1,-1]])
    kernel_5x3 = numpy.array([[-1,-1,-1,-1,-1],
                              [-1,1,2,1,-1],
                              [-1,2,4,2,-1],
                              [-1,1,2,1,-1],
                              [-1,-1,-1,-1,-1]])
 
    img = cv2.imread("1.jpg",0)
    k3 = ndimage.convolve(img,kernel_3x3)
    k5 = ndimage.convolve(img,kernel_5x3)
 
    blurred = cv2.GaussianBlur(img,(11,11),0)
    g_hpf = img-blurred
    cv2.imwrite("2.jpg",g_hpf)
    cv2.imshow("3*3",k3)
    cv2.imshow("5*5",k5)
    cv2.imshow("g_hpf",g_hpf)
    cv2.waitKey()
    cv2.destroyroyAllWindows()
 
 
def test2():
    #img = numpy.zeros((200,200),dtype=numpy.uint8)
    #img[50:150,50:150] = 255
    img = cv2.imread("2.jpg",0)
    ret,thresh = cv2.threshold(img,127,255,0)
    image,contours,hierarchy=cv2.findContours(thresh,
                                              cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
 
    img = cv2.drawContours(color,contours,-1,(0,255,0),2)
    cv2.imshow("contours",color)
    cv2.waitKey()
    cv2.destroyAllWindows()
 
def test3():
    img = cv2.imread("1.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,120)
    minLineLength = 20
    maxLineGap = 5
    lines = cv2.HoughLinesP(edges,1,numpy.pi/180,100,minLineLength,
                            maxLineGap)
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imwrite("2.jpg",edges)
    cv2.imshow("edge",edges)
    cv2.imshow("Lines",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def test4():
    img = cv2.imread("1.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = numpy.float32(gray)
    dst = cv2.cornerHarris(gray,2,23,0.04)
    img[dst>0.01 * dst.max()] = [0,0,255]
    cv2.imshow("corners",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def test5():
    img = cv2.imread("1.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints,descriptor = sift.detectAndCompute(gray,None)

    img = cv2.drawKeypoints(image = img,outImage=img,keypoints = keypoints,
                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                            color=(51,163,236))
    cv2.imshow("sift_keypoints",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test5()