import numpy as np
from PIL import Image
import scipy.fftpack as fftp
import sympy.discrete as disc

def func_flip(block, params):
    x = params[0]
    h, w = block.shape
    copy = np.zeros_like(block)

    if x == "V":
        for i in range(h):
            for j in range(w):
                copy[i,j] = block[h-i-1,j]
    if x == "H":
        for i in range(h):
            for j in range(w):
                copy[i,j] = block[i,w-j-1]
    if x == "T":
        copy = block.T
    

    return copy
    
def func_fft_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.rfft(block))
    if x == "H":
        return np.array(fftp.rfft(block.T)).T
    if x == "T":
        return fftp.rfft(fftp.rfft(block.T).T)

def func_ifft_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.irfft(block))
    if x == "H":
        return np.array(fftp.irfft(block.T)).T
    if x == "T":
        return fftp.irfft(fftp.irfft(block.T).T)

def func_block_level(block, params):
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

def func_dct_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.dct(block, norm='ortho'))
    if x == "H":
        return np.array(fftp.dct(block.T, norm='ortho')).T
    if x == "T":
        return fftp.dct(fftp.dct(block.T, norm='ortho').T, norm='ortho')

def func_idct_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.idct(block, norm='ortho'))
    if x == "H":
        return np.array(fftp.idct(block.T, norm='ortho')).T
    if x == "T":
        return fftp.idct(fftp.idct(block.T, norm='ortho').T, norm='ortho')

def func_dst_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.dst(block, norm='ortho'))
    if x == "H":
        return np.array(fftp.dst(block.T, norm='ortho')).T
    if x == "T":
        return fftp.dst(fftp.dst(block.T, norm='ortho').T, norm='ortho')

def func_idst_2d(block, params):
    x = params[0]
    if x == "V":
        return np.array(fftp.idst(block, norm='ortho'))
    if x == "H":
        return np.array(fftp.idst(block.T, norm='ortho')).T
    if x == "T":
        return fftp.idst(fftp.idst(block.T, norm='ortho').T, norm='ortho')

def func_wht_2d(block, params):
    h,w = block.shape
    x = params[0]
    if x == "V":
        for i in range(h):
            temp = block[i,]
            temp = disc.fwht(temp)
            block[i,] = temp [0:w]
    if x == "H":
        for j in range(w):
            temp = block[:,j]
            temp = disc.fwht(temp)
            block[:,j] = temp [0:h]
    if x == "T":
        for i in range(h):
            temp = block[i,]
            temp = disc.fwht(temp)
            block[i,] = temp [0:w]
        for j in range(w):
            temp = block[:,j]
            temp = disc.fwht(temp)
            block[:,j] = temp [0:h]
    return block

def func_iwht_2d(block, params):
    h,w = block.shape
    x = params[0]
    if x == "V":
        for i in range(h):
            temp = block[i,]
            temp = disc.ifwht(temp)
            block[i,] = temp [0:w]
    if x == "H":
        for j in range(w):
            temp = block[:,j]
            temp = disc.ifwht(temp)
            block[:,j] = temp [0:h]
    if x == "T":
        for j in range(w):
            temp = block[:,j]
            temp = disc.ifwht(temp)
            block[:,j] = temp [0:h]
        for i in range(h):
            temp = block[i,]
            temp = disc.ifwht(temp)
            block[i,] = temp [0:w]
    return block

def func_sort(block, params):
    dir = params[0]
    h,w = block.shape
    for x in range(h):
        if dir == "L":
            temp = block[x, :]
            block[x, :] = sorted(temp)
        if dir == "R":
            temp = block[x, :]
            block[x, :] = sorted(temp)[::-1]
        if dir == "U":
            temp = block[:, x]
            block[:, x] = sorted(temp)
        if dir == "D":
            temp = block[:, x]
            block[:, x] = sorted(temp)[::-1]
    return block

def nuf_func(img_arr, squares, frag,params, func):
    altered = np.zeros_like(img_arr)

    for channel in range(3):
        for square in squares:
            x,y,k, _ = square

            x = x * frag
            y = y * frag
            k = k * frag

            block = img_arr[x:x + k, y:y + k, channel]
            altered[x:x + k, y:y + k, channel] = func(block,params)

    return  altered

### uf

def func_hash(x, params):
    p = 10009
    q = 25601
    return ((p*x)%q)%255

def func_invert(x, params):
    return 255-x

def func_quad(x, params):
    return (x**2)/255

def func_quant(x, params):
    quant = params[0]
    return np.round(x/quant) * quant

def uf_func(img_arr, params, func):
    altered = np.zeros_like(img_arr)
    height, width, _ = img_arr.shape


    for channel in range(3):
        for i in range(0, height):
            for j in range(0, width):
                altered[i, j, channel] = func(img_arr[i,j,channel], params)
    return altered
