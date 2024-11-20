def generate_password(n):
    result = ""

    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n): # Fixed it
            pairs.append((i, j))

    for a, b in pairs:
        pair_sum = a + b
        if n % pair_sum == 0:
            result += f"{a}{b}"

    return result


passwords = {n: generate_password(n) for n in range(3, 21)}

for n in range(3, 21):
    print(f"{n} - {passwords[n]}")