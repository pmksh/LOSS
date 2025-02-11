import numpy as np
from PIL import Image
import func_base as fb
import regex_dict as rd
import file_saver as fs
import nu_frag as nf
import re

from func_base import uf_func

# global variables #########
global current_image
global frag
global squares
global frag_squares
global loaded
global squares_loaded
global frag_loaded
############################

def inp_load(x):
    global current_image
    global loaded
    global squares_loaded
    global frag_loaded
    path = x.group(1)

    try:
        current_image = np.array(Image.open(path).convert('RGB'),dtype=np.float32)
        loaded = True
        frag_loaded = False
        squares_loaded = False
        return

    except FileNotFoundError:
        print("<< File not found, check path >>")
        loaded = False
        return

def inp_save(x):
    global current_image
    global loaded

    if not loaded:
        print("<< please load an image, \"{name}.png\" will be in repo folder >>")
    else:
        w, h, _ = current_image.shape
        path = "repo/"+x.group(1)+".png"
        img = Image.fromarray(current_image.astype('uint8'),mode='RGB')
        img.save(path)
        img.close()
        return

def inp_frag(x):
    global loaded
    global squares_loaded
    global frag
    global frag_squares
    global frag_loaded

    if not loaded:
        print("<< please load an image >>")
        return

    temp = int(x.group(1))
    if temp > 0:
        frag_loaded = True
        if temp != frag:
            squares_loaded = False
        frag = temp
        h, w, _ = current_image.shape
        h = h // frag
        w = w // frag
        frag_squares = []
        for i in range(h):
            for j in range(w):
                frag_squares.append((i,j,1,j+w*i))
    else:
        print("<< frag is nonzero >>")

def inp_squares(x):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    h, w, _ = current_image.shape
    h = h // frag
    w = w // frag
    seed = int(x.group(1))
    squares = nf.nu_frag(h,w,3,seed)
    # nf.sq_print(squares,h,w)   # debug helper
    squares_loaded = True
    return

def inp_fft(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_fft_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_fft_2d)
        return

def inp_ifft(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_ifft_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_ifft_2d)
        return

def inp_dct(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_dct_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_dct_2d)
        return

def inp_idct(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_idct_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_idct_2d)
        return

def inp_dst(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_dst_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_dst_2d)
        return

def inp_idst(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_idst_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_idst_2d)
        return

def inp_wht(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_wht_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_wht_2d)
        return

def inp_iwht(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_iwht_2d)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_iwht_2d)
        return

def inp_block(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, None, fb.func_block_level)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, None, fb.func_block_level)
        return

def inp_sort(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded
    d = x.group(1)

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [d], fb.func_sort)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [d], fb.func_sort)
        return

def inp_quant(x):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return

    q = int(x.group(1))
    if q == 0:
        print("<< quant is nonzero")
        return

    current_image = fb.uf_func(current_image, [q], fb.func_quant)
    return

def inp_quad(x):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return

    current_image = fb.uf_func(current_image, None, fb.func_quad)
    return

def inp_invert(x):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return

    current_image = fb.uf_func(current_image, None, fb.func_invert)
    return

def inp_hash(x):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return

    current_image = fb.uf_func(current_image, None, fb.func_hash)
    return

def inp_flip(x, flag_nu):
    global current_image
    global squares
    global loaded
    global squares_loaded
    global frag
    global squares_loaded

    if not loaded:
        print("<< please load an image >>")
        return
    if not frag_loaded:
        print("<< please choose fragmentation >>")
        return
    if flag_nu:
        if not squares_loaded:
            print("<< please choose squares >>")
            return
        current_image = fb.nuf_func(current_image, squares, frag, [x.group(1)], fb.func_flip)
        return
    if not flag_nu:
        current_image = fb.nuf_func(current_image, frag_squares, frag, [x.group(1)], fb.func_flip)
        return


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

    if single_matcher(s, "fft") is not None:
        return "fft", single_matcher(s, "fft")
    if single_matcher(s, "fft-nu") is not None:
        return "fft-nu", single_matcher(s, "fft-nu")
    if single_matcher(s, "ifft") is not None:
        return "ifft", single_matcher(s, "ifft")
    if single_matcher(s, "ifft-nu") is not None:
        return "ifft-nu", single_matcher(s, "ifft-nu")

    if single_matcher(s, "dct") is not None:
        return "dct", single_matcher(s, "dct")
    if single_matcher(s, "dct-nu") is not None:
        return "dct-nu", single_matcher(s, "dct-nu")
    if single_matcher(s, "idct") is not None:
        return "idct", single_matcher(s, "idct")
    if single_matcher(s, "idct-nu") is not None:
        return "idct-nu", single_matcher(s, "idct-nu")

    if single_matcher(s, "dst") is not None:
        return "dst", single_matcher(s, "dst")
    if single_matcher(s, "dst-nu") is not None:
        return "dst-nu", single_matcher(s, "dst-nu")
    if single_matcher(s, "idst") is not None:
        return "idst", single_matcher(s, "idst")
    if single_matcher(s, "idst-nu") is not None:
        return "idst-nu", single_matcher(s, "idst-nu")


    if single_matcher(s, "wht") is not None:
        return "wht", single_matcher(s, "wht")
    if single_matcher(s, "wht-nu") is not None:
        return "wht-nu", single_matcher(s, "wht-nu")
    if single_matcher(s, "iwht") is not None:
        return "iwht", single_matcher(s, "iwht")
    if single_matcher(s, "iwht-nu") is not None:
        return "iwht-nu", single_matcher(s, "iwht-nu")

    if single_matcher(s, "block") is not None:
        return "block", single_matcher(s, "block")
    if single_matcher(s, "block-nu") is not None:
        return "block-nu", single_matcher(s, "block-nu")

    if single_matcher(s, "sort") is not None:
        return "sort", single_matcher(s, "sort")
    if single_matcher(s, "sort-nu") is not None:
        return "sort-nu", single_matcher(s, "sort-nu")

    if single_matcher(s, "quad") is not None:
        return "quad", single_matcher(s, "quad")
    if single_matcher(s, "quant") is not None:
        return "quant", single_matcher(s, "quant")
    if single_matcher(s, "invert") is not None:
        return "invert", single_matcher(s, "invert")
    if single_matcher(s, "hash") is not None:
        return "hash", single_matcher(s, "hash")

    
    if single_matcher(s, "flip") is not None:
        return "flip", single_matcher(s, "flip")
    if single_matcher(s, "flip-nu") is not None:
        return "flip-nu", single_matcher(s, "flip-nu")
    
    return "None", None

if __name__ == "__main__":

    loaded = False
    squares_loaded = False
    frag_loaded = False
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


        elif r=="fft":
            inp_fft(x, False)
        elif r=="fft-nu":
            inp_fft(x, True)
        elif r=="ifft":
            inp_ifft(x, False)
        elif r=="ifft-nu":
            inp_ifft(x, True)

        elif r=="dct":
            inp_dct(x, False)
        elif r=="dct-nu":
            inp_dct(x, True)
        elif r=="idct":
            inp_idct(x, False)
        elif r=="idct-nu":
            inp_idct(x, True)

        elif r=="dst":
            inp_dst(x, False)
        elif r=="dst-nu":
            inp_dst(x, True)
        elif r=="idst":
            inp_idst(x, False)
        elif r=="idst-nu":
            inp_idst(x, True)

        elif r=="wht":
            inp_wht(x, False)
        elif r=="wht-nu":
            inp_wht(x, True)
        elif r=="iwht":
            inp_iwht(x, False)
        elif r=="iwht-nu":
            inp_iwht(x, True)

        elif r == "block":
            inp_block(x, False)
        elif r == "block-nu":
            inp_block(x, True)

        elif r == "quant":
            inp_quant(x)
        elif r == "quad":
            inp_quad(x)
        elif r == "invert":
            inp_invert(x)
        elif r == "hash":
            inp_hash(x)


        elif r == "sort":
            inp_sort(x, False)
        elif r == "sort-nu":
            inp_sort(x, True)

        elif r == "flip":
            inp_flip(x, False)
        elif r == "flip-nu":
            inp_flip(x, True)

        else:
            print("<< huh? >>")



    print("<< exit >>")



