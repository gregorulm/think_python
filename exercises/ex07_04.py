import math

def eval_loop():
    
    s = ""

    add = raw_input("> ")
    while add != "done":
        s += add
        add = raw_input("> ")

    print eval(s)

eval_loop()
    
