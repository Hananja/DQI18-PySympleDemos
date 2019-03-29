# Zeilen zählen

# Alternative 1
file = open("primes.txt", "r")
print(len(file.readlines()))
file.close()

# Alternative 2
print(len(open("primes.txt").readlines()))

# Alternative 3 (mit counter)
count = 0
with open("primes.txt") as infile:
    for line in infile:
        count += 1
print(count)