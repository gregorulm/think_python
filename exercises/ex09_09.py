def reversed_ages():

    age_differences = [i for i in range(14, 45)]

    result = ""
    for delta in age_differences:
        temp = ""
        for i in range(120):
            if str(i).zfill(2) == str(i + delta)[::-1]:
                temp += str(i).zfill(2) + " " + str(i + delta) + "\n"
        if len(temp) > len(result):
            result = temp

    return result

print reversed_ages()
