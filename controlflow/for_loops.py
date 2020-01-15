cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for s in sentence:
    print(s)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5,31,5):
    print(i)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    usernames.append(name.lower().replace(' ', '_'))
print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index, name in enumerate(usernames):
    usernames[index] = name.lower().replace(' ', '_')

print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += f"<li>{item}</li>\n"
html_str += "</ul>"

print(html_str)