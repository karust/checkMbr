# https://github.com/hamptus/pyMBR/blob/master/mbr.py
# https://stackoverflow.com/questions/41411675/reading-boot-sector-on-windows

import os
disk_fd = os.open( r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY)
data = os.read(disk_fd, 512)
os.close(disk_fd)

print(data)