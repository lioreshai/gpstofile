import argparse
from .gpstofile import GPSToFile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--readrate')
    parser.add_argument('-p', '--path')
    parser.add_argument('-d', '--debug')
    parser.add_argument('-o', '--overwrite')
    args = parser.parse_args()
    gps = GPSToFile(args.path, readrate=args.readrate, debug=args.debug, overwrite=args.overwrite)
    gps.loop()


if __name__ == "__main__":
    main()