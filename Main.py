import cv2
from getCellVal import *

grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
max_images = input('how many images you want to test(max. 7) : ')
for k in range(1,max_images+1):
    grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
    path = 'imagesets/task1_img_' + str(k) +'.jpg'
    img_rgb = cv2.imread(path)
    grid_map = detectCellVal(img_rgb,grid_map)

    for i in range(0,6):
        x,y=(550,50*(2*i+1))
        if(not(abs(grid_map[i][5])==grid_map[i][5])):
                cv2.putText(img_rgb, str(grid_map[i][5]), (x-m/2, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
        elif(not(int(grid_map[i][5]/10)==0)):
                cv2.putText(img_rgb, str(grid_map[i][5]), (x-m/2, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
        else:
                cv2.putText(img_rgb, str(grid_map[i][5]) , (x-m/4, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)

    cv2.imshow('Image ' + str(k),img_rgb)
    cv2.waitKey()
