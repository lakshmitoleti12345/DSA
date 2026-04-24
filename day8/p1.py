# s='he ll o'
# r=''
# for i in s:
#     if i  ==' ':
#         pass
#     else:
#         r+=i
# print(r)
# def remove_space(s):
#     result=''
#     for ch in s:
#         if ch==' ':
#             pass
#         else:
#             result+=ch
#     return result
# print(remove_space("He ll o"))
# def remove_vowels(s):
#     result=''
#     for ch in s:
#         if ch in 'aeiou' or ch in 'AEIOU':
#             pass
#         else:
#             result+=ch
#     return result
# print(remove_vowels('satyalakshmi'))
# def reverse_str(s):
#     result=''
#     for ch in s:
#         result=ch+result
#     return result
# print(reverse_str('HELLO'))
# def reverse_str(s):
#     result=''
#     for ch in range(len(s)-1,-1,-1):
#         result+=s[ch]
#     return result
# print(reverse_str('HELLO'))
# def reverse_spaces(s):
#     result=''
#     reverse=''
#     for ch in s:
#         if ch==' ':
#             pass
#         else:
#             result+=ch
#     for ch in range(len(result)-1,-1,-1):
#         reverse+=result[ch]
#     return reverse
# print(reverse_spaces("he ll o"))
#character type count
# s='Abc@123'
# upper=lower=special=number=0
# for ch in s:
#     if ch.islower():
#         lower+=1
#     elif ch.isupper():
#         upper+=1
#     elif ch.isdigit():
#         number+=1
#     else:
#         special+=1
# print(f""" Upper case:{upper}  
#            Lower case:{lower} 
#            number count:{number}
#            special character:{special}""")
# password=input('enter password:')
# lower=upper=special=digit=0
# if len(password)<8:
#     print('weak password')
# else:
#     for ch in password:
#         if ch.islower():
#             lower+=1
#         elif ch.isupper():
#             upper+=1
#         elif ch.isdigit():
#             digit+=1
#         else:
#             special+=1
#     if upper>=1 and lower>=1 and special>=1 and digit>=1:
#         print('strong password')
#     else:
#         print('medium password')
#print duplicate values
s='aabbccde'
seen=set()
duplicate=set()
for ch in s:
    if ch in seen:
        duplicate.add(ch)
    else:
        seen.add(ch)
print(list(duplicate))
#remove duplicates 


    
        

    
     

   




