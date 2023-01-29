import os
import re

re_pat = r'[A-z]+[(]'
PATH = os.path.dirname(os.path.abspath(__file__))
check_list = []
final_list = []
# file_path = PATH+'/neo_initializer.py'
file_path = PATH+'/neo_scrapes.py'

def python_function_scraper(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            function_list = re.findall(re_pat, line)
            line.strip()
            line_split = line.split(' ')
            for word in line_split:
                for re_function in function_list:
                    if re_function in word and word not in check_list:
                        check_list.append(word)
            for word in check_list:
                while True:
                    if "(" in word:
                        new_function = word.split('(')[0]
                        if new_function not in final_list:
                            final_list.append(new_function)
                        word = '('.join(word.split('(')[1:])
                    else:
                        break
    return check_list, final_list

# print(function_list)
check_list, final_list = python_function_scraper(file_path=file_path)
print(check_list)
print(final_list)