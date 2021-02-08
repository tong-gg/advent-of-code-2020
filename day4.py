def generateData(raw_data):
    i = 0
    data = [{}]
    for line in raw_data:
        line = line.strip()
        if(line != ""):
            for val in line.split(" "):
                person_data = val.split(":")
                # print(person_data)
                if(not any(data[i])):
                    data[i] = {
                        person_data[0] : person_data[1]
                    }
                else:
                    data[i][person_data[0]] = person_data[1]   
        else:
            i += 1                   
            data.append({}) 
    return data

# PART 1
# def checkField(data):
#     validField = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
#     for field in validField:
#         if(field not in data):
#             return 0
#     return 1        

def filterPassport(data):
    validField = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in validField:
        if(field not in data):
            return False
    return True

def checkField(field):
    validField = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validPassport(data):
    count = 0
    filteredList = []
    for passport in data:
        if(filterPassport(passport)):
            filteredList.append(passport)
            
    return count    
    

raw_data = open("input_data/inputd4.txt", "r")
data = generateData(raw_data)

# print(len(data))
total = validPassport(data)
print(total) 
raw_data.close()