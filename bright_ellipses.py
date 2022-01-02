import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
import math
import matplotlib.pyplot as plt

def get_ellipse_shape(scale_factor):
    coords = [(random.randint(30, 100) * scale_factor,
             random.randint(30, 100) * scale_factor),
             (random.randint(100, 256) * scale_factor,
             random.randint(100, 256) * scale_factor)]

    return coords

def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

def generate_art2():
    target_size_px = 256
    scale_factor = 2
    size_px = target_size_px * scale_factor
    background_col = (0, 0, 0)
    image = Image.new("RGB", (size_px, size_px), background_col)
    
    draw = ImageDraw.Draw(image)

    shapes = []

    for _ in range(10):
        shape = get_ellipse_shape(scale_factor=scale_factor)
        shapes.append(shape)
    
    width = 1
    for i, s in enumerate(shapes):
        overlay_image = Image.new("RGB", (size_px, size_px), background_col)
        overlay_draw = ImageDraw.Draw(image)

        outline_col = random_color()

        overlay_draw.ellipse(s, fill=None, outline=outline_col, width=width)
        image = ImageChops.add(image, overlay_image)
        width += 1
    
    # shape = get_ellipse_shape()
    # draw.ellipse(shape, fill=None, outline='white')

    image = image.resize((target_size_px,
                          target_size_px),
                          resample=Image.ANTIALIAS)

    display(image)