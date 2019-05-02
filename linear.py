def search(Y, n, x):

    for i in range (0, n):
        if (Y[i] == x):
            return i;
    return -1;

Y = ['apple', 'banana', 'mango', 'grapes', 'pineapple', 'durian']

x = "pineapple";

n = len(Y);
result = search(Y, n, x)
if(result == -1):
    print("Element is not present in the list")
else:
    print("Element", x, "is present at index", result)
