hrs = input ("Enter your hours:")
rate = input ("Enter your rate:")

h = float (hrs)
r = float (rate)

if h <= 40:
  print  (h*r)

else:
  nt = 40*r
  ot = (h - 40)*10.5
  print (nt + ot)
