# Python3 code to move all zeroes 
# at the end of array 
  
# Function which pushes all 
# zeros to end of an array. 
def pushZerosToEnd(arr, n): 
    count = 0 # Count of non-zero elements 
      
    # Traverse the array. If element  
    # encountered is non-zero, then 
    # replace the element at index 
    # 'count' with this element 
    for i in range(n): 
        if arr[i] != 0: 
              
            # here count is incremented 
            arr[count] = arr[i] 
            count+=1
      
    # Now all non-zero elements have been 
    # shifted to front and 'count' is set 
    # as index of first 0. Make all  
    # elements 0 from count to end. 
    while count < n: 
        arr[count] = 0
        count += 1
# List of Integers 
arr = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4] 
  
# Sorting list of Integers
arr.sort() 
  
print(arr) 
# Driver code 

n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr)  