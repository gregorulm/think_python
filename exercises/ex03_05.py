def grid(n):
    filled = "+----"
    empty = "|    "
    grid = ""

    for i in range(n):
        grid += filled * n + filled[0] + "\n"
        grid += 4 * (empty * n + empty[0] + "\n")
        
    grid += filled * n + filled[0] + "\n"
    
    return grid


print grid(2)
print grid(4)
    
