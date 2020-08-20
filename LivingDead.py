#Error code =
#elif response == input('''
#Incorrect answer! Please copy and paste the answer correctly
#''')
print('''This game is a text adventure game made to test your general knowledge, critical thinking, and problem solving abilities. To answer
the questions that will pop up during the game, copy and paste the given choices next to the question.
      ''')
print("If there are any problems with this game, please email the maker of this game at akronnie55@gmail.com")
name = input("What is your name? This information is used for game purposes only and it will not be recorded. ")
print('''
Greetings, " + name + ". You live in an apartment building near Toronto, Canada. You work as a mechanic,
you're skilled at rock climbing, and your hobby is racing. Your life has been amazing until August 17, during 
the night, at around 11 PM...
''')
print('''
You feel tired, so you decide to go to bed. After an hour, you wake up in your bed, deprived of sleep. 
Everything is quiet, so you think everything 
is normal, but you are awfully wrong. You open the fridge to grab a drink of juice, but you hear a disturbing 
retching sound outside. You open the window and you see a man walking around on the street. You close the window 
just in time to hear a scream outside. You open the window again, and the first man is grabbing another person 
by the head and ripping his head off. You start to feel dizzy. You think you're imagining things, but you hear 
a chorus of howling nearby. You step into the balcony of your home, bathed in 
moonlight, just in time to see a horde of zombies running down the road towards your apartment building. You 
see them enter the lobby, and you hear another scream. The lady at the front desk has mutated into a zombie as 
well. What do you do?
''')
response = input('''
Do you:
Call 911
Run downstairs to investigate
Climb down to your car
''')
if response == "Call 911":
    response = input('''
    You grab your phone to call 911, but the phone battery is dead. You look for your charger, but the 
    electricity stops working. The zombies must have switched off the power generator. Isn't that a little 
    too smart for a zombie to behave? What do you do now? 
    Do you:
    Run downstairs
    Get to your car ASAP
    ''')
    if response == "Run downstairs":
        response == input('''
        You open your apartment door. You check the hallway for any stray zombies. 
        You can either:
        Go down via the elevator
        Go down via the stairs
        Get to the car instead
        ''')
        if response == "Go down via the elevator":
            response == input('''
            Coming soon!
            ''')
        elif response == "Go down via the stairs":
            response == input('''
            Coming soon!
            ''')
        elif response == "Get to the car instead":
            response == input('''
            Coming soon!
            ''')
    elif response == "Get to your car ASAP":
        response == input('''
        You gather your valuables, grab your family photos (you don't feel like leaving them behind), open your 
        apartment window and casually climb down to the first floor. The zombies can't see you leave, but they 
        smell flesh, so you quickly open your car door, hop in the driver seat, and drive away.
        ''')
elif response == "Run dowstairs to investigate":
    response == input('''
    Coming soon!
    ''')
elif response == "Get to your car ASAP":
    response == input('''
    Coming soon!
    ''')
#insert error message code here