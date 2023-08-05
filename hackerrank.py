# n = int(input()) 
# for i in range (0,n):
#     print(i*i)

# num = "geeksforgeeks"
# for i in num :
#     if i=='e' or i =='s':
#         continue
#     print(i)


# str ="Nor,weg,ian Bl,ue"
# print(str.split(','))
# print(str[0::2]) #every 2nd aplbhabet is printed (split mehtod)


# s = "Let's take LeetCode contest"
# s1=s.split()
# s2=[]
# for i in s1:
#     s2.append(i[::-1])
#     print(s2)


# #sequence is defined as an ordered set of items
# today ="friday"
# print("day" in today) 


# converting int to string
# age =20
# print("my age is "  + str(age) + " years")
# print ("vipul " + f"is {age} years old")


# print("my age is {0} years".format(age)) #zero means replacement index

# #string formatting
# print("there are minimum {0} days in {1}, {2}, {3} , {4}".format(30, "jan","feb" ,"march", "april"))

# def addition(num1, num2):
#     num3 = num1 + num2
#     print(num3)
#     return num3

# addition(2,2)


# str = "HackerRank.com"
# str1 = ""
# for char in str:
#     if str.islower():
#         str1+=str.upper()
#     else :
#         str1+=str.lower()    
# print(char)


# tree1 ="this is a mango tree"
# tree2 ="this is a mango tree"

# if tree1==tree2:
#     print("the trees are same")
# else:
#     print("the trees are not same")    


# not working see later

# str="ABCDCDC"
# sub="CDC"
# for letters in str:
#     count=str.count(sub)

#     print(count)


# name = input("Enter ur name")
# age = int(input("Enter ur age"))

# if 18<=age<31:
#     print("welcome to holiday,{0}".format(name))
# else:
#     print("sorry")


# Finding capital letters in a string

# str = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# str1=""
# for char in str:
#     if char.isupper():
#         str1+=char
# print(str1)


# for i in range(0, 100, 7):
#     print(i)
#     if i>0 and i%11==0:
#         break


# USING CHOICE FUNCTION

# print("1 :Learn Python")
# print("2 :Learn Java")
# print("3 :Go swimming")
# print("4 :Have dinner")
# print("5 :Go to bed")
# print("6 :Exit")

# while True:
#     choice =input()

#     if choice=="0":
#         print("Exit")
#     elif choice in "12345":
#         print("your choice".format(choice))


# str="G()(al)"
# str1=""
# i=0
# while i<len(str):
#     if str[i]=='G':
#         str1+="G"
#         i+=1
#     elif str[i]=='(' and str[i+1]==')':
#         str1+="o"
#         i+=2
#     elif str[i]=='(' and str[i+1]=='a' and str[i+2]=='l' and str[i+3]==')':
#         str1+="al"
#         i+=3
# print(str1)


# computer_parts=["computer", "monitor", "mouse", "printer"]
# for i in computer_parts:
#     print(i)

# STRINGS ARE IMMUATBLE WHEREAS LISTS ARE MUTABLE 
# I.E. THERE CONTENT CAN BE CHNAGED
# USE ID FUNCTION TO CHEC  

# ENUMERATE FUNCYION IS USED TO FIND ITEMS IN A LIST
#  AND RETURN IT AND ALSO RETURN ITS INDEX NUMBER


# word1=["ab", "c"]
# word2=["a", "bc"]
# # print(word1)
# # print(word2)

# str1="".join(word1)
# str2="".join(word2)

# if str1==str2:
#     print(True)
# else:
#     print(False)    


# Need to fix this code not working properly 

# s = "Hello how are you Contestant"
# k = 4
# s1=list(s.split())
# str = ""

# i=0
# while i<k:
#     str+=s1[i]
#     i+=1
# print(str)


# s=["a","abc","bc","d"]
# s1=""
# print (s1.join(s))
# word = "abc"
# count=0
# if s in word:
#     count+=1
#     print(count)

# s="book"
# str1="" 
# str2=""
# for i in range(len(s)//2):     
#     str1+=s[i]
# print(str1)

# for i in range(len(s)//2,len(s)):
#     str2+=s[i]
# print(str2)

# count1=0
# vowels = ["a", "e", "i", "o", "u" ,"A", "E", "I","O","U"]
# for i in range(len(str1)):
#     if str1[i] in vowels:
#         count1 += 1   
#         print(count1)


# count2=0
# for i in range(len(str2)):
#     if str2[i] in vowels:
#         count2 += 1   
#         print(count2)

# if count1==count2:
#     print(True)


# patterns = ["a","abc","bc","d"]
# word = "abc"
# count=0
# for i in patterns:
#     if i in word:
#         count+=1
# print(count)


# word1 = "abc"
# word2 = "pqr"
# x=len(word1)+len(word2)
# res=''
# for i in range(x):
#     res += word1[i] + word2[i]
#     print (res + word1[i+1:] + word2[i+1:])


# difference between sort and sorted 
# sorted function assigns the values to a new variable
# and sort arranges the numbers in that variable only

# a=[1,6,5,3,2,9,7]
# a.sort()
# print(a)

# x=sorted(a)
# print(x)
# l3=[]
# l2=[]
# l1=[]

# for i in word1:
#     l1+=word1
#     print(l1)
#     break

# for i in word2:
#     l2+=word2
#     print(l2)
#     break

# print(len(l1+l2))

# for i in range(len(l3)):
#     l3+=l1[i]+l2[i]
#     print(l3)    


# counting percentage of a letter in a word

# s = "foobar"
# letter = "o"
# count=0
# for i in s:
#     if i==letter:
#         count+=1
# print(count)

# percentage=(count*100)//len(s)
# print(percentage)

# even = [2,4,6,8]
# odd = [1,3,5,7]
# numbers =[even,odd] 
# print(numbers)      

# for number_list in numbers:
#     print(number_list)
#     for value in number_list:
#         print(value)


# import array as arr
# a=arr.array('i',[2,2,1,2])
# for i in range(0,len(a)):
#     print(a[i],end=" ")

# print("length of array is" ,len(a))

# a.insert(1,4) #insert will add elemnent at desired position
# a.append(5) #append will add mehtod at last of an array
# for i in a:
#     print(i,end=" ")

# print("length of array after insertion is" ,len(a))


# tuples are immutable like strings
# but lists are mutable i.e. they can be changed
# TUPLES USES LESS MEMORY THAN LISTS

# TUPLE IMPLEMENTATION

# name ="VIPUL"
# age=20

# print((name, "is", age ,"years old"))


# PROGRAM TO TAKE USER INPUT FOR ARRAY AND LIST
# a=[]
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    a.append(l)
# print(a)


# albums = [
#     ("Welcome to my Nightmare", "Alice Cooper", 1975,
#      [
#          (1, "Welcome to my Nightmare"),
#          (2, "Devil's Food"),
#          (3, "The Black Widow"),
#          (4, "Some Folks"),
#          (5, "Only Women Bleed"),
#      ]
#      ),
#     ("Bad Company", "Bad Company", 1974,
#      [
#          (1, "Can't Get Enough"),
#          (2, "Rock Steady"),
#          (3, "Ready for Love"),
#          (4, "Don't Let Me Down"),
#          (5, "Bad Company"),
#          (6, "The Way I Choose"),
#          (7, "Movin' On"),
#          (8, "Seagull"),
#      ]
#      ),
#     ("Nightflight", "Budgie", 1981,
#      [
#          (1, "I Turned to Stone"),
#          (2, "Keeping a Rendezvous"),
#          (3, "Reaper of the Glory"),
#          (4, "She Used Me Up"),
#      ]
#      ),
#     ("More Mayhem", "Imelda May", 2011,
#      [
#          (1, "Pulling the Rug"),
#          (2, "Psycho"),
#          (3, "Mayhem"),
#          (4, "Kentish Town Waltz"),
#      ]
#      ),
# ]

# print(albums[1][3][5][1])  
# print(albums[2][2])       
# print(albums[3][3][3][0])  
# print(albums[2][3][1])     

# two sum
# nums = [3,2,3]
# target = 6
# list=[]
# for i in range(0,len(nums)-1):
# for j in range(i+1,len(nums)):
#     i!=j
#     if nums[i]+nums[j]==target:
#         list=i,j
#         print(list)


# count good triplets

# arr = [3,0,1,1,9,7]
# a = 7
# b = 2
# c = 3
# count=0
# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#          for k in range(j+1,len(arr)):
#             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                 i!=j!=k
#                 count+=1
# print(count)


# nums = [1,2,3,4,5,6,7,8,9,0]
# for i in range(0,len(nums)):
#     if i % 10==nums[i]:
#         print(i)

# print("-1")


# s = "Hello how are you Contestant"
# a=s.split(" ")
# print(a)
# k = 4
# str=""
# for i in range(0,len(a)):
#     if i<k:
#         str+=a[i]+" "
# print(str.rstrip)

# nums=[5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
# k = 7
# count=0
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if i<j and nums[i]==nums[j] and (i*j)%k==0:
#             count+=1
# print(count)        


# title = "capiTalIze tHe titLe"
# title = title.split()
# for i in range(len(title)):
#     if len(title[i]) < 3:
#         word = word + title[i].lower() + " "
#     else:
#         word = word + title[i].capitalize() + " "
# print(word.rstrip())


# print(str)
# str1=" "
# ans=""
# # print(str1.join(str))
# for i in range(0,len(str)):
#     if (len(str[i])>2):
#         ans+=str[0:1]. + str[1].lower +" "
#     else :
#         if len(str[i])<=2:
#             ans+=str[i].lower()+" "


# print(ans)


# rectangles = [[5,8],[3,9],[5,12],[16,5]]
# str=[]
# for list in rectangles: 
#         if list[0]<list[1]:
#             str.append(list[0])
#         else:
#             str.append(list[1])
# print(str)

# count=0
# num=str[0]
# for i in str:
#     freq=str.count(i)
#     if freq>count:
#         count=freq
#         num=i

# print("most frequent no is" , num)


# sentence = "leetcode exercises sound delightful"
# str=sentence.split(" ")


# for i in range(0,len(str)):
#     if (str[len(str)-1][-1])==str[0][0]:
#         print("Circular")
#     else:
#         print("Not Circular")


# for i in range(0,len(str)-1):
#     if (str[i][-1])==str[i+1][0]:
#         print("Circular")
#     else:
#         print("Not Circular")

# sentence = "leetcode exercises sound delightful"
# str=sentence.split(" ")

# value=str[0]
# print(value)

# str1=[]

# str1=str[:] 
# print(str1)

# str1=str.insert(3, value)

# # str1=str.append(str[0])
# print(str1)


# str= ["alic3","bob","3","4","00000"]

# for i in str:
#     if i.isdigit():
#         print(len(i))

# s="0000"
# if s.isdigit():
#     print("true")
# else:
#     print("false")    


# s = "is2 sentence4 This1 a3"
# for i in s.split():
#     # arr = [i[-1] + i[:-1]]

#     # arr.sort()
#     print(s) 


# ans = ""
# for i in arr:
#     ans += i[1:] + ' '
# print(ans[:-1])

# arr=[3,0,1]
# n=len(arr)+1
# print(n)
# for i in range(n):
#     if i not in arr:
#         print(i)


# ROTATING ARRAY
# arr=[1,2,3,4,5]
# print(arr[2:])
# print(arr[:2])


# s = "11111222223"
# k = 3
# for i in range(0, len(s), k):
#     output = (s[i:i+k])

#     print(output)

# res=""
# for i in range(123,97):
#     res+=chr(i)
# print(str(res))


# str=[1,1,2,2,2,3]
# count=0
# num=str[0]
# for i in str:
#     freq=str.count(i)
#     if freq>count:
#         count=freq
#         num=i

# print("most frequent no is" , num)


# from collections import Counter

# def top_two_frequent_numbers(arr):
#     counter = Counter(arr)  # Count the occurrences of each number in the array
#     most_common = counter.most_common(2)  # Get the top two most common numbers

#     # Extract the numbers from the most_common list
#     top_two_numbers = [number for number, _ in most_common]

#     return top_two_numbers

# # Example usage
# arr = [1, 2, 3, 2, 2, 3, 4, 4, 4, 4]
# result = top_two_frequent_numbers(arr)
# print(result)



# GROUP ANAGRAMS
# anagram_groups ={}
# strs=["eat","tea","tan","ate","nat","bat"]
# for i in strs:
#     word = " ".join(sorted(i))
#     if word in anagram_groups:
#         anagram_groups[word].append(i)
#     else:
#         anagram_groups[word]=[i]

# print(list(anagram_groups.values()))



# strs= ["abba","baba","bbaa","cd","cd"]
# arr=[]
# for i in strs:
#     word = "".join(sorted(i))
#     arr.append(word)
#     print(arr)
# print(set(arr))


# n=19
# while n>0:
#     temp =0
#     while n>0:
#         temp+=(n%10)**2
#         n//=10
# print(temp)
