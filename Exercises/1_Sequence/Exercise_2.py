#request data
voted_yes = int(input("How many people voted YES: "))
voted_no = int(input("How many people voted NO: "))
voted_blank = int(input("Number of blank votes: "))
#get total
total_votes = voted_yes + voted_no + voted_blank
#divisions
percent_yes = voted_yes / total_votes * 100
percent_no = voted_no / total_votes * 100
percent_blank = voted_blank / total_votes * 100
#output
print("YES: " + str(percent_yes) + "%")
print("NO: " + str(percent_no) + "%")
print("Blank: " + str(percent_blank) + "%")

