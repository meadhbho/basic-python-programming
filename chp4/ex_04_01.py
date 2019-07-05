def computepay(h,r):
    pay = 0
    if h <= 40:
      pay = h*r
      return pay
    elif h > 40:
      pay = (h - 40)* (r*1.5) + 40*r
      return pay




hrs = input ("Enter hours:")
rate = input ("Enter rate:")

h = float (hrs)
r = float (rate)

print (computepay(h, r))
