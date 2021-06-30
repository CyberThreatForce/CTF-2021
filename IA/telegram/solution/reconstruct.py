#!/usr/bin/python3
import glob
from apng import APNG

def main():
    lst_files = sorted(glob.glob(str('./*.bmp')))
    APNG.from_files(lst_files, delay=100).save('chall2_stego.png')


if __name__=="__main__":
    main()
