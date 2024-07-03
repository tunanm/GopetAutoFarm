import cv2
import numpy as np


def map_object_detect(pathResources, pathImagesRealTime):
    avatar = cv2.imread(pathResources)
    sample = cv2.imread(pathImagesRealTime)

    result = cv2.matchTemplate(avatar, sample, cv2.TM_CCOEFF_NORMED)

    width = avatar.shape[1]
    height = avatar.shape[0]
    threshold = 0.6
    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([x, y, width, height])

    # Convert rectangles to numpy array
    rectangles = np.array(rectangles)

    # Non-maximum suppression
    nms_rectangles = cv2.groupRectangles(rectangles.tolist(), groupThreshold=1, eps=0.2)[0]

    array_result = []
    for (x, y, w, h) in nms_rectangles:
        center_bottom_x = x + w // 2
        center_bottom_y = y + h
        array_result.append((center_bottom_x, center_bottom_y, w, h))  # Append center of the rectangle
        cv2.rectangle(sample, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imwrite(pathImagesRealTime, sample)

    return array_result
