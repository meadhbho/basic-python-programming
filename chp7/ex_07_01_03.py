fname = input("Enter file name: ")
fh = open(fname)
for lx in fh:
    ly = lx.rstrip()
    lc = ly.upper()
    print(lc)
