from image_processing_function import img_processing 
import os

folder_path = 'C:/Users/User/Desktop/multimodal dialogue/drawing/source_images'  # 가져올 파일이 있는 폴더의 경로

file_names = os.listdir(folder_path)

for file_name in file_names:
    img_name, img_no = file_name[:-4].split('_')
    if img_name == 'teddy bear':
        img_processing(img_name, img_no)