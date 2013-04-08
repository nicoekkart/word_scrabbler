import itertools as it
import enchant

letters = input("Please provide me with some letters, I wanna start scrabbling!!!")
length = int(input("Well, what length of string do you want"))

d = enchant.Dict('en_US')
# generator with words. 
words = (i for i in it.permutations(letters,length) if d.check(i))
print("I have found all the words and will now print them out one by one.\nPress enter if you want another word, 'x' if you want to stop and 'a' if you want them all printed out at once.")
ui = None
for word in words:
	print(word)
	if ui!='a': ui = input()
	if ui=='x': break