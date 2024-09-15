#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)



#Task 2: Venue Selection
if attendees > 100:
    print("Recommendation: Audio system")
elif attendees >= 50:
    print("Recommendation: Projector")
else:
    print("No  equipment needed")    

#Task 3: Catering Choices
vegetarian = input("Do you want vegetarian food? (yes/no)\n ").lower()

if vegetarian == "yes":
    print("Recommendation: Veggie Delight Caterers")
else:
    print("Recommendation: Gourmet Meals Caterers")