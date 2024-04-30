number = int(input("Enter a number: "))

count_set_bits = 0

while number:
    count_set_bits += number & 1
    number >>= 1

print(f"No. of set bits in {number} is: {count_set_bits}")