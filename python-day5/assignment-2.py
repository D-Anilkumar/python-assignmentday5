def merge_lists(L1, L2):
    
    
    if not L1:
        return L2
    elif not L2:
        return L1

    result = []
    i = 0
    j = 0

    

    for k in range(len(L1) + len(L2)):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            if i < len(L1) - 1:
                i += 1
            else:
                result += L2[j:]  # When the last element in L1 is reached,
                break             # append the rest of L2 to result.
        else:
            result.append(L2[j])
            if j < len(L2) - 1:
                j += 1
            else:
                result += L1[i:]  # When the last element in L2 is reached,
                break             # append the rest of L1 to result.

    return result

L1 = [10,20,40,60,70,80]
L2 = [5,15,25,35,45,60]
merge_lists(L1, L2)         
  