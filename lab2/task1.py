from decimal import Decimal
from fractions import Fraction

prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

discount = 0.07
vat = 0.20

# float
sum_float = sum(prices) * (1 - discount) * (1 + vat)

print("FLOAT")
print("Итоговая сумма:", sum_float)
print("Одна из трех частей:", sum_float / 3)


# decimal
prices_decimal = [Decimal(str(p)) for p in prices]
sum_decimal = sum(prices_decimal) * (Decimal("1") - Decimal(str(discount))) * (Decimal("1") + Decimal(str(vat)))

print("DECIMAL")
print("Итоговая сумма:", sum_decimal)
print("Одна из трех частей:", sum_decimal / Decimal("3"))


# fraction
prices_fraction = [Fraction(str(p)) for p in prices]
sum_fraction = sum(prices_fraction) * (1 - Fraction(7, 100)) * (1 + Fraction(1, 5))

print("FRACTION")
print("Итоговая сумма:", float(sum_fraction))
print("Одна из трех частей:", float(sum_fraction / 3))