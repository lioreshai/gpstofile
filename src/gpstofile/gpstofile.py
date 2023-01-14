from datetime import datetime

import time
from typing import Tuple
import serial

CONTROL_BYTE = 36

class GPSToFile:

    def __init__(self, path: str, baudrate: int = 115200, readrate: float = 0, debug: bool = False, append: bool = False):
        if readrate is None:
            self._readrate = 0
        else:
            self._readrate = float(readrate)
        if baudrate is None:
            baudrate = 115200
        self._debug = debug
        self._append = append   
        self._ser = serial.Serial(path, baudrate=baudrate, timeout=1)     
        print(str(datetime.utcnow()) + ' -- Initialized GPSToFile. Listening on "' + path + '" --')
        if self._debug:
            print(str(datetime.utcnow()) + ' --  readrate: ' + str(self._readrate) + ' seconds')
            print(str(datetime.utcnow()) + ' --  baudrate: ' + str(baudrate) + ' seconds')

    def _wait_for_ctrl(self):
        bytes = self._ser.read(1)
        while bytes[0] is not CONTROL_BYTE:
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
            f = open(command, 'a' if self._append else 'w')
            f.write(payload)
            if self._debug:
                print(str(datetime.utcnow()) + ' [' + command + '] << ' + payload)
            time.sleep(self._readrate)
