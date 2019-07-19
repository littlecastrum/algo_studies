#!/usr/bin/env python3

import sys, getopt, glob, os

def find_files(suffix, path):
    for file in glob.glob(f"{path}/**/*.{suffix}", recursive=True):
        print(file)

def usage():
    print("usage: ex [-h] [-f filetype] [-o outfile]")
    print("  -h             display help")
    print("  -f filetype    specify file type (ex: .c, .js, .lua)")
    print("  -d directory   specify directory")

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hd:f:", ["help", "dir=", "filetype="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    filetype = None
    directory = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--dir"):
            directory = os.path.abspath(os.path.join(os.path.dirname(__file__), a))
        elif o in ("-f", "--filetype"):
            filetype = a
        else:
            assert False, "unhandled option"
    if filetype is None or directory is None:
        usage()
        sys.exit(2)
    find_files(filetype, directory)

if __name__ == '__main__':
    main()