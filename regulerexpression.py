#unit 3
#regular expression (re)

# string  =  r'm\w\w'
# print(string)

# r: - regulaer expression or row string
# m : - first charcter must start with m
# w : -  means any alpha numeric charcter follwed by 'm'

# string1 = 'this will printed on the \n new line'
# print(string1)

# string1 = r'this will be printed on a new \n line'
# print(string1)

#using complie method in re(regular expression)
# import re
# abc = re.compile(r'm\w\w\w\w\w')
# string1='new day of mat is matter'
# result = abc.search(string1)
# print(result.group())

#create a sub - string that have 'a' at any position and having total 3 chracters
#after it using find all
# import re
# string1 = 'atmiya atm sten string'
# result = re.findall(r'a\w\w',string1)
# print(result)

#re.split

#split(),splilt the given string into pieces according to the regular expression ad retutn the 
# piece as an elements of the list

#replacing the sub-string with the other string
# import re
# from unittest import result
# string1 = "india is the greate country"
# print(string1)
# result=re.sub('india','bharat',string1)
# print(result)

# from pickletools import string1
# import re
# from unittest import result
# string1='sun sines sooner or lastrs s'
# result = re.findall(r's[\w]*',string1)
# print(result)

