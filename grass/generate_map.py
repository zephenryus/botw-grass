from PIL import Image


def generate_height_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64

        color_value = round(data[index].height * 255)
        color = (color_value, color_value, color_value)

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)


def generate_color_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    color_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64
        color = (data[index].r, data[index].g, data[index].b)

        color_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    color_map_image.save(outfile)
