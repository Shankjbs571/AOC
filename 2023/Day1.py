file1 = open("2023\D01\in.txt","r")
#print(file1.read())

ins=file1.read()
ins=ins.split("\n")

#print(ins)
nums=['one','two','three','four','five','six','seven','eight','nine','zero']
all_number=[]
for ins in ins:
    digit=''
    fl=''
    for c in ins:
        if c in '1234567890':
            digit+=c
    
    fl=digit[0]+digit[-1]
    all_number.append(int(fl))
    

print(all_number)
sum=0
for i in all_number:
    sum+=i

print(sum)
# ins='56fiven58inenqpfrv'
# digit=''
# fl=''
# for c in ins:
#         if c in '1234567890':
#             digit+=c

# fl=digit[0]+digit[-1]
# print(fl)
file1.close()
# inpt=inpt.split("\n")
# print(inpt)


# import re

# def spelled_digits_to_numbers(text):
#     # Define a dictionary to map spelled-out words to numerical values
#     word_to_number = {
#         'zero': '0',
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9'
#     }

#     # Define a regular expression pattern to match consecutive words representing numbers
#     pattern = r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)+\b'

#     # Use re.sub to replace spelled-out words with their numerical values
#     result_text = re.sub(pattern, lambda match: ''.join(word_to_number[word.lower()] for word in re.findall(r'\b\w+\b', match.group(0))), text, flags=re.IGNORECASE)

#     return result_text

# # Example usage:
# input_string = "1eightseven89"
# converted_string = spelled_digits_to_numbers(input_string)

# print("Original string:", input_string)
# print("Converted string:", converted_string)


