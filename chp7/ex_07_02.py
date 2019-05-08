fname = input ("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence: ") :
        count = count + 1
        colpos = line.find(':')
        number = line[colpos+1:]
        nnum = float(number)
        total = total + nnum

average = total/count

print('Average spam confidence:' , average)
