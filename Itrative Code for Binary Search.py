# Iterative Code For Binary Search
# Global Space
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

def BinarySearch(Value):
    LB = 0
    UB = len(arr) - 1
    while LB <= UB:
        Mid = (LB + UB) // 2
        if arr[Mid] == Value:
            return Mid
        elif arr[Mid] < Value:
            LB = Mid + 1
        else:
            UB = Mid - 1
    return -1

# Main Program (Input and Output)
choice = 0
while choice != 2:
    print()
    print("1. Search a value: ")
    print("2. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        Value = input("Enter the Value to search for: ")
        print(BinarySearch(Value))
    elif choice == 2:
        print("Bye...")
# End of Program