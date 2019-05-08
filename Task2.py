"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def flatten(l): 
    return [item for sublist in l for item in sublist]

def is_phone(val):
    cleaned = val.replace(" ", "")
    return len(cleaned) == 10 or cleaned[0] == '('

def extract_numbers(data):
    flat = flatten(data)
    filtered = list(filter(is_phone, flat))
    return filtered

def use_time(phones, data):
    for list in data:
        phones[list[0]] += int(list[3])
        phones[list[1]] += int(list[3])

def most_seconds(phones):
    higher = ['', 0]
    for phone, seconds in phones.items():
        if int(higher[1]) < int(seconds):
            higher = [phone, seconds]
    return higher
            

phones = dict.fromkeys(extract_numbers(calls), 0)
use_time(phones, calls)
longest = most_seconds(phones)
print(f"{longest[0]} spent the longest time, {longest[1]} seconds, on the phone during September 2016.")

