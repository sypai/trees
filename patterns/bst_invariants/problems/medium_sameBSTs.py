def sameBSTs(A, B):
    sizeA = len(A)
    sizeB = len(B)
    if sizeA == 0:
        return True
    if A[0] != B[0]:
        return False
    
    if not sizeA == sizeB:
        return False
    
    a = []
    b = []
    for i in range(sizeA):
        if A[i] > A[0]:
            a.append(A[i])
        if B[i] > B[0]:
            b.append(B[i])
    
    print("Larger ===>")
    print(a)
    print(b)
    larger = sameBSTs(a, b)
    
    a = []
    b = []
    for i in range(sizeA):
        if A[i] < A[0]:
            a.append(A[i])
        if B[i] < B[0]:
            b.append(B[i])
    

    print("Smaller ===>")
    print(a)
    print(b)

    print("---------------------------")

    smaller = sameBSTs(a, b)

    return larger and smaller
    
A = [ 10, 15, 8, 12, 94, 81, 5, 2, 11 ]
B = [ 10, 8, 5, 15, 2, 12, 11, 94, 81 ]

sameBSTs(A, B)
A = [1, 2, 3]
B = [1, 3, 2]


