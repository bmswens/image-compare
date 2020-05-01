# standard
import os
import copy
import argparse

# third party
from skimage.metrics import structural_similarity
from scipy.ndimage import label
import cv2
import numpy as np


def to_three_channel(img, gray):
    new = np.zeros_like(img)
    new[:, :, 0] = gray
    new[:, :, 1] = gray
    new[:, :, 2] = gray

    return new


def compare(old, new):
    if isinstance(old, str):
        old = cv2.imread(old)
    if isinstance(new, str):
        new = cv2.imread(new)

    old_gray = cv2.cvtColor(old, cv2.COLOR_BGR2GRAY)
    new_gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

    score, difference = structural_similarity(old_gray, new_gray, full=True)
    difference = (difference * 255).astype("uint8")

    return difference


def visualize(base, difference, threshold=200, output=None):
    if isinstance(base, str):
        base = cv2.imread(base)

    gray = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
    out = to_three_channel(base, gray)
    change_grid = copy.deepcopy(gray)

    for x, row in enumerate(difference):
        for y, pixel in enumerate(row):
            if pixel < threshold:
                change_grid[x][y] = 1
                blue = out[x][y][0] - 66
                green = out[x][y][1] - 66
                out[x][y][0] = max(0, blue)
                out[x][y][1] = max(0, green)
            else:
                change_grid[x][y] = 0

    if output:
        cv2.imwrite(output, out)

    return change_grid


def main(f1, f2, output=None):

    for f in [f1, f2]:
        if not os.access(f, os.R_OK):
            raise FileNotFoundError(f"Unable to access {f}")

    difference = compare(f1, f2)
    absolute_difference = visualize(f1, difference, output=output)
    _, n_features = label(absolute_difference,
                          [[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]])
    return n_features


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script for comparing two images.")
    parser.add_argument('file1',
                        type=str,
                        help="Path to first image to be processed, base image for output if used.")
    parser.add_argument('file2',
                        type=str,
                        help="Path to second image.")
    parser.add_argument('--output',
                        dest='output',
                        type=str,
                        default=None,
                        help="Output location for an image which highlights the differences between the two images.")
    kwargs = parser.parse_args()
    features = main(kwargs.file1, kwargs.file2, kwargs.output)
    print(features)
