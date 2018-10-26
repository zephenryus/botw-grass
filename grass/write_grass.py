import struct


def compile_grass(data: list) -> bytes:
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    grass_binary = b''
    for index in range(4096):
        grass_binary += struct.pack(
            '<4B',
            data[index].height,
            data[index].r,
            data[index].g,
            data[index].b
        )

    return grass_binary


def write_grass(data: list, outfile_name: str) -> None:
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    with open(outfile_name, 'wb+') as outfile:
        binary_data = compile_grass(data)
        outfile.write(binary_data)
