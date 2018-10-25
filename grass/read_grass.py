import os
import struct

from .Grass import Grass


def read_grass(path: str, verbose=False) -> list:
    """
    Decompiles terrain grass to a list of Grass objects

    :param path:        Path to .grass.extm file to be decompiled
    :param verbose:     Print messages to console
    :return:            List of Grass objects
    """
    grass_array = []

    if os.path.exists(path):
        if verbose:
            print("Reading {}...".format(path))

        with open(path, 'rb') as infile:
            # Each file contains 4,096 entries (64 * 64)
            for _ in range(4096):
                height, r, g, b = struct.unpack('<4B', infile.read(4))
                grass_array.append(Grass(
                    height,
                    r,
                    g,
                    b
                ))

    return grass_array
