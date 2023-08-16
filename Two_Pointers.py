# Problem Valid Palindrome 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
        
#         while l < r:
            
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
                
#             if s[l].lower() != s[r].lower():
#                 return False
            
#             l += 1
#             r -= 1
            
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )


# Problem  Two Sum II - Input Array Is Sorted

# lst = [1,3,4,5,7,11]
# target = 9

# l,r = 0, len(lst)-1

# while l < r:
#     curSum = lst[l] + lst[r]
    
#     if curSum > target:
#         r -= 1
        
#     elif curSum < target:
#         l += 1
        
#     else:
#          print([l+1, r+1])



# Problem  Container With Most Water

# height = [1,8,6,2,5,4,8,3,7]

# l,r = 0, len(height) - 1
# result = 0

# while l < r:
#     area = (r - l) * min(height[l], height[r])
#     result = max(result,area)
    
#     if height[l] < height[r]:
#         l +=1
        
#     else:
#         r -= 1
        
# print(result)

