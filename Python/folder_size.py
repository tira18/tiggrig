import os
from pathlib import Path
def get_size(line):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(line):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

p = Path('C:\\Users\\tigran.grigoryan.a\\AppData\\Local')
subdirectories = [x for x in p.iterdir() if x.is_dir()]
for line in subdirectories:
    size = get_size(line)
    MB ='{:,.0f}'.format(size/float(1<<20))
    GB = '{:,.0f}'.format(size/float(1<<30))


    if int(GB) == 0:
        print("Folder size: " + str(line)+ "\t"+str(MB+" MB"))
    else:
        print("Folder size: " + str(line)+ "\t"+str(GB+" GB"))

