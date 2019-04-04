import random

question3Dict = {'What is your favorite color?': 'blue', 'What is the capital of Assyria?': 'Assur', 'What is the airspeed velocity of an unladen swallow?': '11 m/s'}

print('What is your name?')    # ask for their name
myName = input()
print('Greetings, ' + myName)
print('What is your quest?')    
myAge = input()
# random item from question3

question3 = random.choice(list(question3Dict.keys()))
answer3 = question3Dict.get(question3)
print(question3)
response3 = input()
if response3 == answer3:
    print('Right, off you go then.')
else:
    print('AAAAAAHHHHHHH')