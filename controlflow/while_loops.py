card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    print(current)
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)


# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range(2, number + 1):
    product *= i

# print the factorial of number
print(product)