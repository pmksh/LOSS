import numpy as np
from PIL import Image
import scipy.fftpack
import sympy.discrete as disc


def func_block_level(block):
    h, w = block.shape
    a = 0
    for x in range(h):
        for y in range(w):
            a += block[x, y]
    a = a / (h * w)
    for x in range(h):
        for y in range(w):
            block[x, y] = a

    return block

def func_dct_2d(block):
    return scipy.fftpack.dct(scipy.fftpack.dct(block.T, norm='ortho').T, norm='ortho')

def func_idct_2d(block):
    return scipy.fftpack.idct(scipy.fftpack.idct(block.T, norm='ortho').T, norm='ortho')

def func_dst_2d(block):
    return scipy.fftpack.dst(scipy.fftpack.dst(block.T, norm='ortho').T, norm='ortho')

def func_idst_2d(block):
    return scipy.fftpack.idst(scipy.fftpack.idst(block.T, norm='ortho').T, norm='ortho')

def nuf_func(img_arr, squares, frag, func):
    altered = np.zeros_like(img_arr)

    for channel in range(3):
        for square in squares:
            x,y,k, _ = square

            x = x * frag
            y = y * frag
            k = k * frag

            block = img_arr[x:x + k, y:y + k, channel]
            altered[x:x + k, y:y + k, channel] = func(block)

    return  altered


### soon to be deprecated

def image_dct_2d(img_arr, frag):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape

    for channel in range(3):
        for i in range(0, height, frag):
            for j in range(0, width, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                block = scipy.fftpack.dct(scipy.fftpack.dct(block.T, norm='ortho').T, norm='ortho')
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def image_idct_2d(img_arr, frag):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height, frag):
            for j in range(0, width, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                block = scipy.fftpack.idct(scipy.fftpack.idct(block.T, norm='ortho').T, norm='ortho')
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def image_wht_2d(img_arr, frag):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height - frag + 1, frag):
            for j in range(0, width - frag + 1, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                block = disc.fwht(np.array(disc.fwht(block.T)).T)
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def image_iwht_2d(img_arr, frag):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height - frag + 1, frag):
            for j in range(0, width - frag + 1, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                block = disc.ifwht(np.array(disc.ifwht(block.T)).T)
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def LL_quantize(img_arr, frag, quant):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height, frag):
            for j in range(0, width, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                block = np.round(block / quant) * quant
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def LL_Block_level(img_arr, frag):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height - frag + 1, frag):
            for j in range(0, width - frag + 1, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                a = 0
                for x in range(frag):
                    for y in range(frag):
                        a += block[x,y]
                a = a / (frag ** 2)
                for x in range(frag):
                    for y in range(frag):
                        block[x, y] = a
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered

def LL_frag_sort(img_arr, frag, dir):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height - frag + 1, frag):
            for j in range(0, width - frag + 1, frag):
                block = img_arr[i:i + frag, j:j + frag, channel]
                a = 0
                for x in range(frag):
                    if(dir == "L"):
                        temp = block[x,:]
                        block[x,:] = sorted(temp)
                    if(dir == "R"):
                        temp = block[x,:]
                        block[x,:] = sorted(temp)[::-1]
                    if(dir == "U"):
                        temp = block[:,x]
                        block[:,x] = sorted(temp)
                    if (dir == "D"):
                        temp = block[:, x]
                        block[:, x] = sorted(temp)[::-1]
                altered[i:i + frag, j:j + frag, channel] = (block)
    return altered
