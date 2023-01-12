import argparse
from .gpstofile import GPSToFile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--readrate')
    parser.add_argument('-p', '--path')
    parser.add_argument('-d', '--debug')
    args = parser.parse_args()
    gps = GPSToFile(args.path, readrate=args.readrate, debug=args.debug)
    gps.loop()


if __name__ == "__main__":
    main()