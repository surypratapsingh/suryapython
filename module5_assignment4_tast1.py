
file=open("sample.txt",'r')
reading_fileline1=file.readline()
reading_fileline2=file.readline()
print("reading file : ")
print("line 1: ",reading_fileline1.strip() )
print("line 2: ", reading_fileline2.strip() )
file.close()
