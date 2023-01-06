def sum(x, y):
    return x + y 

print(sum(5, 5))

bill = 175.0
tax_rate = 15

total_tax = (bill * tax_rate) / 100.0
# result = enumerate('Total tax is', total_tax)
# print(result)

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.0)

print('--------------------')
# result1 = enumerate('Total tax is', calculate_tax(129.33, 12))
# print(result1)

print('Total tax:', calculate_tax(391.44, 12.3))