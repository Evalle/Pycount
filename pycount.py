x = ["fuzz", "fizz", "fkzz"]
def fizz_count(x):
    counter = 0
    for word in x:
        if word == "fizz":
            counter = 1 + counter
    return counter
