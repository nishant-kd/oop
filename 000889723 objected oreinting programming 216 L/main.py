from facilityclasses import Facility

print("The Alberta Hospital (AH) Management system is pleased to have you.")
A = input(
    "Choose from the available options, or press 0 to stop, as appropriate: \n1-Doctors\n2-Facilities\n3- Laboratories\n4-Patients\n")
if A == '2':
    i = 0
while i != 3:
    choice = input(
        "Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")
    if choice == '1':
        Facility.displayFacilities(Facility)
        print("Back to the prevoius Menu")
    if choice == '2':
        Facility.addFacility(Facility)
        print("Back to the prevoius Menu")
    if choice == '3':
        print("Back to the prevoius Menu")
        quit()
else:
    quit()
