def magic_date():
    date = input("Podaj date " )
    months = {"January": 1,
    "February":2,
    "March":3,
    "April":4}
    
    
    separeted_date = date.split(" ")
    numer = months[separeted_date[0]]
    dzien = int(separeted_date[1])
    rok = int(separeted_date[2][2::])
    if numer * dzien == rok:
        return " to twoj szczesliwy day lololololo lo"
    else:
        return " to twoj chujowy day"
    
print(magic_date())


'''A magic date is a date where the day multiplied by the month is equal to the two digit
#year. For example, June 10, 1960 is a magic date because June is the sixth month, and
#6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise.'''