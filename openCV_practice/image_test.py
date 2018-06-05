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
def get_closest_color(R, G, B, colors):
    gap_min = 3
    print("="*50)
    #최적의 알고리즘 찾기 - 공간 분할
    for col in colors.values():
        R_ = col["R"] - R
        G_ = col["G"] - G
        B_ = col["B"] - B 
        gap = R_**2+G_**2+B_**2
        if gap < gap_min:
            gap_min = gap
            closest_R = col["R"]
            closest_G = col["G"]
            closest_B = col["B"]
    
    return (closest_R, closest_G, closest_B)

def draw_dots(img_file, colors):
    
    img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
    rows, cols = img.shape[:2]
    unit  = 10
#     print(img.shape)
    
    new_rows = rows-(rows%unit)+unit if rows%unit != 0 else rows
    new_cols = cols-(cols%unit)+unit if cols%unit != 0 else cols
    dst = np.zeros((new_rows, new_cols, 3))
    print(dst.shape)
    
    R = G = B = 1
    for i in range(0, new_rows, unit):
        for j in range(0, new_cols, unit):
            print(dst[i, j, :3])
#             dst[i, j, :3] = get_closest_color(dst[i, j, :3], colors)
            dot = img[i:i+unit, j:j+unit]
    #         print(i, i+unit, j, j+unit)
    #         print(i,j, "="*50)
            
            #평균내서 본격 도트 찍기
            if i < rows:
                B= dot[:unit, :unit, :1].mean()/255
                G= dot[:unit, :unit, 1:2].mean()/255
                R= dot[:unit, :unit, 2:3].mean()/255
#                 print("before :", R, G, B)
                R, G, B = get_closest_color(R, G, B, colors)
#                 print("after :", R, G, B)
#                 
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


    img_file = './test_image2.jpg'
    draw_dots(img_file, colors)