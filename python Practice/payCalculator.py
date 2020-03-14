federal_income_tax = .11
state_income_tax = .056
social_security_tax = .062
medicare_tax = .0145
total_taxes = federal_income_tax + state_income_tax + social_security_tax + medicare_tax

response = input('What\'s the salary? leave blank to use default value...\n')
if len(response) == 0:
    salary = 77500
else:
    salary = int(response)
monthly = salary / 12
weekly = salary / 52
daily = weekly / 5
hourly = daily / 8

salary_after_tax = salary - (salary * total_taxes)
monthly_after_tax = salary_after_tax / 12
weekly_after_tax = salary_after_tax / 52
daily_after_tax = weekly_after_tax / 5
hourly_after_tax = daily_after_tax / 8

print('salary:  ${:,}'.format(round(salary,2)))
print('monthly: ${:,}'.format(round(monthly,2)))
print('weekly:  ${:,}'.format(round(weekly,2)))
print('daily:   ${:,}'.format(round(daily,2)))
print('hourly:  ${:,}'.format(round(hourly,2)))

print('\nAfter Taxes:')

print('salary:  ${:,}'.format(round(salary_after_tax,2)))
print('monthly: ${:,}'.format(round(monthly_after_tax,2)))
print('weekly:  ${:,}'.format(round(weekly_after_tax,2)))
print('daily:   ${:,}'.format(round(daily_after_tax,2)))
print('hourly:  ${:,}'.format(round(hourly_after_tax,2)))
print('total taxes taken:  ${:,}'.format(round(salary * total_taxes,2)))