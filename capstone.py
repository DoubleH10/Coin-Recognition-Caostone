import numpy as np
import cv2

def radius(circles):
    radii =[]
    for i in circles[0,:]:
        radii.append(i[2])
    return radii

def brightness(image, circles, size):
    bright = []
    for i in circles[0,:]:
        values = np.mean(image[i[1]-size:i[1]+size, i[0]-size:i[0]+size])
        bright.append(values)
    return bright



img_gray = cv2.imread('/Users/hadihijazi/OneDrive - Universitat Ramón Llull/Martial Arts/CS50/untitled folder/365 Data Science/python-programmer-bootcamp/19. Capstone/19.1 capstone_coins.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('/Users/hadihijazi/OneDrive - Universitat Ramón Llull/Martial Arts/CS50/untitled folder/365 Data Science/python-programmer-bootcamp/19. Capstone/19.1 capstone_coins.png', 1)
img_gray = cv2.GaussianBlur(img_gray,  (5,5), 0)



circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT,1,120,
                            param1=50,param2=27,minRadius=60,maxRadius=120)

circles = np.uint16(np.around(circles))


for i in circles[0,:]:
    cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)
    cv2.circle(img, (i[0],i[1]), 2, (0, 0, 255), 0) 



r = radius(circles)
b = brightness(img, circles, 20)

c =[]
for i in range(len(circles[0,:])):
    if (r[i]<=90) and (b[i]<=130): 
        c.append(1)
        cv2.putText(img, '1p', (circles[0,i][0],circles[0,i][1]), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)
    
    elif (r[i]>=90) and (b[i]<=130):  
        c.append(2)
        cv2.putText(img, '2p', (circles[0,i][0],circles[0,i][1]), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)
    
    elif (r[i]<=90) and (b[i]>=130):   
        c.append(5)
        cv2.putText(img, '5p', (circles[0,i][0],circles[0,i][1]), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)
    
    elif (r[i]>=90) and (b[i]>=130):
        c.append(10)
        cv2.putText(img, '10p', (circles[0,i][0],circles[0,i][1]), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)


cv2.putText(img, f'Total Estimated Value: {sum(c)} p', (1,50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,0), 2)

cv2.imshow('Detected Coins', img)
cv2.waitKey(0)
cv2.destroyAllWindows()