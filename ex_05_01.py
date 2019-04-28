largest = None
smallest = None
while True :
    sval = raw_input('Enter number: ')
    if sval == 'done':
      break
    try:
      fval = float (sval)
      if smallest is None or fval < smallest:
          smallest = fval
      if largest is None or fval > largest:
          largest = fval
    except:
      print('Invalid Input')
      continue


print ('Maximum is {}'.format(largest))
print ('Minimum is {}'.format(smallest))
