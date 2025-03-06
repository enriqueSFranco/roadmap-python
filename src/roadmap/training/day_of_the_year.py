def is_leap_year(year):
  return year % 4 == 0 and year and (year % 100 != 0 or year % 400 == 0)

def dayOfYear(date: str) -> int:
  year, month, day = map(int, date.split("-")) # YYYY-MM-DD -> 2019-01-09
  days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # total de dias que hay en los meses, sin contar que es año bisiesto
  
  # verificamos si el año es bisiesto
  if is_leap_year(year):
    days_in_month[2] = 29

  day_of_year = sum(days_in_month[:month]) + day
  
  return day_of_year

print(dayOfYear("2019-01-09"))