# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
       
#         for i in range (len(nums)):
#                 for j in range (1,len(nums)):
#                     if (i!=j):
#                         if (nums[i]+nums[j]==target):
#                             o=[i,j]
#                             return o
#         return None


# class Solution:
#     def studentGrade(self, marks):
#         if (marks>=90):
#             print("Grade A")
#         elif(marks<90) and (marks>=70):
#             print("Grade B")
#         elif(marks<70) and (marks>=50):
#             print("Grade C")
#         elif(marks<50) and (marks>=35):
#             print("Grade D")
#         else:
#             print("Fail")   


# class Solution:
#     def whichWeekDay(self, day):

#         if (day > 7) or (day < 1):
#             print("Invalid")

#         elif (day == 1):
#             print("Monday")

#         elif (day == 2):
#             print("Tuesday")

#         elif (day == 3):
#             print("Wednesday")

#         elif (day == 4):
#             print("Thursday")

#         elif (day == 5):
#             print("Friday")

#         elif (day == 6):
#             print("Saturday")

#         elif (day == 7):
#             # print("Sunday")   