# ================start new game=============================
def new_game():
    pass
# ================end new game=============================


# ================start check answer=============================
def check_answer():
    pass
# ================end check answer=============================


# ================start display score=============================
def display_score():
    pass
# ================end display score=============================


# ================start play again=============================
def play_again():
    pass
# ================end play again=============================


# dictionary for questions. dictionary symbol is {}
questions ={
    #"key": "value"
    "Q1.Which of the following data types is immutable in Python?: " : "D",
    "Q2.What does the built-in function len() do in Python?: " : "B",
    "Q3.Which of the following statements is used to declare a function in Python?: " : "A",
    "Q4.Which of the following is used to represent comments in Python?: " : "B",
    "Q5.Which of the following is used to read user input in Python?: " : "B",
    "Q6.What does the pass statement do in Python?: " : "C",
    "Q7.Which method can be used to remove an item from a list in Python":"D"
}

# 2d list or list of lists

options = [
    [
        "A.List",
        "B.Dictionary",
        "C.Set",
        "D.Tuple"  
    ],
    [
        "A.Returns the last element of a list",
        "B.Returns the number of items in a container",
        "C.Reverses the order of elements in a list",
        "D.Removes the first element from a list"  
    ],
    [
        "A.def",
        "B.func",
        "C.define",
        "D.function"  
    ],
    [
        "A.// comment",
        "B.# comment",
        "C./* comment */",
        "D.<!-- comment -->"  
    ],
    [
        "A.readline()",
        "B.input()",
        "C.get_input()",
        "D.user_input()"  
    ],
    [
        "A.Terminates the loop",
        "B.Skips to the next iteration of a loop",
        "C.Allows for an empty block of code",
        "D.Breaks out of a loop or switch statement"  
    ],
    [
        "A.delete(item)",
        "B.remove(item)",
        "C.discard(item)",
        "D.pop(index)"  
    ],
]