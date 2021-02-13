##Default Argument

#Variable-length Argument

def disaply(name,course="B.Tech",*fav_subjects):
    print(name,course)
    print(fav_subjects)
    for i in fav_subjects:
        print(i,end=" ")
disaply("Avinash")
disaply("Akash","BBA","Business")



