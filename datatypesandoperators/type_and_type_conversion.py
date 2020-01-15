print(type("444"))
print(type(444))
print(type(444.0))

count = int(444.0)
print(type(count))

grams = "35.0"
print(type(grams))
float_grams = float(grams)
print(type(float_grams))

# QUIZ

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

sales = [mon_sales, tues_sales, wed_sales, thurs_sales, fri_sales]
for index, sale in enumerate(sales):
    sales[index] = int(sale) 
sum_sales = sum(sales)
print(type(sum_sales))
sum_sales = str(sum_sales)
print(type(sum_sales))
message = f"This week's total sales: {sum_sales}"
message = "This week's total sales: " + sum_sales
print(message)    