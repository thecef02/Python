print('Hello!')
print('I am your computer, I would like to know something about you.')
name=input('What is you name?')
color=input('And ' + name.title() + ', What is you favorite color?')
print('Thank you ' + name.title() + '.\n')
print('Now I know you better.')
print('Your name is ' + name.title() + ' and your favorite color is "' + color + '".\n\n')


"""I made it look like the PC is talking to you. 
I used concatenation to display name in a proper way 
in case you enter the name in all lower case.""" 
#It will display the name and color in one line with 
#color in betwen " " and I added some blank lines for 
#separation using "\n".