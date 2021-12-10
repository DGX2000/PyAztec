import cv2.cv2 as cv2
import numpy as np


def find_contained_squares(squares):
    contained_squares = []

    for square in squares:
        square_list = [square]

        for other_square in squares:
            if square is not other_square:
                reject = False

                for point in other_square:
                    if cv2.pointPolygonTest(square, (float(point[0]), float(point[1])), False) != 1:
                        reject = True
                        break

                if not reject:
                    square_list.append(other_square)

        if len(square_list) > 1:
            contained_squares.append(square_list)

    return contained_squares


def find_nested_squares(contained_squares, levels: int):
    candidates = [square for square in contained_squares if len(square) == levels+1]

    nested_squares = []
    for candidate in candidates:
        is_nesting = True
        for i in range(1, len(candidate)-1):
            matching_squares = [1 for square in contained_squares if (square[0] == candidate[i]).all()]
            if len(matching_squares) == 0:
                is_nesting = False
                break
        if is_nesting:
            nested_squares.append(candidate)
    return nested_squares


image = cv2.imread('Aztec1.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rectangles = [cv2.minAreaRect(contour) for contour in contours]
boxes = [np.int0(cv2.boxPoints(rect)) for rect in rectangles]

contained_squares = find_contained_squares(boxes)
compact_centers = find_nested_squares(contained_squares, 3)
# full_centers = find_nested_squares(contained_squares, 5)

# TODO: Get pixel dimensions (compact = 7x7, full = 11x11)
outer_square = compact_centers[0][0]
side_length_1 = round(np.sqrt(np.sum(np.square(outer_square[1] - outer_square[0]))))
side_length_2 = round(np.sqrt(np.sum(np.square(outer_square[2] - outer_square[1]))))

if abs(outer_square[1][0] - outer_square[0][0]) > abs(outer_square[1][1] - outer_square[0][1]):
    side_length_x = side_length_1
    side_length_y = side_length_2
else:
    side_length_x = side_length_2
    side_length_y = side_length_1

bit_width = side_length_x / 7.0
bit_height = side_length_y / 7.0

mode_boundary = outer_square
mode_boundary[0][0] -= int(2*bit_width)
mode_boundary[0][1] += int(2*bit_height)

mode_boundary[1][0] -= int(2*bit_width)
mode_boundary[1][1] -= int(2*bit_height)

mode_boundary[2][0] += int(2*bit_width)
mode_boundary[2][1] -= int(2*bit_height)

mode_boundary[3][0] += int(2*bit_width)
mode_boundary[3][1] += int(2*bit_height)

cv2.drawContours(image, [mode_boundary], -1, (0, 0, 255), 2)
# cv2.drawContours(image, full_centers[0], -1, (255, 0, 0), 2)

cv2.imshow('Bullseye Detection', image)
cv2.waitKey()
