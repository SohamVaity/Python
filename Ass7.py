def fileHandle(file = "Ass7.txt"):

    try:
        f = open(file,"a")
    
        f.writelines("Name- Soham Vaity, Roll number - 106, Class - CO3")
        
        f.close()
        f = open(file,"r") #r to read
        print(f.readlines())
    except IOError: pass

fileHandle("Ass7.txt")