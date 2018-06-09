from lab6_2_1_q1 import mark_problem


def student_check():
    """
    playground.py is importing lab6_2_1_q1 & which holds a function were interacting with from a function in this file
    """
    c = True
    while c:
        i = input("Enter your student id: ")
        if not i.isnumeric():
            print("Something went wrong, please try again.")
        else:
            commit = input("Valid id, lets continue shall we.. press Y to precede: ").lower()
            if commit == 'y':
                mark_problem()
            else:
                print("Exiting program")
                c = False


# student_check()
