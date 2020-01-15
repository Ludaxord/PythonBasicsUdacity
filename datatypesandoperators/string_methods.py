name = "sebastian thurn"
print(name.title())
print(name.islower())
names = f"{name} " * 10
name_count = names.count("thurn")
print(name_count)
message = "my name is {}, nice to meet you!".format(name.title())
print(message)

# QUIZ

print(message.capitalize())
print(message.casefold())
print(message.center(12))

# Split
new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))
print(new_str.split('.'))
print(new_str.split(None, 3))


# QUIZ
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
print(verse.find("and"))
print(verse.rfind("you"))
print(verse.count("you"))