import os


def create_bmp(filename, width, height, rgb_array):
    def write_bmp_header(fd):
        file_size = 14 + 40 + (width * height * 4)
        os.write(fd, b'BM')  # Signature
        os.write(fd, file_size.to_bytes(4, 'little'))
        os.write(fd, b'\x00\x00')  # Reserved
        os.write(fd, b'\x00\x00')  # Reserved
        os.write(fd, (14 + 40).to_bytes(4, 'little'))  # Offset to pixel array

    def write_dib_header(fd):
        os.write(fd, (40).to_bytes(4, 'little'))  # DIB header size
        os.write(fd, width.to_bytes(4, 'little'))
        os.write(fd, height.to_bytes(4, 'little'))
        os.write(fd, (1).to_bytes(2, 'little'))  # Number of color planes
        os.write(fd, (24).to_bytes(2, 'little'))  # Bits per pixel
        os.write(fd, b'\x00\x00\x00\x00')  # Compression (none)
        os.write(fd, b'\x00\x00\x00\x00')  # Image size (can be 0 for BI_RGB)
        os.write(fd, b'\x13\x0B\x00\x00')  # Horizontal resolution (2835 ppm)
        os.write(fd, b'\x13\x0B\x00\x00')  # Vertical resolution (2835 ppm)
        os.write(fd, b'\x00\x00\x00\x00')  # Number of colors in palette
        os.write(fd, b'\x00\x00\x00\x00')  # Important colors

    fd = os.open(filename, os.O_RDWR | os.O_CREAT | os.O_TRUNC, 0o644)

    # BMP header
    write_bmp_header(fd)

    # DIB header
    write_dib_header(fd)

    # Pixel array (bitmap data)
    for y in range(height-1, -1, -1):  # BMP rows are bottom to top
        for x in range(width):
            r, g, b = rgb_array[y][x]
            r_byte = int(r).to_bytes(1, byteorder='big')
            g_byte = int(g).to_bytes(1, byteorder='big')
            b_byte = int(b).to_bytes(1, byteorder='big')
            os.write(fd, b_byte)  # BMP format uses BGR
            os.write(fd, g_byte)  # BMP format uses BGR
            os.write(fd, r_byte)  # BMP format uses BGR
        s = (4 - (3*width)%4)%4
        os.write(fd, b'\x00' * s)

    os.fsync(fd)
    os.close(fd)

# # Example usage
# width = 5
# height = 4
# rgb_array = [
#     [(255, 255, 255), (255, 0  , 255), (255, 255, 255), (0  , 0  , 0  ), (255, 255, 255)],
#     [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)],
#     [(255, 255, 255), (255, 255, 255), (255, 0  , 255), (255, 255, 255), (0  , 255, 255)],
#     [(255, 255, 255), (255, 255, 255), (255, 255, 0  ), (255, 255, 255), (255, 255, 255)]
# ]
# create_bmp('example.bmp', width, height, rgb_array)
#
