f=open("H:\\funny.txt", "r")
f_out = open("H:\\funny_out.txt", "w")
for lines in f:
    token = lines.split(' ')
    f_out.write("WordCount: " + str(len(token)) + ' ' +  lines)
f.close()
f_out.close()
