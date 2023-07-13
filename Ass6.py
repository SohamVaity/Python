def ds(name, roll_no):

    lst = [name,roll_no]
    tup = (name,roll_no)
    sets = {name,roll_no}
    dic = {
        "Name":name,
        "Roll_no":roll_no
        }

    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    newName = str(input("Enter Name : "))
    newRoll_no = int(input("Enter Roll number : "))
    
    lst[0] = newName
    lst[1] = newRoll_no
    tup = tuple(lst)
    set.update(set(lst))
    dic["Name"] = newName
    dic["Roll_no"] = newRoll_no
    
    print("Updated data structures : ")
    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    print("Deleting the data structures...")
    del lst,tup,sets,dic
    print("Data Structures deleted.")
    print("Bye")

# Storing Data

ds("Soham Vaity",106)