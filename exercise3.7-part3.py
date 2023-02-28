#Written by Shiven Desai
#This program calculates the highest and lowest amounts of rainfall
def rainfall():
    # Initialize list of months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']

    # Ask user to input rainfall for each month
    rainfall = []
    for month in months:
        rainfall.append(float(input(f"Enter rainfall for {month}: ")))

    # Calculate total rainfall for the year
    total_rainfall = sum(rainfall)

    # Calculate average monthly rainfall
    avg_rainfall = total_rainfall / 12

    # Find month with highest and lowest rainfall
    max_rainfall_month = months[rainfall.index(max(rainfall))]
    min_rainfall_month = months[rainfall.index(min(rainfall))]

    # Output results to console and file
    with open("rainfall_results.txt", "w") as f:
        print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
        f.write(f"Total rainfall for the year: {total_rainfall:.2f} inches\n")

        print(f"Average monthly rainfall: {avg_rainfall:.2f} inches")
        f.write(f"Average monthly rainfall: {avg_rainfall:.2f} inches\n")

        print(f"Month with highest rainfall: {max_rainfall_month} ({max(rainfall):.2f} inches)")
        f.write(f"Month with highest rainfall: {max_rainfall_month} ({max(rainfall):.2f} inches)\n")

        print(f"Month with lowest rainfall: {min_rainfall_month} ({min(rainfall):.2f} inches)")
        f.write(f"Month with lowest rainfall: {min_rainfall_month} ({min(rainfall):.2f} inches)\n")

rainfall()
