from gpstofile import GPSToFile

gps = GPSToFile('/dev/tty.usbmodem14401', readrate=1, debug=True)

gps.loop()