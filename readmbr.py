# https://github.com/hamptus/pyMBR/blob/master/mbr.py
# https://stackoverflow.com/questions/41411675/reading-boot-sector-on-windows
import hashlib
import os
from binascii import hexlify, unhexlify



if __name__ == "__main__":
    m = hashlib.sha256()

    disk_fd = os.open( r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY)
    data = os.read(disk_fd, 512)
    os.close(disk_fd)

    m.update(data)
    h = m.digest()

    coolHash = b'4f198add422223d6a067f7cbdf3a99e28fbae4c6926112cc0a5449e8d9c8da12'
    
    if h == unhexlify(coolHash):
        print("Cool")
    else:
        print("Your MBR is changed by H@Cker")
    print(hexlify(h))