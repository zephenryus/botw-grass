import filecmp
import hashlib
import json

import grass


def grass_to_json():
    """
    Tests reading of grass file and exports data as a json file
    """
    data = grass.read_grass("assets/5000000000.grass.extm")

    print("Saving file output/5000000000.grass.extm.json...")
    with open("output/5000000000.grass.extm.json", "w+") as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def grass_to_binary_string():
    """
    Tests that data is recompiled correctly and matches the original file
    """
    data = grass.read_grass("assets/5000000000.grass.extm")
    binary_data = grass.compile_grass(data)

    hash_md5 = hashlib.md5()
    with open("assets/5000000000.grass.extm", "rb") as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            hash_md5.update(chunk)

    file_hash = hash_md5.hexdigest()

    hash_md5 = hashlib.md5()
    pos = 0
    for chunk in iter(lambda: binary_data[pos:pos + 4096], b""):
        pos += 4096
        hash_md5.update(chunk)

    string_hash = hash_md5.hexdigest()

    print("The file and binary string are the same: {0}".format(file_hash == string_hash))


def grass_to_binary_file():
    """
    Tests reading data from grass file then writes the same data back as a binary
    """
    data = grass.read_grass("assets/5000000000.grass.extm")
    grass.write_grass(data, "output/5000000000.grass.extm")
    print("The files are the same: {0}".format(
        filecmp.cmp("assets/5000000000.grass.extm", "output/5000000000.grass.extm")))


def main():
    grass_to_json()
    grass_to_binary_string()
    grass_to_binary_file()
    # grass_to_image()


if __name__ == "__main__":
    main()
