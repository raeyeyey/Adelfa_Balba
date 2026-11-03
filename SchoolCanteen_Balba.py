meet_target = 0
below_target = 0
total_sales = 0
number_of_items = int(input("Enter number of food items: "))

for i in range (number_of_items):
    sales = int(input(f"Enter sales for item {i + 1}: "))
    total_sales += sales
    if sales >= 500:
        meet_target += 1
    else:
        below_target += 1

def calculate_average(total_sales, number_of_items):
    average_sales = total_sales/number_of_items
    return average_sales

def display_report():
    print("CANTEEN SALES REPORT")
    print(f"Average Sales: PHP{calculate_average(total_sales, number_of_items):.2f} | Meeting Target: {meet_target} | Below Target: {below_target}")

calculate_average(total_sales, number_of_items)
display_report()