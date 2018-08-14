# True and True
'''True and True
my_guess = True
print(f"{my_guess}")
print("Is my guess correct?")
print(f"{my_guess}", True and True)
'''
import random

questions = ["True and True",
             "False and True",
             "1 == 1 and 2 == 1",
             "True and 1 == 1",
             "False and 0 != 0",
             "True or 1 == 1",
             '"test" != "testing"',
             "1 != 0 and 2 == 1",
             '"test" != "testing"',
             '"test" == 1',
             "not (True and False)",
             "not 1 == 1 and 0 != 1",
             "not 10 == 1 or 1000 == 1000",
             "not 1 != 10 or 3 == 4",
             'not "testing" == "testing" and "Zed" == "Cool Guy"',
             '1 == 1 and (not ("Testing" == 1 or 1 == 0))',
             '"chunky" == "bacon" and (not (3 == 4 or 3 == 3))',
             '3 == 3 and (not ("testing" or "Python" == "Fun"))']


def truth_guesser(boolean_statement):
    bool_in_str = str(boolean_statement)
    print(f"What do you think {bool_in_str} evaluates as?")
    my_guess = input('> ')
    if eval(boolean_statement) == eval(my_guess):
        print(f"Yep! That does evaluate to {my_guess}.")
        return(1)
    else:
        print("Nope, ", eval(boolean_statement), " is correct.")
        return(0)
    # else:
    #    print(f"I didn't understand {my_guess}. Only enter True or False.")


def quiz_taker(num_questions):
    num_questions_asked = 0
    score = 0
    print("First Question:")
    while num_questions_asked < num_questions:
        temp = truth_guesser(str(questions[random.randint(0, (len(questions)-1))]))
        num_questions_asked += 1
        score += temp
    total_score = round(float(score) / float(num_questions_asked), 2)
    print(f"You scored: {score} out of {num_questions_asked}!")
    print(f"That's {total_score}")


quiz_taker(int(input('How many questions? ')))
