import os

# LETTER TEMPLATE
starting_letter = ""
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

# NAMES
invited_names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    for line in file.readlines():
        invited_names.append(line.strip())

# ENDING LETTER
for name in invited_names:
    ending_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(ending_letter)
    # os.remove(f"./Output/ReadyToSend/{name}.txt")

