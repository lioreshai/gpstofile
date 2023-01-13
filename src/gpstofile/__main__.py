import argparse
from .gpstofile import GPSToFile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--readrate')
    parser.add_argument('-b', '--baudrate')
    parser.add_argument('-p', '--path')
    parser.add_argument('-d', '--debug')
    parser.add_argument('-a', '--append')
    args = parser.parse_args()
    gps = GPSToFile(args.path, baudrate=args.baudrate, readrate=args.readrate, debug=args.debug, append=args.append)
    gps.loop()


if __name__ == "__main__":
    main()