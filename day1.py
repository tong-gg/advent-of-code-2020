raw_data = open("input_data/inputd1.txt", "r").read().splitlines()
data = [int(x) for x in raw_data]

# PART 1
# for i in range(len(data)):
#     diff = 2020 - data[i]
#     for j in range(len(data)):
#         if(data[j] == diff):
#             print(data[i] * data[j])

# PART 2
for i in range(len(data)):
    for j in range(len(data)):
        first_sum = data[i] + data[j]
        if(first_sum < 2020):
            for k in range(j, len(data)):
                second_sum = first_sum + data[k]
                if(second_sum == 2020):
                    print(data[i] * data[j] * data[k])