import json

import grass


def grass_to_json():
    """
    Tests reading of mate file and exports data as a json file
    """
    data = grass.read_grass("assets/5000000000.grass.extm")

    print("Saving file output/5000000000.grass.extm.json...")
    with open("output/5000000000.grass.extm.json", "w+") as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def main():
    grass_to_json()
    # mate_to_binary_string()
    # mate_to_binary_file()
    # mate_to_image()


if __name__ == "__main__":
    main()
