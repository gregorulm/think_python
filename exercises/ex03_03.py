def right_justify(s):
    padding = 70 - len(s)
    return " " * padding + s

print right_justify("python")
