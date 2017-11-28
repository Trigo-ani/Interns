def main():
 s = raw_input("Enter a string: ") # taking input
 l = len(s) # calculating length of the string
 count=0 # to store count of Capital letters
 for i in range(0,l):
  if(s[i]>='A' and s[i]<='Z'):
   count=count+1
 print(count)

main()


