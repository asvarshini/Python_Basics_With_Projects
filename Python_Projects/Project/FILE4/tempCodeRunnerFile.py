while True:
    print("1.Add marks ")
    print("2.Veiw marks")
    print("3.Exit")
    choice=int(input("Enter Your choice"))
    if choice==1:
        f1=open("Marks.txt","w")
        name=input("Enter the name of the student")
        mark=int(input("Enter the marks of student"))
        f1.write(f"{name}:{mark}\n")
    elif choice ==2:
        try:
            f2=open("Marks.txt",'r')
            con=f2.read()
            print(con)
        except Exception as e:
            print("File is not found")
    else:
        break