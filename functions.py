def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200,500,700]

tom_expenses = calculate_total(tom_exp_list)
joe_expenses = calculate_total(joe_exp_list)

print("Tom's expense list :", tom_expenses)
print("Joe's expense list:", joe_expenses)


