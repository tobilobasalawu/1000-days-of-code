def parse_int(string):
    # Dictionaries for number words
    num_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90
    }

    # Handling larger number words
    larger_units = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }

    # Process the input string, remove any 'and', split words by spaces
    words = string.replace(" and ", " ").split()

    result = 0
    current = 0  # To accumulate numbers within larger units

    for word in words:
        if word in num_words:
            current += num_words[word]
        elif word in larger_units:
            if word == "hundred":
                current *= larger_units[word]
            else:
                current *= larger_units[word]
                result += current
                current = 0
    return result + current

#print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))  # 783919
