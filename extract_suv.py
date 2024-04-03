import re
import argparse


#fic = "./20200527152905.861802.ig.tum"


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("fichier", help="indiquer le nom du fichier", type=str)
    return parser.parse_args()

def do_it(*arg):
    with open(*arg, "r") as f:
        lines = f.read()

        m = re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)",lines, re.M)

        d = {el[0]:float(el[1]) for el in m}
        print(d)

if __name__ == "__main__":
    arg = parse()
    do_it(arg.fichier)
