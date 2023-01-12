# GPSToFile

Quick and easy way to read GPS sentences to file with no gpsd required.

![running on a ublox gps dongle](https://github.com/pubudeux/gpstofile/blob/main/example-run.png)

## Getting Started

Once you get the serial path of your GPS modem, you can get started either via command line, or by importing the module:

`python -m gpstofile --port /dev/tty.usbmodem14401 --debug True`

or:


```python
from gpstofile import GPSToFile

gps = GPSToFile('/dev/tty.usbmodem14401', readrate=1, debug=True)

gps.loop()
```

