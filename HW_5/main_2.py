names = ["Nikita", "Anton", "Denis"]
rates = [100, 200, 300]
bonuses = ["10.25%", "5.5%", "7.75%"]

dictionary = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(dictionary)