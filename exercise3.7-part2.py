#Written by Shiven Desai
#This program calculates the total sales each week
def calculate_total_sales():
    # Ask the user to enter the store's sales for each day of the week
    sales = []
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        sales.append(float(input("Enter sales for {}: ".format(day))))

    # Calculate the total sales for the week
    total_sales = sum(sales)

    # Display the total sales to the console and output to a text file
    with open('total_sales.txt', 'w') as file:
        file.write("Total sales for the week: ${:.2f}\n".format(total_sales))
        print("Total sales for the week: ${:.2f}".format(total_sales))

    # Output daily sales to the console and output to a text file
    with open('daily_sales.txt', 'w') as file:
        file.write("Daily sales for the week:\n")
        for day, sale in zip(days_of_week, sales):
            file.write("{}: ${:.2f}\n".format(day, sale))
            print("{}: ${:.2f}".format(day, sale))

calculate_total_sales()
