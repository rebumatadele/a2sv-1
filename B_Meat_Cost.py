n = int(input())
min_ = float('+inf')
total = 0
for _ in range(n):
    amount, price = map(int, input().split())
    price = min(min_, price)
    min_ = price
    total += amount * price
print(total)
# print(amount, price)