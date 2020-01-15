points = 174  # use this input to make your submission

# write your if statement here
if points > 0 and points <= 50:
    prize = "wooden rabbit"
elif points > 50 and points <= 150:
    prize = "no prize"
elif points > 150 and points <= 180:
    prize = "wafer-thin mint"
elif points > 180 and points <= 200:
    prize = "penguin"

if prize != "no prize":
    result = "Congratulations! You won a " + prize
else:
    result = "Oh dear, "+ prize +" this time."

print(result)