name = input("What is your name?: ")
time1 = input("Give me a time:")
time2 = input("Give me another time: ")
pronoun = input("Give me a pronoun: ")
noun1 = input("Give me a noun: ")
noun2 = input("Give me a noun: ")
verb = input("Give me a (Past Tense) verb:")

# actual sentence
madlib = f"Hi! My name is {name}. I woke up at {time1} to go to school, but schools starts at {time2}. \
After walking my {pronoun} I decided to go get ready! I changed into my favourite outfit- a dressy pant \
and a {noun1}. Then it was time for me to eat my go to breakfast which is a {noun2}. I then {verb} to school."

print(madlib)