# Recursive Code For Binary Search
# Global Space
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
LB = 0
UB = len(arr) - 1

def BinarySearch(LB,UB,Value):
    Mid = (LB + UB) // 2
    if arr[Mid] == Value : # Base Case
        return Mid
    elif LB > UB : # Base Case 
        return -1
    elif arr[Mid] < Value : # General Case
        return BinarySearch (Mid+1,UB,Value)
    else: # General Case
        return BinarySearch (LB,Mid-1,Value)
# Main Program (Input and Output)
choice = 0
while choice != 2:
    print()
    print("1. Search a value: ")
    print("2. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        Value = input("Enter the Value to search for: ")
        print(BinarySearch(LB,UB,Value))
    elif choice == 2:
        print("Bye...")
# End of Program
