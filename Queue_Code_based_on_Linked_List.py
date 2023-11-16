#Queue Code based on Linked List
#Global Space

Free = 0
Header = 0
Tail = 0
Null = -1

class QueueLinkedList:
    def __init__(self):
        self.Data = ''
        self.Pointer = 0
        
Queue=[QueueLinkedList() for i in range(8)]

def Initialisation ():
    global Header,Tail,Null,Free,Queue
    Header = Null
    Tail = Null
    Free = 0
    for i in range (8):
        Queue[i].Data= ''
        Queue[i].Pointer = i + 1
    Queue[7].Pointer = Null
    
def Enqueue(Value):
    global Header,Tail,Null,Free,Queue
    if Free == -1:                      #Check to see if Queue is alredy full with Data
        print ("Overflow! Can not add to Queue")
    elif Free != Null:                  #Check to see for empty space in queue
        NewNode = Free                  #NewNode will represent the index of the Queue
        Queue[NewNode].Data = Value     #At the index pointed by NewNode insert the Value
        Free = Queue[Free].Pointer      #The Free Pointer is now moved to the next free location
        Queue[NewNode].Pointer = Null   #It sets the Pointer attribute of the new node to Null since it is now the last node in the queue.
        Tail = NewNode
        if Tail != Null:
            Queue[Tail].Pointer = NewNode
        Tail = NewNode
    else:
        pass
    
def Dequeue():
    global Header,Tail,Null,Free,QueueS
    Header = Tail
    if Header == Null :
        print("Underflow! Queue is Empty")
        return None
    if Header != Null:
        Value = Queue[Header].Data          #Dequeue the Data at the index indicated by the header
        ThisNode = Queue[Header].Pointer    #Assign the index pointed by the header to 'ThisNode'
        if Queue[Header].Pointer == Null:                #Check to see if the queue is now empty
            Tail = Null                     #Setting 'Tail' to -1 to indicate the Queue is Empty
            Header = Null
        else:    
            Queue[Header].Pointer = Free        #Updates the index pointed by the "Header' to the index pointed by 'Free'
            Free = Header
            Header = ThisNode                   #Points to now a new Header as the previous Header is removed
        Tail -= 1
        Header = Tail
    return Value

def PrintQueue():
    global Header,Tail,Null,Free,Queue
    print("Header= ", Header,"  Tail= ", Tail,"  Free= ",Free)
    print("Queue:")
    CurrentNode = Header            #This variable will be used to traverse the queue while printing the data in each node.
    if Tail == Null:              #Checks if the queue is empty
        print("Underflow! Queue is Empty")
        return None
    while CurrentNode != Null:
         print(CurrentNode, Queue[CurrentNode].Data) #Prints the current index as well as the data at the corresponding index
         CurrentNode = Queue[CurrentNode].Pointer    #Moves the pointer to the next index 'pointed' in the queue.
         
#Main Program
Initialisation()
Choice = 0
while Choice != 4:
    print("1. Insert in Queue")
    print("2. Print Queue")
    print("3. Remove from Queue")
    print("4. Exit Program")
    Choice = int(input("Enter Your Choice: "))
    if Choice == 1:
        Value = str(input("Enter The Value to be inserted:"))
        Enqueue(Value)
    elif Choice == 2:
        PrintQueue()
        for i in range(8):
            print(i, Queue[i].Data,Queue[i].Pointer)
    elif Choice == 3:
        Value = Dequeue()
        print ("Data Popped ==>", Value)
    elif Choice == 4:
        print("Exiting Program")
    else:
        print("Invalid Command")