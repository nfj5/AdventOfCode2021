position = {
    "horizontal": 0,
    "vertical": 0,
}

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    for line in lines:
        parts = line.split(" ")
        direction = parts[0]
        amount = int(parts[1])

        if direction == "forward":
            position["horizontal"] += amount
        elif direction == "up":
            position["vertical"] -= amount
        else:
            position["vertical"] += amount

print(position["horizontal"], ",", position["vertical"])
print(position["horizontal"] * position["vertical"])

# 1968 , 1063
# 2091984
