Problem Statement : Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array.

Input : arr[] = {5, 5, 10, 100, 10, 5}
Output : 110
  
Code : 
  
list1 = list(map(int, input().split(',')))
list2 = []
for i in range(len(list1)-1):
    a = list1[i] + list1[i+1]
    list2.append(a)
print(max(list2))
