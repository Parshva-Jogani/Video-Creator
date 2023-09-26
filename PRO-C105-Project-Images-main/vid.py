import os
import cv2


path = "Images"

image = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        image.append(file_name)

frame = cv2.imread(image[0])
height, width, channels = frame.shape
obj1 = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 5, (width, height))

print(len(image))
count = len(image)


for i in range(0, count-1, 1):
    frame = cv2.imread(image[i])
    obj1.write(frame)

obj1.release()
print('completed')