city1n2temp = [
    [24, 26, 27, 25, 21, 29, 27,],
    [32, 30, 29, 31, 33, 35, 34,]
]

print("Total for each row:", "\n", sum(city1n2temp[0]), "\n", sum(city1n2temp[1]))
print("Average for each row:", "\n", average_city1 := sum(city1n2temp[0]) / len(city1n2temp[0]), "\n", average_city2 := sum(city1n2temp[1]) / len(city1n2temp[1]))
print("Maximum of the entire data set:", "\n", max(max(city1n2temp[0]), max(city1n2temp[1])))
print("Minimum of the entire data set:", "\n", min(min(city1n2temp[0]), min(city1n2temp[1])))
