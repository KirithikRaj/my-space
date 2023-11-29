def subset(a, l):
    t = []
    if l == 0: 
        yield t
    elif l == 1:
        for i in range(len(a)):
            t = [a[i]]
            yield t
    else:
        #print('array, len: ', a, l)
        for i in range(len(a)-l+1):
            #print('     subset sent into fn, len: ', a[i+1:], l-1)
            #temp = subset(a[i+1:], l-1)
            #for j in range(len(a[i+1:])):
            for item in subset(a[i+1:], l-1):
                t = [a[i]] 
                for x in item:
                    t.append(x)
                #print('fixed: ', t)
                #t.append(item)
                #print('         t at the end of iter: ', t)
                yield t
    
arr = [1, 2, 3, 4, 5]
n = 2**len(arr)
powerset = []
for i in range(len(arr)):
    count = 0
    #print('init count: ', count)
    #sets = subset(arr, i)
    for item in subset(arr, i):
        powerset.append(item)
    #j = 0
    #while j < max(count, len(arr)):
        #print('     count, max: ', count, max(count, len(arr)))
        #powerset.append(next(sets))
        #print('     j, powerset:', j, powerset)
        #j += 1
powerset.append(arr)
triangle = []
for item in subset(arr, 3):
    triangle.append(item)
#print("Powerset: ", powerset)
#if len(powerset) == n: print("Yes!")
distinct = []
for x in powerset:
    if x not in distinct:
        distinct.append(x)
print(triangle)