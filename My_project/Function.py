def sum(a, b):
    return a + b
print(sum(2,5))


def calculate_mean(numbers):
    if not numbers:
        return 0
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)
print(calculate_mean([1, 2, 3, 4]))
print(calculate_mean([]))



features = ["age", "income", "score"]
for feature in features:
    print(f"Processing {feature}")




data = [1, 2, 3, 4, 5, 6]
sum = 0
for i, value in enumerate(data):
    if value % 2 == 0:
        sum += value
    print(sum)

data = [1, 2, 3, 4, 5, 6]
total = 0
for value in data:
    if value % 2 == 0:
        total += value
print(total)  # 12
