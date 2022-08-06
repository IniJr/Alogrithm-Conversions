# - read the 18 numbers from where they are stored and put them in an array
# - Naturally, each number in the array is indexed 
list = [60, 61, 30, 82, 42, 44, 71, 100, 36, 16, 92, 97, 5, 64, 52, 3, 63, 34]
list = [12, 47, 78, 22, 21, 28, 25, 4, 12, 69, 45, 40, 13, 18, 51, 87, 59, 2, 19, 44, 23, 78, 38, 21, 76, 5, 5, 77, 80, 6, 87, 53, 15, 37, 80, 91, 61, 92, 72, 0, 50, 39, 47, 79, 87, 5, 46, 23, 99, 83, 85, 61, 31, 0, 23, 55, 24, 62, 19, 30, 27, 28, 36, 38, 14, 36, 54, 35, 44, 77, 22, 21, 62, 11, 62, 48, 39, 73, 2, 99, 12, 91, 9, 28, 50, 58, 86, 94, 30, 82, 25, 71, 81, 63, 20, 88, 41, 42, 98, 16, 6, 76, 59, 62, 24, 98, 24, 36, 6, 68, 72, 40, 79, 18, 58, 71, 58, 79, 60, 41, 40, 42, 64, 84, 69, 96, 0, 18, 81, 10, 73, 95, 94, 95, 83, 93, 53, 24, 11, 38, 20, 91, 19, 41, 40, 37, 93, 65, 68, 37, 89, 38, 12, 29, 76, 83, 11, 93, 27, 93, 15, 89, 4, 44, 71, 28, 58, 19, 97, 36, 97, 6, 71, 45, 45, 33, 31, 57, 97, 16]
list = [56, 69, 63, 10, 41, 57, 47, 35, 46, 91, 100, 26, 99, 35, 65, 16, 37, 100, 49, 16, 72, 92, 69, 72, 36, 8, 67, 85, 15, 19, 2, 92, 85, 65, 0, 75, 63, 56, 11, 49, 20, 76, 70, 66, 13, 61, 60, 58, 36, 57, 83, 15, 27, 19, 60, 5, 39, 34, 76, 54, 71, 90, 35, 23, 33, 51, 98, 64, 9, 94, 54, 79, 63, 73, 71, 7, 40, 35, 4, 57, 43, 15, 72, 52, 48, 24, 21, 74, 59, 23, 49, 11, 70, 6, 5, 91, 28, 0, 13, 63, 21, 71, 39, 82, 88, 55, 26, 80, 73, 63, 87, 87, 58, 5, 91, 98, 74, 21, 89, 16, 88, 55, 92, 47, 12, 25, 81, 75, 4, 28, 66, 96, 51, 30, 77, 5, 7, 75, 18, 9, 48, 18, 18, 86, 5, 44, 80, 77, 55, 32, 47, 52, 44, 21, 88, 4, 76, 3, 2, 78, 45, 3, 94, 12, 50, 92, 68, 27, 39, 29, 12, 21, 20, 94, 85, 17, 98, 87, 20, 27, 75, 16, 23, 83, 52, 70, 82, 44, 100, 53, 76, 62, 28, 8, 55, 53, 97, 48, 41, 44, 51, 20, 32, 68, 1, 26, 68, 2, 94, 29, 7, 55, 86, 24, 97, 9, 67, 1, 86, 75, 84, 2, 38, 17, 21, 25, 82, 56, 19, 88, 74, 40, 52, 2, 9, 84, 54, 53, 62, 53, 65, 82, 93, 96, 15, 15, 12, 63, 46, 56, 56, 69, 33, 78, 83, 90, 7, 51, 37, 89, 29, 84, 10, 80, 54, 86, 20, 93, 59, 64, 56, 29, 54, 43, 10, 76, 41, 2, 19, 76, 40, 5, 33, 9, 93, 86, 17, 23, 93, 67, 72, 58, 15, 24, 91, 7, 36, 97, 55, 31, 83, 79, 44, 0, 74, 92, 5, 95, 83, 69, 32, 38, 68, 87, 19, 58, 69, 78, 94, 9, 54, 12, 79, 62, 82, 57, 97, 41, 46, 52, 37, 29, 61, 65, 64, 71, 30, 64, 74, 53, 90, 29, 21, 90, 32, 27, 84, 48, 18, 86, 89, 14, 0, 20, 27, 12, 64, 85, 99, 23]

# - Create an empty array called Even
even = []

# - Iterate through list using a for loop:
#   For i in range (len(list)):
#   If list [i] mod 2=0
# - put the number in the array called Even

for i in range(len(list)):
    if list[i] % 2 == 0 and list[i] < 50:
        even.append(list[i])

# - Take the first number at the zero index, and add the next number to it (the one at the 1 index ) 
# - Get the sum
sum_of_even = even[0] + even[1]

# - loop through the array , adding the number at the next index position to the new sum 
# - Get the new sum…loop through again in the same way through each number in the array 
# - After the number at the 17th index is added, end the loop 
i = 2
while i < len(even):
    sum_of_even  = sum_of_even + even[i] 
    i = i + 1

# - print the sum of even
print("Sum of even is ",sum_of_even)

# - Take the first number at the zero index, and add the next number to it (the one at the 1 index ) 
# - Get the sum
if list[0] > 50 and list[1] > 50:
    sum = list[0] + list[1]
elif list[0] > 50:
    sum = list[0]
elif list[1] > 50:
    sum = list[1]
else:
    sum = 0

# - loop through the array , adding the number at the next index position to the new sum 
# - Get the new sum…loop through again in the same way through each number in the array 
# - After the number at the 17th index is added, end the loop 
i = 2
while i < len(list):
    if list[i] > 50:
        sum  = sum + list[i] 
    i = i + 1

# - print the final sum
sum = sum+sum_of_even
print("The final sum is", sum)

