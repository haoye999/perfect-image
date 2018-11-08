import numpy as np
import cv2
# import circle

def goalimage(filename):
	img = cv2.imread(filename)
	#识别前景物体

	img2 = img.copy()                               # a copy of original image
	mask = np.zeros(img2.shape[:2],dtype = np.uint8) # mask initialized to PR_BG
	output = np.zeros(img2.shape,np.uint8)           # output image to be shown
	# 然后创建以0填充的前景和背景模型：
	bgdModel = np.zeros((1, 65), np.float64)
	fgdModel = np.zeros((1, 65), np.float64)
	rect = (100, 100, 300, 300)
	#rect = (img2.shape[0]//2-100, img2.shape[1]//2-100 , 200, 200)
	cv2.grabCut(img2, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
	mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
	output = cv2.bitwise_and(img2,img2,mask=mask2)
	bar = np.zeros((img2.shape[0],5,3),np.uint8)
	fgres = np.hstack((bar,output))
	return fgres
	cv2.imwrite('output.jpg',fgres)
	# cv2.imshow('thr',fgres)

	#切割前景图片
def cropimage(image):
	#变换前景为灰度图
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#高斯去噪声
	blurred = cv2.GaussianBlur(gray, (9, 9),0) 

	gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
	gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)

	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)

	blurred = cv2.GaussianBlur(gradient, (9, 9),0)
	(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (200, 200))
	closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

	closed = cv2.erode(closed, None, iterations=4)
	closed = cv2.dilate(closed, None, iterations=4)

	(_, cnts, _) = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

	# compute the rotated bounding box of the largest contour
	rect = cv2.minAreaRect(c)
	box = np.int0(cv2.boxPoints(rect))

	# draw a bounding box arounded the detected barcode and display the image
	draw_img = cv2.drawContours(image.copy(), [box], -1, (0, 0, 255), 3)

	Xs = [i[0] for i in box]
	Ys = [i[1] for i in box]
	x1 = min(Xs)
	x2 = max(Xs)
	y1 = min(Ys)
	y2 = max(Ys)
	hight = y2 - y1
	width = x2 - x1
	crop_img= image[y1:y1+hight, x1:x1+width]
	return crop_img
	# cv2.imshow('thresh', crop_img)

def addimage(crop_img,backname,dx,dy,size=1):

	#图像融合
	rows,cols,channels=crop_img.shape
	back=cv2.imread(backname)
	# face=cv2.imread('su_haoye.jpg')
	# print(face.shape)
	# rows,cols,channels=face.shape
	# roi=back[dx:dx+cols,dy:dy+rows]
	roi=back[dx:dx+rows,dy:dy+cols]
	# print(rows, cols)
	for i in range(rows):
	    for j in range(cols):
	        if (crop_img[i,j][0]+crop_img[i,j][1]+crop_img[i,j][2])<=3:
	        	roi[i,j]=roi[i,j]
	        else:
	        	roi[i,j][0]=int(crop_img[i,j][0]*size)+int(roi[i,j][0]*(1-size))
	        	roi[i,j][1]=int(crop_img[i,j][1]*size)+int(roi[i,j][1]*(1-size))
	        	roi[i,j][2]=int(crop_img[i,j][2]*size)+int(roi[i,j][2]*(1-size))
	back[dx:dx+rows,dy:dy+cols]=roi
	        # if i>=227: break
	        # if (face[i,j][0]+face[i,j][1]+face[i,j][2])<=30:
	        # 	roi[i,j]=roi[i,j]
	        # else:
        	# roi[i,j]=face[i,j]
	        # print(i,j)
	# back[dx:dx+rows,dy:dy+cols]=roi


	#泊松无缝融合        
	# imgnext=cv2.imread('backgoal_output.jpg')
	# imgnext = cv2.resize(imgnext,(rows,cols),cv2.INTER_LINEAR)
	# imgnextmask = 255 * np.ones(imgnext.shape,imgnext.dtype)
	# width, height, channels = back.shape
	# center = ( dy+cols//2,dx+rows//2)
	# mixed_clone = cv2.seamlessClone(imgnext, back, imgnextmask, center, cv2.MIXED_CLONE)

	#加权融合
	# crop_img=cv2.imread('backgoal_output.jpg')
	# cv2.imshow("loglfghfdg",crop_img)
	# cv2.imshow("loglfghfdg",crop_img)
	# crop_img = cv2.resize(crop_img,(rows,cols),cv2.INTER_LINEAR)
	# print(rows, cols)
	# for j in range(rows):
	#     for i in range(cols):
	#         if (crop_img[i,j][0]+crop_img[i,j][1]+crop_img[i,j][2])<=0:
	#         	roi[i,j]=roi[i,j]
	#         else:
	#         	roi[i,j][0]=int(crop_img[i,j][0]*0.7)+int(roi[i,j][0]*0.3)
	#         	roi[i,j][1]=int(crop_img[i,j][1]*0.7)+int(roi[i,j][1]*0.3)
	#         	roi[i,j][2]=int(crop_img[i,j][2]*0.7)+int(roi[i,j][2]*0.3)
	# cv2.imshow("loglfghfdg",crop_img)
	# back[dx:dx+cols,dy:dy+rows]=roi
	# cv2.imshow("logo",back)

	# cv2.imwrite('face2.jpg',roi)
	cv2.waitKey(20179)
	return back, roi

def addface(face,crop_img,backname,dx,dy):
    #脸部加权融合
	rows,cols,channels=crop_img.shape
	back=cv2.imread(backname)

	a=face.copy()
	roi=back[dx:dx+rows,dy:dy+cols]
	for i in range(rows):
	    for j in range(cols):
	        if (face[i,j][0]+face[i,j][1]+face[i,j][2])>=3:
	            a[i,j][0]=1
	        else: a[i,j][0]=0
	cv2.imshow("loglfghfdg",roi)
	print(rows, cols)
	for i in range(rows):
	    for j in range(cols):
	        if a[i,j][0]==0:
	        	roi[i,j]=roi[i,j]
	        if a[i,j][0]==1:
	        	roi[i,j][0]=int(crop_img[i,j][0]*1)+int(roi[i,j][0]*0)
	        	roi[i,j][1]=int(crop_img[i,j][1]*1)+int(roi[i,j][1]*0)
	        	roi[i,j][2]=int(crop_img[i,j][2]*1)+int(roi[i,j][2]*0 )
	back[dx:dx+rows,dy:dy+cols]=roi


	

	cv2.imshow("logo",back)

	cv2.imwrite('backgoal6.jpg',back)
	cv2.imwrite('face2.jpg',roi)
	cv2.waitKey(20179)
	return back

# name='hand.jpg'
# img=cv2.imread(name)
# img=test2.getcutimage(name)
# # # img=goalimage(name)
# cv2.imshow("01",img)


# img=cv2.imread('output.jpg')
# img=cropimage(img)
# cv2.imshow("02",img)
# cv2.imwrite('face.jpg',img)

# face=cv2.imread('face.jpg')
# rows,cols,channels=face.shape
# # img=cv2.imread('face2_output.jpg')
# # bigimg = cv2.resize(face,(int(cols*1.55),int(rows*1.55)),cv2.INTER_LINEAR)
# bigimg = cv2.resize(face,(int(cols*1.4),int(rows*1.4)),cv2.INTER_LINEAR)



# img = addimage(bigimg,"night.jpg",140,100,1)


# #dx 图片下调，dy左调

# #普京参数
# # img = addimage(bigimg,"wave.jpg",140,40,1)

# # cv2.imshow("02",img)
# # face=cv2.imread('face.jpg')
# # image=addface(face,img,"wave.jpg",100,200)

# # # source = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# # #均值滤波

# # result = cv2.medianBlur(image, 3)

# #star
# # img=circle.circle(name)
# cv2.imshow("01",img)
# # img=cropimage(img)
# # cv2.imshow("02",img)
# # rows,cols,channels=img.shape
# # bigimg = cv2.resize(img,(int(cols*0.3),int(rows*0.3)),cv2.INTER_LINEAR)
# # img = addimage(bigimg,"hand.jpg",30,430,1)

# cv2.imwrite('night.jpg',img)
# cv2.waitKey(10179)