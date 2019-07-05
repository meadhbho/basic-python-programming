fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From ") :
        count = count + 1
        ls = line.split()
        lf = ls[1]
        print (lf)

print("There were", count, "lines in the file with From as the first word")
