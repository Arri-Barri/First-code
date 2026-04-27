open('database.py','r')

for i in range(len(forename)):
    email = forename[i]+surname[i]+"@uni.ac.uk"
    password = course[i]

    with open('output'+str(i)+'.txt','w') as p:
        output = email,password
        p.write(output)