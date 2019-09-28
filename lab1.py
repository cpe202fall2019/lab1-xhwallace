
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   pass
   if int_list == None:
      raise ValueError
   if len(int_list) < 1:
      return None
   biggest = int_list[0]
   for val in int_list:
      if val > biggest:
         biggest=val
   return biggest

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   pass
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return int_list
   new_list=reverse_rec(int_list[1:])
   new_list.append(int_list[0])
   return new_list

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
   if int_list == None:
      raise ValueError
   if low == high:
      return low
   if int_list[(high-low)//2] < target:
      return bin_search(target, (high+low)//2+1, high, int_list)
   if int_list[(high - low) // 2] > target:
      return bin_search(target, low, (high+low)//2-1, int_list)
   return (high+low)/2