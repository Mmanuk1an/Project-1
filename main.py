from random import randint

# Choosing the right template

def choose(n):
    if n == 1:
        temp1() # Calling function for first template
    elif n == 2:
        temp2() # Calling function for second template
    elif n == 3:
        temp3() # Calling function for third template
    else:
        return -1

    
def temp1():
    # Here are the all inputs for Template 1

    number = int(input("Input a Number: "))
    mesTime = input("Input a Measure of Time: ")
    modTrans = input("Input a Mode of Transportation: ")
    adjv  = input("Input an Adjective: ")
    adjv2 = input("Input an Adjective(2): ")
    noun = input("Input a Noun: ")
    color = input("Input a Color: ")
    partOf = input("Input a Part of the body: ")
    verb = input("Input a Verb: ")
    number2 = int(input("Input a Number(2): "))
    noun2 = input("Input a Noun(2): ")
    noun3 = input("Input a Noun(3): ")
    partOf2 = input("Input a Part of the body(2): ")
    verb2 = input("Input a Verb(2): ")
    noun4 = input("Input a Noun(4): ")
    adjv3 = input("Input an Adjective(3): ")
    silly = input("Input a Silly Word: ")
    noun5 = input("Input a Noun(5): ")

    # Here is the formating string
    temp = f'''
    It was about {number} {mesTime} ago when I arrived at the hospital in a {modTrans}.
    The hospital is a {adjv} place, there are a lot of {adjv2} {noun} here. There are nurses here who
    have {color} {partOf}. If someone wants to come into my room I told them that they have to {verb}
    first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a
    {noun3} on their {partOf2}. I heard that all doctors {verb2} {noun4} every day for breakfast. The most
    {adjv3} thing about being in the hospital is the {silly} {noun5} !
    '''
    # Function returns

    print(temp)

def temp2():
    # Here are the all inputs for Template 2

    persName = input("Input a Proper Noun (Person’s Name): ")
    noun = input("Input a Noun: ")
    adjv = input("Input an Adjective(Feeling): ")
    verb = input("Input a Verb: ")
    adjv2 = input("Input an Adjective(Feeling)(2): ")
    animal = input("Input a/an Animal: ")
    verb2 = input("Input a Verb(2): ")
    color = input("Input a Color: ")
    verbing = input("Input a Verb (ending in ing): ")
    adverb = input("Input an Adverb (ending in ly): ")
    number = int(input("Input a Number: "))
    mesTime = input("Input a Measure of Time: ")
    color2 = input("Input a Color (2): ")
    animal2 = input("Input a/an Animal (2): ")
    number2 = int(input("Input a Number(2): "))
    silly = input("Input a Silly Word: ")
    noun2 = input("Input a Noun(2): ")

    # Here is the formating string

    temp = f'''
    This weekend I am going camping with {persName}. I packed my lantern, sleeping bag,
    and {noun}. I am so {adjv} to {verb} in a tent. I am {adjv2} we might see 
    {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I
    have heard that the {color} lake is great for {verbing}. Then we will {adverb} hike
    through the forest for {number} {mesTime}. If I see a {color2} {animal2} while hiking, I am going to bring
    it home as a pet! At night we will tell {number2} {silly} stories and roast {noun2} around the campfire!!
    '''
    # Function returns

    print(temp)

def temp3():
    # Here are the all inputs for Template 3

    persName = input("Input a Proper Noun (Person’s Name): ")
    adjv = input("Input an Adjective(Feeling): ")
    color = input("Input a Color: ")
    animal = input("Input a/an Animal: ")
    place = input("Input a Place: ")
    adjv2 = input("Input an Adjective(Feeling)(2): ")
    magicCreature = input("Input Magical Creature (Plural): ")
    adjv3 = input("Input an Adjective(3): ")
    magicCreature2 = input("Input Magical Creature (Plural)(2): ")
    room  = input("Input a Room in a House: ")
    noun = input("Input a Noun: ")
    noun2 = input("Input a Noun(2): ")
    noun3 = input("Input a Noun(Plural)(3): ")
    adjv4 = input("Input an Adjective(4): ")
    noun4 = input("Input a Noun(Plural)(4): ")
    number = int(input("Input a Number: "))
    mesTime = input("Input a Measure of Time: ")
    verbing = input("Input a Verb (ending in ing): ")
    adjv5 = input("Input an Adjective(5): ")
    noun5 = input("Input a Noun (5): ")

    # Here is the formating string

    temp = f'''
    Dear {persName}, I am writing to you from a {adjv} castle in an enchanted forest. I
    found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjv2} {magicCreature} 
    and {adjv3} {magicCreature2} here! In the {room} there is a pool full
    of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjv4} {noun4}. It
    feels as though I have lived here for {number} {mesTime}. I hope one day you can visit, although the
    only way to get here now is {verbing} on a {adjv5} {noun5}!!
    '''
    # Function returns

    print(temp)


# Checking users input

num = int(input('Please choose a number between 1 - 3 (included) or for Random type (0): '))
if num in range(1, 4):
    choose(num)
elif num == 0:
    n = randint(1, 3)
    choose(n)
else:
    print("ERROR!!!  You entered wrong number!")




