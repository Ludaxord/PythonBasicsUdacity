elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"] 
print(helium)
hydrogen_weight = elements["hydrogen"]["weight"]  
print(hydrogen_weight)

# QUIZ

# 1

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
print(elements['hydrogen']['is_noble_gas'])
elements['helium']['is_noble_gas'] = True
print(elements['helium']['is_noble_gas'])

