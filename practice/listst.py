
friends = ["Bryan", "Alex", "Santi", "Renzo", "Matt"]
friends[1] = "Henry"
print(friends[1:4])

friends = ["Bryan", "Alex", "Santi", "Santi", "Renzo", "Matt"]
lucky_numbers = [5, 10, 15, 30, 50, 70]

print(friends.count("Santi"))

print(lucky_numbers.index(15))

lucky_numbers.extend(friends)
print(lucky_numbers)


lucky_numbers.append(6)
print (lucky_numbers)

lucky_numbers.remove("Matt")
print(lucky_numbers)

friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers.clear()
print(lucky_numbers)
print("Your list has been cleared.")

