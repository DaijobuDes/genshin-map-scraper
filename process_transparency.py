from PIL import Image

def process_transparency(img):
    r, g, b, a = img.split()

    # Get alpha data as a sequence
    alpha_data = a.getdata()

    has_transparency = any(pixel < 255 for pixel in alpha_data)

    if has_transparency:
        # print("Transparent pixels detected. Updating colors...")

        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                current_r, current_g, current_b, current_a = pixels[x, y]

                if current_a == 0:
                    # pixels[x, y] = (0, 0, 0, 255)
                    pixels[x, y] = (16, 23, 31, 255)

    return img
