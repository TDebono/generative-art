import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
import math
import matplotlib.pyplot as plt

def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

def interpolate_color(start_col, end_col, factor: float):
    recip = 1 - factor

    return (int(start_col[0] * recip + end_col[0] * factor),
            int(start_col[1] * recip + end_col[1] * factor),
            int(start_col[2] * recip + end_col[2] * factor))

def generate_art():
    start_col = random_color()
    end_col = random_color()
    target_size_px = 256
    scale_factor = 2
    size_px = (target_size_px * scale_factor, 
               target_size_px * scale_factor)
    background_col = (0, 0, 0)
    padding_px = 12 * scale_factor
    image = Image.new("RGB", size_px, background_col)
    
    draw = ImageDraw.Draw(image)

    points = []

    for _ in range(10):
        random_point = (
            random.randint(padding_px, size_px[0] - padding_px),
            random.randint(padding_px, size_px[0] - padding_px)
        )

        points.append(random_point)

    thickness = 0
    for i, point in enumerate(points):

        overlay_image = Image.new("RGB", size_px, background_col)
        overlay_draw = ImageDraw.Draw(image)

        p1 = point

        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1, p2)
        col_fact = i / (len(points) - 1)
        line_col = interpolate_color(start_col, end_col, col_fact)
        thickness += 1 * scale_factor
        overlay_draw.line(line_xy, fill=line_col, width=thickness)
        image = ImageChops.add(image, overlay_image)
    
    image = image.resize((target_size_px,
                          target_size_px),
                          resample=Image.ANTIALIAS)
    display(image)