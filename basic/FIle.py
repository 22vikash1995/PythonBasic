try:
    f = open("D://Python/file/hello.txt", "rt")
    # read whole text of file
    # print(f.read())
    # read whole text of file
    # print(f.read(100))
    # read the a single line
    print("hello")
    print(f.readline())
    print(f.readline())
    # looping the text of file
    f.close()
except:
    print("Something went wrong")

# append the text in file
try:
    myfile = open("D://Python/file/hello.txt", "a")
    myfile.write("\n Helo this text is appended at end of file by vikash")
    myfile.close()
    try:
        outputfile=open("D://Python/file/hello.txt","rt")
        print(outputfile.read())
        outputfile.close()
    except:
        print("Somthing ent wrong to read the file after making changes in file")

except:
   print("Something went wrong while opening the file")



