#pattern#

word=input("tell us word to print: ")

for row in range(len(word)):
    for col in range(len(word)):
        print(word[col],end=" ")
    print()

#folid pattern
'''
for row in range(len(word)):
     for col in range(row+1):
         print(word[col],end=" ")
     print()
'''''

#folid pattern2
     
for row in range(len(word),0,-1):
    for col in range(row):
        print(word[col],end=" ")
    print()
  
