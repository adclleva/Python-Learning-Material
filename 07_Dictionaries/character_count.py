import pprint

# character count
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

allCharacterCount = {}
normalCharacterCount = {}

for character in message:
    allCharacterCount.setdefault(character, 0)
    allCharacterCount[character] += 1

for character in message.lower():
    normalCharacterCount.setdefault(character, 0)
    normalCharacterCount[character] += 1

for item in allCharacterCount.items():
    print(item)

print()

for item in normalCharacterCount.items():
    print(item)

print()


# you can use the pretty print module
pprint.pprint(allCharacterCount)

pprint.pformat(allCharacterCount)