<div align="center"><img src="https://github.com/nelson123-lab/warp_perspective/blob/daa65d0145f52e5d6a737edd0b97d2407cdf280d/Wrap_perspective_output.png" width="900"/></div>

# Wrap perspective

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=255)](https://www.linkedin.com/in/nelsonjoseph123/)
[![Youtube](https://img.shields.io/badge/-Youtube-black.svg?style=flat-square&logo=Youtube&colorB=900)](https://www.youtube.com/channel/UCj-j1k_3vC6F1rVgrEhDF7g)
[![Medium](https://img.shields.io/badge/-Medium-black.svg?style=flat-square&logo=Medium&colorB=000)](https://medium.com/me/stories/public)

The program allows one to warp the image you require from the original image.
The coordinates of the image can be found out by uploading the image in  the paint and you can use the mouse pointer to find the cooridnates at the bottom left. Copy and paste the coordinates in the program to get the wrap output of your image.

# Program for the wrap perspective

```python

import cv2
import numpy as np

dire = r"C:\Users\NELSON JOSEPH\Desktop"
path = dire +'/'+ "note_book.jpeg" # image which is to be taken for wrapperspective
img = cv2.imread(path)
save = dire+"/"+ "note_book1.jpeg" # Output name of the image.

width,height = 210,297 # Dimensions of an A4 paper.
pts1 = np.float32([[123,250],[500,240],[559,717],[24,720]])# Coordinates of the points to take wrap perspective.
"""
Future Goal:- Implement a model that can could get you the 4 coordinates 
so that we don't need to manually find the coordinates. Example such a model works in 
camscanner i Guess.
"""
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))
cv2.imwrite(save, output) # used to save the output.


cv2.imshow("image", img) # To view the image used
cv2.imshow("output",output) # To view the output image generated.
cv2.waitKey(0)
```

# Wrapped output from the original image.

<div align="center"><img src="https://github.com/nelson123-lab/warp_perspective/blob/66f7f5c077874c3b4c9318f43b32b4872a817699/note_book1.jpeg" width="500"/></div>

# Project extended in making an app for getting wrap perspective from an image.
