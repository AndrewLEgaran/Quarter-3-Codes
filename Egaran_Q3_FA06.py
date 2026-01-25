Scholar = {}

scholarname = input("Enter scholar's name: ")
scholarage = int(input("Enter scholar's age: "))
scholarfavsubject = input("Enter scholar's favorite subject: ")

Scholar["Name"] = scholarname
Scholar["Age"] = scholarage
Scholar["Favorite Subject"] = scholarfavsubject

print("Student Record:")
for key, value in Scholar.items():
    print(key + ":", value)