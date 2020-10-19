lunch = input("What did you eat for lunch: ")
sandwich_count = lunch.count("sandwich")
first_position = lunch.find("sandwich")
lunch_minus_first = lunch[first_position+8:]
second_position = lunch_minus_first.find("sandwich")

if sandwich_count >= 2:
    print(lunch_minus_first[0:second_position])