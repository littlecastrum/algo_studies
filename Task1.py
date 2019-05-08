"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def flatten(arr): 
    return [item for sublist in arr for item in sublist]

def is_phone(val):
    cleaned = val.replace(" ", "")
    return len(cleaned) == 10 or cleaned[0] == '('

def extract_numbers(array):
    flat = flatten(array)
    filtered = list(filter(is_phone, flat))
    return filtered

numbers_from_texts = extract_numbers(texts)
numbers_from_calls = extract_numbers(calls)
numbers = flatten([numbers_from_texts, numbers_from_calls])
print(f"There are {len(list(dict.fromkeys(numbers)))} different telephone numbers in the records.")