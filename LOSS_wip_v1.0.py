import numpy as np
from PIL import Image
import os
import scipy.fftpack
import sympy.discrete as disc
import func_base as fb
import regex_dict as rd
import file_saver as fs
import nu_frag as nf
import re

from func_base import image_dct_2d

# global variables #########
global current_image
global squares
global frag
global loaded
global squares_loaded
############################

def inp_load(x):
    global current_image
    global loaded
    global squares_loaded
    path = x.group(1)
    squares_loaded = False
    try:
        current_image = np.array(Image.open(path).convert('RGB'),dtype=np.float32)
        loaded = True
        return

    except FileNotFoundError:
        print("<< File not found, check path >>")
        loaded = False
        return

def inp_save(x):
    global current_image
    global loaded

    if not loaded:
        print("<< please load an image, \"{name}.bmp\" will be in repo folder >>")
    else:
        w, h, _ = current_image.shape
        path = "repo/"+x.group(1)+".bmp"
        img = Image.fromarray(current_image.astype('uint8'),mode='RGB')
        img.save(path)
        img.close()
        return

def inp_frag(x):
    global loaded
    global squares_loaded
    global frag

    if not loaded:
        print("<< please load an image >>")
    else:
        temp = int(x.group(1))
        if x>0:
            frag = temp
            squares_loaded = False
        else:
            print("<< frag is nonzero >>")

def inp_squares(x):
    global current_image
    global squares
    global loaded
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
    else:
        h, w, _ = current_image.shape
        seed = int(x.group(1))
        squares = nf.nu_frag(h,w,3,seed)
        nf.sq_print(squares,h,w)
        return

def inp_dct(x):
    global current_image

    frag = int(x.group(1))
    current_image = image_dct_2d(current_image,frag)

def single_matcher(s, reg):
    return re.fullmatch(rd.regex_dictionary.get(reg), s)

def case_matcher(s):

    if single_matcher(s, "load") is not None:
        return "load", single_matcher(s, "load")
    if single_matcher(s, "save") is not None:
        return "save", single_matcher(s, "save")
    if single_matcher(s, "frag") is not None:
        return "frag", single_matcher(s, "frag")
    if single_matcher(s, "squares") is not None:
        return "squares", single_matcher(s, "squares")
    if single_matcher(s, "dct") is not None:
        return "dct", single_matcher(s, "dct")

    return "None", None

if __name__ == "__main__":

    loaded = False
    squares_loaded = False
    frag = 8

    while True:

        print("LL:v1.0 >> ", end="")
        s = input()
        if s == "exit":
            break

        r, x  = case_matcher(s)

        if r == "load":
            inp_load(x)
        elif r == "save":
            inp_save(x)
        elif r=="frag":
            inp_frag(x)
        elif r=="squares":
            inp_squares(x)

        else:
            print("<< huh? >>")



    print("<< exit >>")



