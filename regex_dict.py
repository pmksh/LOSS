regex_dictionary = {
    "load"      : "load\\s+<(.+)>\\s*",
    "save"      : "save\\s+<([\\w]+)>\\s*",
    "frag"      : "frag\\s+<([\\d]+)>\\s*",

    "fft"       : "fft\\s+<([HVT])>\\s*",
    "fft-nu"    : "fft\\s+-nu\\s+<([HVT])>\\s*",
    "ifft"      : "invfft\\s+<([HVT])>\\s*",
    "ifft-nu"   : "invfft\\s+-nu\\s+<([HVT])>\\s*",

    "dct"       : "cosine\\s+<([HVT])>\\s*",
    "dct-nu"    : "cosine\\s+-nu\\s+<([HVT])>\\s*",
    "idct"      : "invcos\\s+<([HVT])>\\s*",
    "idct-nu"   : "invcos\\s+-nu\\s+<([HVT])>\\s*",

    "dst"       : "sine\\s+<([HVT])>\\s*",
    "dst-nu"    : "sine\\s+-nu\\s+<([HVT])>\\s*",
    "idst"      : "invsin\\s+<([HVT])>\\s*",
    "idst-nu"   : "invsin\\s+-nu\\s+<([HVT])>\\s*",

    "wht"       : "wht\\s+<([HVT])>\\s*",
    "wht-nu"    : "wht\\s+-nu\\s+<([HVT])>\\s*",
    "iwht"      : "invwht\\s+<([HVT])>\\s*",
    "iwht-nu"   : "invwht\\s+-nu\\s+<([HVT])>\\s*",

    "block"     : "block\\s*",
    "block-nu"  : "block\\s+-nu\\s*",

    "sort"      : "sort\\s+<([UDLR])>\\s*",
    "sort-nu"   : "sort\\s+-nu\\s+<([UDLR])>\\s*",

    "quant"     : "quant\\s+<(\\d+)>\\s*",
    "squares"   : "squares\\s+<(-?\\d+)>s*",
    "quad"      : "quad\\s*",
    "invert"    : "invert\\s*",
    "hash"      : "hash\\s*",

    "flip"      : "flip\\s+<([HVT])>\\s*",
    "flip-nu"      : "flip\\s+-nu\\s+<([HVT])>\\s*"
}