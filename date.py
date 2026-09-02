day = int(input('days: '))
years = day // 365
remaining_day = day % 365
months = remaining_day // 30
days = remaining_day % 30
print(f"{day} is {years} years and {months} months and {days} days.")