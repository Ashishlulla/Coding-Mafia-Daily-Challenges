Problem Statement : Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
  
Input : "Let's take coding club contest"
Output : s'teL ekat gnidoc bulc tsetnoc
  
Code :
  
str = "Let's take coding club contest"
arr = [i[::-1] for i in str.split()]
print(" ".join(arr))
