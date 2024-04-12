num = int(input())
res = ""
bucket = []
l = len(str(num))
f = 0
s = 0
def backtrack(bucket, f, s):
    if not bucket:
        return
    if bucket[-1] == 4:
        bucket[-1] = 7
        f -= 1
        s += 1
        return bucket
    bucket[-2] = backtrack(bucket[:-1], f, s)
    bucket.append(4) 
    f += 1  
    return bucket
for i, v in enumerate(str(num)):
    back = l - (f + s)
    if f > s and  back <= f - s:
        bucket.append(7)
    else:
        if int(v) <= 4:
            bucket.append(4)
            f += 1
        elif int(v) <= 7:
            bucket.append(7)
            s += 1
        else:
            if s:
                bucket.append(4)
            else:
                bucket = backtrack(bucket, f, s)
for i in bucket:
    res += str(i)

print(int(res))
            
            
            

    
            
            
        
        
        
