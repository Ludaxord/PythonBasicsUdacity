print("hello")
print('hello')

welcome_message = "hello world!"
print(welcome_message)

message = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
print(message)

message = '"I think you\'re an encyclopedia salesman"'
print(message)

first_word = "hello"
second_word = "world"
print(first_word + " " + second_word)

word = "hello"
print(word * 5)
word_len = len("udacity")
print(word_len)

# QUIZ

# 1

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

# 2
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
print(type(tropical_fruit_count))

# 3
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
server_message = f"{username} accessed the site {url} at {timestamp}."
print(server_message)
# or
server_message = username + " accessed the site " + url + " at " + timestamp + "."
print(server_message)

# 4
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(f"{given_name} {middle_names} {family_name}") #todo: calculate how long this name is 
name_length = len(given_name + " " + middle_names + " " + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)