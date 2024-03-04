import cv2
import os

def img_processing(img_name, img_no):
    image = cv2.imread("source_images/"+img_name+"_"+img_no+".jpg",cv2.IMREAD_COLOR)

    rows = 3
    cols = 2

    height, width, _ = image.shape

    small_images = []
    for r in range(rows):
        for c in range(cols):
            start_row = int(r * height / rows)
            end_row = int((r + 1) * height / rows)
            start_col = int(c * width / cols)
            end_col = int((c + 1) * width / cols)
            small_images.append(image[start_row:end_row, start_col:end_col])

    output_dir = 'output_images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, small_image in enumerate(small_images[:-1]):
        small_image_resized = cv2.resize(small_image, (512, 512))
        cv2.imshow(f'OutputImage {i}', small_image_resized)
        cv2.imwrite(f'{output_dir}/{img_name}_hyeon_{i+(int(img_no)-1)*5}.png', small_image_resized)

    cv2.destroyAllWindows()