from datetime import datetime

import time
from typing import Tuple
import serial

UBLOX_CONTROL_BYTE = 36

class GPSToFile:

    def __init__(self, path: str, baudrate: int = 9600, readrate: int = 1, debug: bool = False):
        self._ser = serial.Serial(path, baudrate=baudrate, timeout=1)
        self._read_rate = readrate
        self._debug = debug        
        print(str(datetime.utcnow()) + ' -- Initialized GPSToFile. Listening on "' + path + '" --')
        if self._debug:
            print(str(datetime.utcnow()) + ' --  readrate: ' + str(readrate) + ' seconds')
            print(str(datetime.utcnow()) + ' --  baudrate: ' + str(baudrate) + ' seconds')

    def _wait_for_ctrl(self):
        bytes = self._ser.read(1)
        while bytes[0] is not UBLOX_CONTROL_BYTE:
            bytes = self._ser.read(1)

    def _read_sentence(self) -> Tuple[str, str]:
        data = self._ser.read_until()
        data = str(data, 'utf-8').replace('\r\n', '')
        data = data.split(',')
        return [data[0], ','.join(data[1:])]

    def loop(self):
        while True:
            self._wait_for_ctrl()
            [command, payload] = self._read_sentence()
            f = open(command, 'w')
            f.write(payload)
            if self._debug:
                print(str(datetime.utcnow()) + ' [' + command + '] << ' + payload)
            time.sleep(1)
