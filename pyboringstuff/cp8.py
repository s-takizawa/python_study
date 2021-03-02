import pyinputplus as pyip

print("start")

while True:
    print("Enter your age:")
    # age = input()
    age = 11

    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue

    if age < 0:
        print('Please enter a positive number.')
        continue
    break

print('your age is {}.'.format(age))


print("----------------")

# response = pyip.inputNum(prompt="Enter a number:",
#                          min=4, lessThan=100, blank=True)

# response = pyip.inputNum(prompt="enter a number:", limit=1, default='none')
# print(response)

# response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# print(response)

print("----------------")


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbersList)))
    return int(numbers)  # Return an int form of numbers.

# response = pyip.inputCustom(addsUpToTen)
# print(response)

print("end")
