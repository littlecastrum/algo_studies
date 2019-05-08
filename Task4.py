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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
from functools import reduce

def posible_telemarketer(acc, curr):
  if curr[0] not in text_senders and curr[0] not in text_receivers and curr[0] not in call_receivers:
    acc.append(curr[0])
  return acc

def pretty_print(data):
  data.sort()
  for code in data:
    print(code)

text_senders = reduce((lambda acc, curr: acc + [curr[0]]), texts, [])
text_receivers = reduce((lambda acc, curr: acc + [curr[1]]), texts, [])
call_receivers = reduce((lambda acc, curr: acc + [curr[1]]), calls, [])
list_of_numbers = list(dict.fromkeys(reduce(posible_telemarketer, calls, [])))

print("These numbers could be telemarketers:")
pretty_print(list_of_numbers)