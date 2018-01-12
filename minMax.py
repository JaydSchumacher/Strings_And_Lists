x = [2,54,-2,7,12,98]

def minMax(x):
    min = 0;
    max = 0;

    for count in range(len(x)):
        if x[count] < min:
            min = x[count]
        
        if x[count] > max:
            max = x[count]
    print (min, max)

minMax(x)