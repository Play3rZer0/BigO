X = [21, 5, 3, 18, 30, 2, 8]

def bubbleSort(X):
    n = len(X)


    for i in range(n):


        for j in range(0, n-i-1):


            if X[j] > X[j+1] :
                X[j], X[j+1] = X[j+1], X[j]

bubbleSort(X)

print ("Sorted list is:")
for i in range(len(X)):
    print ("%d" %X[i])
