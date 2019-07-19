# Analysis of complexity

## Task 0: 
  This task presents a time and space complexity of O(1), there is no
  iteration making the 5 operations have no increment by the input and
  the access to the arrays data is of O(1) generating no increased
  complexity.

## Task 1:
  First we iterate through the list of texts and calls to filter and 
  flatten the data. And we perform a third flattening on the conjunction
  of both new lists. Making first a loop over n and then a loop over n*4
  (which is the size of the internal lists) and then another loop over n.
  We have accumulated 3n + 2n*4 so far. Afterwards we made another loop to
  create a dictionary that will remove all duplicates and turn it into a
  list, adding 2n to the complexity. After that we perfom a simple print
  that leaves us with O(5n + 2n*4) making it a O(n*4) a very expensive
  operations in its current form. 

## Task 2:
  This one have less complexity since you only require flattening the 
  list once which makes the entire algorithm a little faster. First we 
  flat the calls array, then we extract the numbers and turn them into a
  dictionary for us to accmulate the incidence of each use tiem. Then we
  iterate over the dictionary to get the highest user and print it to the
  console. Nonetheless its still an O(n*4) because of the size of the 
  internal array being flattened.

## Task 3:
  In this task we first reduce the calls to a list containing our objective
  (the inner loops al negilible because they check for patterns inside
  the strings which are less than 12 characters long), afterwards we sort the 
  remaining list which in the worst case is of n size making this sort add log n
  and loop through it to print the first results. So far we have made 2n + log n

  For the second task we make 2 loops to count adding 2n and then we caculate the
  percentage which is a simple operation followed by the print.

  The third task have no double iteration which makes it an O(4n + log n) that
  simplifies to O(n log n).

## Task 4:
  In the last task we make 3 reduce operations for that we require to make the
  needed calculations. Then we make another reduce operation that have 3 internal
  loops making the current process 3n + 3n * 2. Then we generate a dictionary from
  that data to clean the duplicates, turn it into a list again adding 2n. Then we
  sort the data and print the values in a loop. This final step adds n log n.
  The total complexity would be 6n + 3n*2 + log n making this algorithm O(n2).