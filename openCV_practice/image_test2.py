import cv2
import numpy as np
import json

#http://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html#id2


#https://techne301.wordpress.com/mtt2/codes/project-22/project22_colortracking_with_opencv/
#비슷한 색 찾기 

#https://docs.opencv.org/2.4/modules/core/doc/basic_structures.html
#opencv tutorial

#TODO
#contrast 증가 -> 테두리 두껍게 -> color filtering -> dot -> color filtering
 
def get_closest_color(col, colors):
    col = col/255
    colors_ = colors - col
    
    if np.zeros((1,3)) in colors_:
        return col
    
    colors_ = np.power(colors_, 2)
    
    min_dist = 4
    min_index = 0
    
    for i in range(len(colors)):
        dist = np.sum(colors_[i, :3])
        if dist < min_dist:
            min_dist = dist
            min_index = i 

    return colors[min_index, :3]

def draw_dots(img_file, colors):
    
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)
    rows, cols = img.shape[:2]
    unit  = 10
    new_rows = rows-(rows%unit)+unit if rows%unit != 0 else rows
    new_cols = cols-(cols%unit)+unit if cols%unit != 0 else cols
    print(img.shape) 
    dst = np.zeros((new_rows, new_cols, 3))
    
    for i in range(rows):
        for j in range(cols):
            dst[i,j] = get_closest_color(img[i, j], colors)
            
    print(img)
    

#     print(dst[:, :] = get_closest_color_(img[]))
#     img[i, j, 0:3]
     
#     for i in range(rows+1):
        
#         img[i , :3] = get_closest_color(img[i, :3], colors)
            
    cv2.imshow('original', img)
    cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    color_file = './colors.csv'
    colors = {}
    
    with open(color_file, 'r') as f:
        colors = np.genfromtxt(color_file, delimiter=',')
        colors = colors[1:, 1:]

    img_file = './test_image.png'
    draw_dots(img_file, colors)
    