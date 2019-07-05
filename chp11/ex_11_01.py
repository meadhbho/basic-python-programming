import re
fh = open('regex_sum_219981.txt')
numlist = list()

for line in fh:
    numline = re.findall('[0-9]+', line)
    if len(numline) > 0:
        for numl in numline:
            numlist.append(int(numl))
sum = 0
for number in numlist:
    sum = sum + number


print (numlist)
print (sum)
