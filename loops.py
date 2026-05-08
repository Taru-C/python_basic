# practicing loops

# question 1: Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.

# i=1
# while i<=10:
#     print(i)
#     i+=1

# question 2: Display numbers from -10 to -1 using for loop

# for i in range(-10,0):
#     print(i)


#question 3:Display a message “Done” after successful execution of for loop

# for i in range(5):
#     print(i)
# print("Done!")    


#question 4: Calculate the sum of all numbers from 1 to N

# n= int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("The sum of numbers from 1 to", n, "is:", sum)

# question 4 : Print multiplication table of a given number

# n= int(input("Enter a number: "))
# for i in range (1,11):
#     print(n, "x", i, "=", n*i)

#question 5: Calculate the cube of all numbers from 1 to a given number

# n= int(input("enetr a number:"))
# for i in range(1, n+1):
#     print(i**3)

# questuion 6: Display numbers from a list using a loop

# a= [12, 75, 150, 180, 145, 525, 50]
# for i in a:
#     if(i>500):
#         break
#     if(i>150):
#         continue 
#     if(i%5==0):
#         print(i)

# question 7:  Count occurrences of a specific element in a list

# list1 = [10, 20, 10, 30, 10, 40, 50]
# t=10
# count=0
# for i in list1:
#     if(i==t):
#         count+=1
# print("10 occured" ,count, "times")       
    
