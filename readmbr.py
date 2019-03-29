# https://github.com/hamptus/pyMBR/blob/master/mbr.py
# https://stackoverflow.com/questions/41411675/reading-boot-sector-on-windows
import hashlib
import os
from binascii import hexlify, unhexlify
from window import WarningWindow
import sys
from PyQt5 import QtCore, QtWidgets


def checkMbr():
    app = QtWidgets.QApplication(sys.argv)
    m = hashlib.sha256()

    disk_fd = os.open( r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY)
    data = os.read(disk_fd, 512)
    os.close(disk_fd)

    m.update(data)
    h = m.digest()

    coolHash = b'4f198add422223d6a067f7cbdf3a99e28fbae4c6926112cc0a5449e8d9c8da12'
    h = b'123'
    if h == unhexlify(coolHash):
        print("Everything's OK")
    else:
        message = ("Evil Maid attack is detected!\n\n"
        "Original MBR hash is: \n{0} \n\n"
        "Current MBR hash is: \n{1}").format(coolHash[2:-1], h[2:-1])

        
        warn = WarningWindow(message)
        warn.show()
    sys.exit(app.exec_() )

if __name__ == "__main__":
   checkMbr()


   