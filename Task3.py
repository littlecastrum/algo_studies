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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
from functools import reduce

list_of_codes = []

# b => bangalore
def b_called_to_code(acc, curr):
  area_code = ""
  if "(080)" in curr[0]:
    if "(" in curr[1]:
      end_area_code_index = curr[1].find(")")
      area_code = curr[1][0: end_area_code_index + 1]
    elif curr[1][0] in "789":
      area_code = curr[1][0:4]
    elif curr[1][0:3] == "140":
      area_code = "140"
    if area_code not in acc:
      acc.append(area_code)
  return acc

# b2b => bangalore to bangalore
def b2b_count(acc, curr):
  if "(080)" in curr[0] and "(080)" in curr[1]:
    acc += 1
  return acc

def b_calls_count(acc, curr):
  if "(080)" in curr[0]:
    acc += 1
  return acc
  
def pretty_print(data):
  data.sort()
  for info in data:
    print(info)

filtered_codes = reduce(b_called_to_code, calls, [])
print("The numbers called by people in Bangalore have codes:")
pretty_print(filtered_codes)

total_b2b_calls = reduce(b2b_count, calls, 0)
total_calls_from_b = reduce(b_calls_count, calls, 0)
percentage = (total_b2b_calls * 100) / total_calls_from_b
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")