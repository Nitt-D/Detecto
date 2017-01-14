# -*- coding: utf-8 -*-
# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)

import cv2
import numpy as np

def detectCellVal(img_rgb,grid_map):
## FETCHING DATA AND COMPARING        
        ctr=-1        
        for j in range(0,12):
                img_rgb2=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
                ctr=ctr+1
                
                if(ctr<=9):
                        imgpath='digits/'+str(j) +'.jpg'
                elif(ctr==10):
                        imgpath='digits/minus.jpg'
                elif(ctr==11):
                        imgpath='digits/plus.jpg'

                check2=cv2.imread(imgpath)
                check=cv2.cvtColor(check2,cv2.COLOR_BGR2GRAY)
                del check2
                res = cv2.matchTemplate(img_rgb2,check,cv2.TM_CCOEFF_NORMED)
                del img_rgb2
## THRESHOLDING
                if(ctr==7 or ctr==1 ):
                        thresh = 0.55
                elif(ctr==10):
                        thresh=0.53
                else :
                        thresh=0.63
                loc = np.where(res>thresh)

## WRITING ON GRID_MAP
                for k in range(0,len(loc[0])):
                        a=loc[0][k]/100
                        b=loc[1][k]/100
                        if(ctr<=9):
                                grid_map[a][b]=j
                        elif(ctr==10):
                                grid_map[a][b]='-'
                        elif(ctr==11):
                                grid_map[a][b]='+'

## EXPRESSION EVALUATION
        for i in range(0,6):

                s=0;

                if ((grid_map[i][1]=='+')&(grid_map[i][3]=='+')):
                        s+= (grid_map[i][0]) +  (grid_map[i][2]) +  (grid_map[i][4]);
                elif ((grid_map[i][1]=='-')&(grid_map[i][3]=='-')):
                        s+= (grid_map[i][0]) -  (grid_map[i][2]) -  (grid_map[i][4]);

                elif ((grid_map[i][1]=='+')&(grid_map[i][3]=='-')):
                        s+= (grid_map[i][0]) +  (grid_map[i][2]) -  (grid_map[i][4]);

                elif ((grid_map[i][1]=='-')&(grid_map[i][3]=='+')):
                        s+= (grid_map[i][0]) -  (grid_map[i][2]) +  (grid_map[i][4]);  
                grid_map[i][5]=s

                
        return grid_map
