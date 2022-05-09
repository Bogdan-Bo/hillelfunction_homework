def seasons(month):
    if month in range(3,6):
        return "Spring"
    elif month in range(6, 9):
        return "Summer"
    elif month in range(9, 12):
        return "Autumn"
    elif month == 12 or 1 or 2:
        return "Winter"
print(seasons(2))