# Insertion Code
# Global Space
'''
*Note:- The following code is working on all the arrays mentioned below*
arr = [10,9,5,12,5,4,8,2,6,7]                                   # This Array contains numericals in Integer Form 
arr = ['10','9','5','12','5','4','8','2','6','7']               # This Array contains numericals in String Form
arr = ['a', 'z', 'p', 'd', 't', 'h', 'g', 's', 'b', 'n', 'k']   # This Array contains characters in String Form
'''

arr = [10,9,5,12,5,4,8,2,6,7]     

def InsertionSortAsc(arr):
    for BlueP in range (1, len(arr)):
        Value = arr[BlueP]
        BlackP = BlueP - 1
        while arr[BlackP] > Value and BlackP >= 0:  # checking if the current data is greater than the next data
            arr[BlackP + 1] = arr[BlackP] # Swapping of Data
            BlackP -= 1 # It's done to check whether the current data is smaller than the other previous data so that it can be properly sorted
        arr[BlackP + 1] = Value # If the data is not smaller than the previous data therefore it is already in its correct position
        
def InsertionSortDesc(arr):
    for BlueP in range (1, len(arr)):
        Value = arr[BlueP]
        BlackP = BlueP - 1
        while arr[BlackP] < Value and BlackP >= 0:  #checking if the current data is less than the next data
            arr[BlackP + 1] = arr[BlackP] # Swapping of Data
            BlackP -= 1 # It's done to check whether the current data is greater than the other previous data so that it can be properly sorted
        arr[BlackP + 1] = Value # If the data is not greater than the previous data therefore it is already in its correct position

# Main Program
print("Data Before Being Sorted Looks Like This: ", arr)
print()
choice = 0
while choice != 3:
    print("1. Press (1) If You Want The Data To Be Displayed In Ascending Order.")
    print("2. Press (2) If You Want The Data To be Displayed In Descending Order.")
    print("3. Press (3) To Exit The Program.")
    print()
    choice = int(input("Enter Your Choice: "))
    print()
    if choice == 1:
        InsertionSortAsc(arr)
        print("Data After Being Sorted Looks Like This", arr)
    elif choice == 2:
        InsertionSortDesc(arr)
        print("Data After Being Sorted Looks Like This", arr)
    else:
        print("Exiting...")
# End of Program