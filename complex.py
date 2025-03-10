
# count nested levels
def count_nested_levels(tree, target_id, level=1):
    for node in tree:# access tree 
        if node == target_id:#condition
            return level
        else:#look deeper
            found = count_nested_levels(tree[node], target_id, level + 1) 
        if found != -1:#found condition
            return found
    return -1# not found condition

# Return the list of file paths.
def list_files(tree, path=""):
    file_list = []
    for node in tree:# access tree
        if tree[node] is None:# condition
            file_list.append(path + "/" + node)
        else:# look deeper
            file_list.extend(list_files(tree[node], path + "/" + node))
    return file_list

# return the reversed string by recursively reversing the substrings inside.
def BOOTreverse_string(s):
    if len(s) == 0:
        return s
    return BOOTreverse_string(s[1:]) + s[0]

def MYreverse_string(s):
    reverse = ''
    subS = ''
    for i in range(0, len(s)):
        if i == len(s) - 1:
            reverse += s[i] + MYreverse_string(subS) 
        else:
            subS += s[i]
    return reverse

# another reursive example
def find_longest_word(document, longest_word=""):
    if document == '':
        return longest_word
    word_lst = document.split(' ')
    if len(word_lst[0]) > len(longest_word):
        longest_word = word_lst[0]
    sub_s = ' '.join(word_lst[1:])
    return find_longest_word(sub_s, longest_word)

#diction input without .update({})
def css_styles(initial_styles):
    styles = initial_styles.copy()
    def add_style(selector, property, value):
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles
    return add_style
#vs.
def MYcss_styles(stylesDict):
    stylesCopy = stylesDict.copy()
    def add_style(selector, property, value):
        if selector not in stylesCopy:
            stylesCopy.update({selector:{}})
        stylesCopy[selector][property] = value
        return stylesCopy
    return add_style

#pagination with reduce
from functools import reduce

def paginator(page_length):
    def paginate(document):
        def add_word_to_pages(pages, word):
            if pages == []:
                pages.append(word)
                return pages
            if (len(f'{pages[-1]} {word}')) > page_length:
                pages.append(word)
            else:
                pages[-1] += f' {word}'
            return pages
        return reduce(add_word_to_pages, document.split(), [])#last param. is empy list
    return paginate
#pagination with for loop
def LOOPpaginator(page_length):
    def paginate(document):
        tempLst = []
        def add_word_to_pages(pages, word):
            if pages == []:
                pages.append(word)
                return pages
            if (len(f'{pages[-1]} {word}')) > page_length:
                pages.append(word)
            else:
                pages[-1] += f' {word}'
            return pages
        for word in document.split():
            add_word_to_pages(tempLst, word)
        return tempLst
    return paginate

#better and worse way to handle string manipulation
def BETTERcreate_markdown_image(alt_text):
    enclosed_alt_text = f"![{alt_text}]"
    def add_url(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        image_syntax = enclosed_alt_text + f"({escaped_url})"
        def add_title(title=None):
            if title:
                return image_syntax[:-1] + f' "{title}")'
            return image_syntax
        return add_title
    return add_url

def create_markdown_image(alt_text):
    string = f'![{alt_text}]'
    def func(url):
        urlStr = url.replace('(', '%28')
        urlStr = urlStr.replace(')', '%29')
        urlStr = f'{string}({urlStr})'
        def inner(opt=''):
            nonlocal urlStr
            if opt != '':
                opt = f'"{opt}"'
                urlStr = urlStr.replace(')', '')
                urlStr = f'{urlStr} {opt})'
                return urlStr
            return urlStr
        return inner
    return func

# access keys and values in diction/ sorted example
def args_logger(*args, **kwargs):
    if args:
        for i in range(len(args)):
            print(f'{i+1}. {args[i]}')
    if kwargs:
        for key, value in sorted(kwargs.items()):
            print(f'* {key}: {value}')

# map function for changing dictionary values
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args = list(map(convert_md_to_txt, args))
        kwargs = dict(map(lambda item: (item[0], convert_md_to_txt(item[1])), kwargs.items()))#changes value of tupul in the item
        return func(*args, **kwargs)
    return wrapper
#vs for loop method
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args = list(map(convert_md_to_txt, args))
        for key, value in kwargs.items():
            kwargs[key] = convert_md_to_txt(value)
        return func(*args, **kwargs)
    return wrapper
#they actually made another function to handle the tuple..
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args))
        def kwarg_item_to_txt(item_tuple):#kwarg function
            key, value = item_tuple
            return (key, convert_md_to_txt(value))
        converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))
        return func(*converted_args, **converted_kwargs)
    return wrapper

#unpacking operator for potential arguments
def configure_plugin_decorator(func):
    def wrapper(*args):
        argDict =  dict(args)        
        return func(**argDict)# **is unpacked
    return wrapper

# Escape HTML 
def replacer(old, new):
    def replace(decorated_func):
        def wraper(text):
            return decorated_func(text.replace(old, new))
        return wraper
    return replace

@replacer('&', '&amp;')
@replacer('<', '&lt;')
@replacer('>', '&gt;')
@replacer('"', '&quot;')
@replacer("'", '&#x27;')
def tag_pre(text):
    return f"<pre>{text}</pre>"

#enums example
from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4
    
def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace('# ', '<h1>') + '</h1>'
        case (DocFormat.TXT, DocFormat.PDF):
            return '[PDF] ' + content + ' [PDF]'
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace('<h1>', '# ').replace('</h1>', '')
        case _:
            raise Exception('Invalid type')
        
#nested map and calls
class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4
    
def get_csv_status(status, data):
    match (status):
        case (CSVExportStatus.PENDING):
            return ('Pending...', list(map(lambda o: list(map(lambda i: str(i), o)), data)))
        case (CSVExportStatus.PROCESSING):
            return ('Processing...', '\n'.join(map(lambda o: ','.join(o), data)))
        case (CSVExportStatus.SUCCESS):
            return ('Success!', data)
        case (CSVExportStatus.FAILURE):
            return ('Unknown error, retrying...', get_csv_status(CSVExportStatus.PROCESSING, get_csv_status(CSVExportStatus.PENDING, data)[1])[1])
        case _:
            raise Exception('Unknown export status')
        
#great assighnment for edeiting docs
#uses dictionary as inputs for edits
class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4

def handle_edit(document, edit_type, editDict):
    match (edit_type):
        case (EditType.NEWLINE):
            if editDict['line_number'] >= len(document.split('\n')):
                raise Exception('Invalid line number')
            lines = document.split('\n')
            lines[editDict['line_number']] += '\n'
            return '\n'.join(lines)
        case (EditType.SUBSTITUTE):
            if editDict['line_number'] >= len(document.split('\n')):
                raise Exception('Invalid line number')
            if editDict['start'] > len(document.split('\n')[editDict['line_number']]):
                raise Exception('Invalid start index')
            if (editDict['end'] > len(document.split('\n')[editDict['line_number']])) | (editDict['end'] < editDict['start']):
                raise Exception('Invalid end index')
            lines = document.split('\n')
            string = lines[editDict['line_number']][editDict['start']:editDict['end']]
            lines[editDict['line_number']] = lines[editDict['line_number']].replace(string, editDict['insert_text'])
            return '\n'.join(lines)
        case (EditType.INSERT):
            if editDict['line_number'] >= len(document.split('\n')):
                raise Exception('Invalid line number')
            if editDict['start'] > len(document.split('\n')[editDict['line_number']]):
                raise Exception('Invalid start index')
            lines = document.split('\n')
            start = lines[editDict['line_number']][:editDict['start']]
            end = lines[editDict['line_number']][editDict['start']:]
            lines[editDict['line_number']] = start + editDict['insert_text'] + end
            return '\n'.join(lines)
        case (EditType.DELETE):
            if editDict['line_number'] >= len(document.split('\n')):
                raise Exception('Invalid line number')
            if editDict['start'] > len(document.split('\n')[editDict['line_number']]):
                raise Exception('Invalid start index')
            if (editDict['end'] > len(document.split('\n')[editDict['line_number']])) | (editDict['end'] < editDict['start']):
                raise Exception('Invalid end index')
            lines = document.split('\n')
            string = lines[editDict['line_number']][editDict['start']:editDict['end']]
            lines[editDict['line_number']] = lines[editDict['line_number']].replace(string, '')
            return '\n'.join(lines)
        case _:
            raise Exception('Unknown edit type')
        
#find min inlist
def find_minimum(nums):
    min = float('inf')
    for num in nums:
        if num < min:
            min = num
    if min == float('inf'):
        min = None
    return min

def is_divisible_by_2(number):
    return number % 2 == 0

def median_followers(nums):
    if len(nums) == 0:
        return None
    sortedLst = sorted(nums)
    if len(nums) % 2 == 0:
        first = sortedLst[(len(nums) // 2)-1]
        second = sortedLst[(len(nums) // 2)]
        return (first + second) / 2
    else:
        median = len(nums) / 2
        return sortedLst[int(median)]


# O(1)
# 2 different methods of dict look up, perhaps the second is more professional

def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]
    
def find_last_name2(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None

#binary search
# note that the arrays values must be sorted     
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        med = (low + high) // 2
        if arr[med] == target:
            return True
        elif arr[med] < target:
            low = med + 1
        else:
            high = med - 1
    return False

#bubble sort
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                num = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = num
                swapping = True
        end -= 1
    return nums

#merge sort
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    #print(lst1,'\n',lst2)
    return merge(left, right)

def merge(first, second):
    final = []
    i, j = 0, 0
    #print(first,second)
    while((i < len(first)) & (j < len(second))):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1
    final.extend(first[i:])
    final.extend(second[j:])
    return final

#insertion sort
def insertion_sort(nums):
    for i in range(0, len(nums)):
        j = i
        while((j > 0) & (nums[j-1] > nums[j])):
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
    return nums

#quick sort
def quick_sort(nums, low, high):
    if low < high:
        i = partition(nums, low, high)
        quick_sort(nums, 0, i-1) #left
        quick_sort(nums, i+1, high) #right
        #do not assighn a left and right variable
        

def partition(nums, low, high):
    pivit = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivit:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
    temp = nums[i]
    nums[i] = nums[high]
    nums[high] = temp
    return i

#returns the Fibonacci number at that index
def fib(n):
    if n <= 1:
        return n
    current = 0
    parent = 1
    gp = 0
    for i in range(0, n-1):
        current = parent + gp
        gp = parent
        parent = current
    return current

#Order 2^N - Exponential
def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    subsets = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets
# what i put
def power_set(input_set):
    if input_set == []:
        return [[]]
    lst = []
    first = input_set[0]
    cut = power_set(input_set[1:])
    for set in cut:
        combo = [first]
        combo.extend(set)
        lst.append(combo)
        lst.append(set)
    return lst

#Exponential Growth Sequences
def exponential_growth(n, factor, days):
    growth_sequence = [n]
    for i in range(days):
        growth_sequence.append(growth_sequence[-1] * factor)
    return growth_sequence

#Travel Time Limit
def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    while int(time_left) > 0:
        time_in_country *= factor
        time_left -= time_in_country
        count += 1
    return count

#uses stack to simplfy operations such as making sure all () are complete
def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False
    return stack.peek() is None #checks if statement is true and returns the value
#this was my answer without use of stack accidently
def no_stack_is_balanced(input_str):
    op = 0
    cp = 0
    for char in input_str:
        if char == "(":
            op += 1
        if char == ")":
            cp += 1
            if cp > op:
                return False
    if cp == op:
        return True
    return False