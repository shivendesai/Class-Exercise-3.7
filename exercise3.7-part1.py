#Written by Shiven Desai
#This program practices lists and outputing them to a text file
def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum += value
    average = sum / len(numbers)

    with open('numbers.txt', 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')

    print('The total is {}, the average is {}'.format(sum, average))

total()
