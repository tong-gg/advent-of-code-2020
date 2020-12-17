def wordCount(minMax, word, password):
    count = 0
    min_max_range = minMax.split("-")
    for letter in password:
        if(letter == word):
            count += 1
    if(count >= int(min_max_range[0]) and count <= int(min_max_range[1])):
        return 1        
    return 0

def validPosition(minMax, word, password):
    count = 0
    min_max_range = minMax.split("-")
    word_list = list(password)
    count += 1 if word_list[int(min_max_range[0]) - 1] == word else 0
    count += 1 if word_list[int(min_max_range[1]) - 1] == word else 0
    if(count == 1):
        return 1
    else:
        return 0   


raw_data = open("input_data/inputd2.txt", "r").read().split("\n")


result = 0
for data in raw_data:
    res = data.split(" ")
    # PART 1 each password reach min and max range
    # result += wordCount(res[0], res[1].strip(":"), res[2])

    # PART 2
    result += validPosition(res[0], res[1].strip(":"), res[2])
print(result)





