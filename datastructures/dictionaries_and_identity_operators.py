dictionary = dict()
dictionary = {"hydrogen": 1, "helium": 2, "carbon": 6}
dictionary["lithium"] = 3
print(dictionary)

print(dictionary.get("dilithium"))

# QUIZ

# 1

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = dict()

country = ["Shanghai", "Istanbul", "Karachi", "Mumbai"]
values = [17.8, 13.3, 13.0, 12.5]

for i in range(len(country)):
    population[country[i]] = values[i]

print(population)

# 2

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)