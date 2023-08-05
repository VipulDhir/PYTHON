# arr = [-2,-1,-1,1,2,3]
# count1=0
# count2=0
# for i in range(0,len(arr)):
#     if arr[i]<0:
#         count1+=1
#     elif arr[i]>0:
#         count2+=1
# print(count1)
# print(count2)

# if count1>count2:
#     print(count1)
# elif count1==count2:
#     print(count1)
# else:
#     print(count2)



# x = 3
# y = 4
# points = [[1,2],[3,1],[2,4],[2,3],[4,4]]


# valid=[]
# for i in points:
#     if i[0]==x or i[1]==y:
#         valid.append(i)
# dist=[]
# if len(valid) == 0:
#    print("-1")
# else :
#     for i in valid:
#         dist.append(abs(x - i[0]) + abs(y - i[1]))
#     if valid[dist.index(min(dist))] in valid:
#         print(points.index(valid[dist.index(min(dist))]))

# number = "1-23-45 6"
# number=number.replace(" ","").replace('-',"")
# print(number)
# print(len(number))
# ans = []
# for i in range(0, len(number), 3): 
#     print(number[i])



# s = "PPALLP" 
# s=list(s)
# print(s)
# for i in range(0,len(s)):
#     abs_count=s.count('A')
# print(abs_count)

# late_count=0
# for i in range(0,len(s)-2):
#     if s[i]==s[i+1]==s[i+2]=='L':
#         late_count+=1
# print(late_count)

# if late_count==0 and abs_count<2:
#     print("true")
# else:
#     print("false")


# s = [-100,-98,-1,2,3,4]
# s.sort()
# sum=[]
# print(s)
# # for i in range(0,len(s)-2):
# #     product=s[i]*s[i+1]*s[i+2]
# #     sum.append(product)
# # print(sum)

# # print(max(sum))

# nums = [11,7,2,15]
# count=0
# mn = min(nums)
# print(mn)
# mx = max(nums)
# print(mx)
# for i in nums:
#     if i > mn and i < mx:
#         print(i)
#         count += 1
# print(count)

# text= "  this   is  a sentence "
# words=text.split()
# for i in range(0,len(text)):
#         spc_count=text.count(" ")
       
# print(spc_count)
# print(len(words))

# even_spaces= spc_count // (len(words)-1)
# print(even_spaces)



# candyType = [6,6,6,6]
# total_candy=len(candyType)//2
# print(total_candy)

# candies=set(candyType)
# print(candies)
# if len(candies)==total_candy:
#         print(len(candies))
# elif len(candies)>total_candy:
#         print(total_candy)
# else :
#         print(len(candies))




# strs = ["eat","tea","tan","ate","nat","bat"]

# strs_table = {}

# for string in strs:
#     sorted_string = ''.join(sorted(string))
#     print(sorted_string)

#     if sorted_string not in strs_table:
#         strs_table[sorted_string] = []
#         print(strs_table)

#     strs_table[sorted_string].append(string)
#     print(list(strs_table.values()))


# import string
# s = "A man, a plan, a canal: Panama"
# new_s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ","").lower()
# print(new_s)

# rev = new_s[::-1]
# if new_s == rev:
#     print("false")
# else:
#     print("true")




# s = "{[()]}"
# while '()' in s or '[]'in s or '{}' in s:
#     s = s.replace('()','').replace('[]','').replace('{}','')
# if len(s)==0:
#     print("true")
# else:
#     print("false")


# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = sorted(set(nums))
# print(nums)

# if len(nums)==0:
#     print("0")
            
# count=0
# for i in range(1,len(nums)):
#     if nums[i]==nums[i-1]+1:
#         count+=1
# print(count + 1)



# n = int(input("enter no of testcases"))
# x= int(input("enter income"))

# k =2**x
# print(k)
# for i in range(0,n):
#     k=(k-0.5*k)
# print(int(k))


# product of array except self
# nums = [1,2,3,4]
# multiply=1
# for i in nums:
#     multiply = multiply * i

# print(multiply)

# left = [1] * len(nums)
# right = [1] * len(nums)
# final = [1] * len(nums)

# for i in range(1,len(nums)):
#     left[i]=left[i-1]*nums[i-1]

# for i in range (len(nums)-2, 0 ,-1):
#     right[i]=right[i+1]*nums[i+1]

# for i in range(len(nums)):
#     final[i] = left[i] * right[i]



# prices = [7,1,5,3,6,4]
# profit = [0] * len(prices)

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         profit[i] = max(profit[i], prices[j] - prices[i])
#         print(profit[i])

#     max_profit = max(profit)

# print(max_profit)

# 1876. Substrings of Size Three with Distinct Characters
# s = "xyzzaz"
# pairs=[]
# for i in range(len(s) - 2):
#     pair = s[i:i+3]
#     pairs.append(pair)
# print(pairs)

# unique=[]
# for i in pairs:
#     if len(set(i))==len(i):
#         unique.append(i)
# print (len(unique))


# Container With Most Water
# height = [1,8,6,2,5,4,8,3,7]
# i=0
# j=len(height)-1
# maximum=0
# while j>i:
#     breadth=abs(j-i)
#     area = breadth * min(height[i],height[j])
#     maximum= max(area , maximum)
#     if height[i] > height[j]:
#         j -=1
#     else:
#         i +=1
# print(maximum)


# 167 SORTED ARRAY INPUT 2
# numbers = [2,3,4]
# target = 6
# for i in range(0, len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             arr.append(i) 
#             arr.append(j) 

# print(arr)

# for i in range(len(arr)):
#     arr[i]+=1

# print(arr)

# OR

# arr = []
# left = 0
# right = len(numbers) - 1

# while left < right:
#     current_sum = numbers[left] + numbers[right]

#     if current_sum == target:
#         arr.append(left)
#         arr.append(right)
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1

# for i in range(len(arr)):
#     arr[i] += 1

# print(arr)



