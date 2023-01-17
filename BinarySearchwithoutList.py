def binary_search(a_list, an_item):
   first = 0
   last = len(a_list) - 1       # last is the length of the list

   while first <= last:         # keep looking until we find the client or the first and last are flipped
       mid_point = (first + last) // 2
       if a_list[mid_point] == an_item:
           return True
       else:                    # move the end of list based on the middle number
           if an_item < a_list[mid_point]:
               last = mid_point - 1
           else:
               first = mid_point + 1
   return False


def binary_search_rec(a_list, first, last, an_item):
   if len(a_list) == 0:
       return False
   else:
       mid_point = (first + last) // 2
       if a_list[mid_point] == an_item:
           return True
       else:
           if an_item < a_list[mid_point]:
               last = mid_point - 1
               return binary_search_rec(a_list, first, last, an_item)
           else:
               first = mid_point + 1
               return binary_search_rec(a_list, first, last, an_item)


if __name__ == '__main__':
   a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]
  
   print('Binary Search:', binary_search(a_list, 4))
   print('Binary Search Recursive:',
       binary_search_rec(a_list, 0, len(a_list) -1, 4))