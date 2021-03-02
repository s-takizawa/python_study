import traceback

print('start')

# raise Exception('this is hte error message.')


print('------')

# assertions
assert 1 == 1
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
# AssertionError
# assert ages[0] >= ages[-1]
assert ages[0] <= ages[-1]


print('------')

# traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open(r'..\sample\errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

print('end')
