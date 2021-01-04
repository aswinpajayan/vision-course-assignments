#!/usr/bin/env python3

import os
import cv2

if __name__ == "__main__":
    for file_name in os.listdir('./in2'):
        # print(os.path.join('./in2', file_name))

    
        img = cv2.imread(os.path.join('./in2', file_name), cv2.IMREAD_GRAYSCALE)

        _, mask = cv2.threshold(img, 0, 1, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (5, 5))

        dilated_mask = cv2.dilate(mask, kernel, iterations=1)

        final_image = img * dilated_mask + (1 - dilated_mask) * 255

        cv2.imwrite(os.path.join('./out/', file_name), final_image)
