# Bubble Sort Code
# #Global Space 
students=['Kevin','Anthony','Thomas','Edward','Alan','Harry',Chris','William']

def BubbleSort(Names):
    N = len(Names)
    for Count in range (N):
        swapped= False      # This line initializes the boolean variable swapped to False (if no swaps are made in nest loop then the list is sorted)
        for Index in range (0, N - Count - 1): #(n-i-1) represents the range of elements to be compared during each loop, excluding the already sorted elements.
            if Names[Index] > Names[Index + 1]: #Checking if the first data is greater than the next data or not (thus incrementing)
                Temp = Names[Index]
                Names[Index] = Names[Index + 1]
                Names[Index + 1] = Temp
                swapped = True
        if not swapped: # Use of'not' to check if swapped is false to determine that the list has been sorted completely
            break # immediately cuts off from the loop when the above condition is true

# Main Program
BubbleSort(students)
print("The Sorted list of Students are:- ", students)
            
