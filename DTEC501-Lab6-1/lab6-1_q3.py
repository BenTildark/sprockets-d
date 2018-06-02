"""
Write a program to ask the user for their name and then ask them to enter a sentence.
Your program must decide if the text they entered was a sentence and if so then examine the number of vowels present.



Ask the user to enter their first name by displaying the message:
Please enter your first name:


Display the message:
<FirstName>, please enter a sentence:

If the sentence ends with a full stop then count the number of vowels in the sentence and display how many instances
of each vowel there are in the sentence as per the examples below.



If the sentence does not end with a full stop then display
Sorry <FirstName>, a sentence must end with a full stop.



Your messages must be grammatically correct. Note the use of singular and plural below.



Hints.

No loop is needed.
Check the associated presentation for using count().


Examples


Please enter your first name: dave
Dave, please enter a sentence: This is a sentence.
There is 1 a in the sentence.
There are 3 e's in the sentence.
There are 2 i's in the sentence.
There are 0 o's in the sentence.
There are 0 u's in the sentence.



Please enter your first name: dave
Dave, please enter a sentence: Hi there.
There are 0 a's in the sentence.
There are 2 e's in the sentence.
There is 1 i in the sentence.
There are 0 o's in the sentence.
There are 0 u's in the sentence.



Please enter your first name: dave
Dave, please enter a sentence: hi there
Sorry Dave, a sentence must end with a full stop.

"""

# Auth: Michael Devenport.

# Sorry no time for comments Dave, please do ask me about the code if required ;-)
# It's all off the top of my head No Goggling on this one.
# The Brief:
# I ran the vowels through a for loop counting each vowel & appending each count to a list object then it's just if else

name_prompt = "Please enter your first name: "
sentence_prompt = "{}, please enter a sentence: "
a = "There is {} a in the sentence."
a_multi = "There are {} a's in the sentence."
e = "There is {} e in the sentence."
e_multi = "There are {} e's in the sentence."
i = "There is {} i in the sentence."
i_multi = "There are {} i's in the sentence."
o = "There is {} o in the sentence."
o_multi = "There are {} o's in the sentence."
u = "There is {} u in the sentence."
u_multi = "There are {} u's in the sentence."
error = "Sorry {}, a sentence must end with a full stop."

vowels = ['a', 'e', 'i', 'o', 'u']

first_name = input(name_prompt).capitalize()
sentence = input(sentence_prompt.format(first_name))

if sentence.endswith('.'):

    vowels_count = []
    for vowel in vowels:
        vowel_count = sentence.count(vowel)
        vowels_count.append(vowel_count)

    if vowels_count[0] == 1:
        print(a.format(vowels_count[0]))
    else:
        print(a_multi.format(vowels_count[0]))

    if vowels_count[1] == 1:
        print(e.format(vowels_count[1]))
    else:
        print(e_multi.format(vowels_count[1]))

    if vowels_count[2] == 1:
        print(i.format(vowels_count[2]))
    else:
        print(i_multi.format(vowels_count[2]))

    if vowels_count[3] == 1:
        print(o.format(vowels_count[3]))
    else:
        print(o_multi.format(vowels_count[3]))

    if vowels_count[4] == 1:
        print(u.format(vowels_count[4]))
    else:
        print(u_multi.format(vowels_count[4]))

else:
    print(error.format(first_name))
