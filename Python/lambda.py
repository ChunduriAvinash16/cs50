people=[
    {"Name":"Avinash","Reg_no":6006},
    {"Name":"Naveen","Reg_no":6032},
    {"Name":"Siddhart","Reg_no":6011},
    {"Name":"Akash","Reg_no":6001}
]


people.sort(key=lambda people:people["Name"])

print(people)