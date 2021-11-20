import numpy as np
import util


def sample_image_to_array(img: np.ndarray, layers: int, compact: bool):
    side_length = util.side_length_in_bits(layers, compact)

    # gets the rows/columns of reference grid lines, since they need to be excluded
    # during the following sampling of the source image
    if not compact:
        grid_lines = util.reference_grid(side_length)
    else:
        grid_lines = []

    step_x, step_y = img.shape[0] / side_length, img.shape[1] / side_length
    offset_x, offset_y = step_x / 2, step_y / 2

    symbol_size = side_length - len(grid_lines)
    symbol = np.zeros((symbol_size, symbol_size), dtype=str)

    x_sym, y_sym = 0, 0
    lines_without_grid = [i for i in range(side_length) if i not in grid_lines]
    for x in lines_without_grid:
        for y in lines_without_grid:
            x_img, y_img = round(offset_x + x*step_x), round(offset_y + y*step_y)
            symbol[x_sym][y_sym] = '1' if img[x_img][y_img] < 128 else '0'
            y_sym += 1
        y_sym = 0
        x_sym += 1

    return symbol
