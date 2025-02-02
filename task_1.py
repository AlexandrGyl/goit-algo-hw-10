import pulp

prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)


lemonade = pulp.LpVariable('Lemonad', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruite_juice', lowBound=0, cat='Integer')


prob += lemonade + fruit_juice, "Total_Production"


prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
prob += 1 * lemonade <= 50, "Sugar"
prob += 1 * lemonade <= 30, "Lemon_Juice"
prob += 2 * fruit_juice <= 40, "Fruit_Puree"


prob.solve()


print("Status:", pulp.LpStatus[prob.status])
print("Лимонад:", pulp.value(lemonade))
print("Фруктовий сік:", pulp.value(fruit_juice))
print("Загальна кількість продуктів:", pulp.value(lemonade) + pulp.value(fruit_juice))
