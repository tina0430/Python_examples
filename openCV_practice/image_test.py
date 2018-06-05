import cv2
import numpy as np
import json
import math

#http://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html#id2
#TODO - 샤프하게
def get_clost_color(R, G, B, colors):
    dist_min = 2
    for col in colors.values():
        R_ = col["R"]
        G_ = col["G"]
        B_ = col["B"]
        dist = math((R-R_)**2+(G-G_)**2+(B-B_)**2)
        if dist < dist_min:
            dist_min = dist
            close_R = R_
            close_G = G_
            close_B = B_
    
def draw_dots(img_file, colors):
    
    img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
    rows, cols = img.shape[:2]
    unit  = 10
    print(img.shape)
    
    new_rows = rows-(rows%unit)+unit if rows%unit != 0 else rows
    new_cols = cols-(cols%unit)+unit if cols%unit != 0 else cols
    dst = np.zeros((new_rows, new_cols, 3))
    print(dst.shape)
    
    R = G = B = 1
    for i in range(0, new_rows, unit):
        for j in range(0, new_cols, unit):
            dot = img[i:i+unit, j:j+unit]
    #         print(i, i+unit, j, j+unit)
    #         print(i,j, "="*50)
            if i < rows:
                B= dot[:unit, :unit, :1].mean()/255
                G= dot[:unit, :unit, 1:2].mean()/255
                R= dot[:unit, :unit, 2:3].mean()/255
                
                
            dst[i:i+unit, j:j+unit, :1] = B
            dst[i:i+unit, j:j+unit, 1:2] = G
            dst[i:i+unit, j:j+unit, 2:3] = R
            
    #         print(dot[:unit, :unit, :1].mean(), dot[:unit, :unit, 1:2].mean(), dot[:unit, :unit, 2:3].mean())
    #         print(dst[i:i+unit, j:j+unit, 0:1], dst[i:i+unit, j:j+unit, 1:2], dst[i:i+unit, j:j+unit, 2:3])
    
    cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_file = './colors.json'
    colors = {}
    
    with open(color_file, 'r') as f:
        colors = json.load(f)


    img_file = './test_image2.png'
    draw_dots(img_file, colors)