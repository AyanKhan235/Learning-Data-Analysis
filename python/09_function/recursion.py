def tri_recurion(k):
    if(k>0):
        result=k+ tri_recurion(k-1)
        print(result)
    else:
        result=0
    return result

tri_recurion(6)