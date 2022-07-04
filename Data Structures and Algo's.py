
        
from tempfile import tempdir
from typing import Tuple


board = [['x','o','x'],
         ['o','o','x'],
         ['o','o','o']]

board_length=len(board)
board_height=len(board)

string_column=""
x="xxx"
o='ooo'
count=0

for w in range(board_length): #w=['x','o','x']
    for v in range(board_height):#v='x'
        for loop in board:
            string_column+=loop[w][v]
            count+=1
            if o in string_column:
                print("o_won")
                break
            if x in string_column:
                print("x_won")
                break
            if count ==3:
                count=0
                string_column=""



#LINKED LISTS and REVERSE LINKED LISTS

class Node: #This class is used for creating all the stuff in each Node
    def __init__(self,value):
        self.head=value     #This makes the head equal to the vale
        self.next=None      #This is the end of LINKED LIST if there is another Node it will point to it

class LinkedList:
    def __init__(self,value):
        new_node=Node(value) #This creates the Node
        self.head=new_node   #This makes the head equal to the new Node
        self.tail=new_node   #This makes the tail equal to the new Node
        self.length+=1

    def append(self,value):#This function is adding a new node(dict value) to the end of the list
        new_node=Node(value)
        if self.length==0:#THIS checks if the list and empty and if it is makes the head and tail equal to the new node
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node #This sets the previous tail to point towards the new node
            self.tail=new_node #This updates the tail to the new node.
        self.length+=1

    def pop(self,value):#This function is used to pop the last element of a list
        if self.length==0:
            return None
        temp=self.head #creating two variable so one can be returned to get the value and another used to remove the node
        pre=self.head

        while (temp.next):#this walks through the list until there is no next
            pre=temp
            temp=temp.next

        self.tail=pre #This acts as the last node since the temp.next is none and broke the While loop
        self.tail.next=None
        self.length-=1

        if self.length==0:#This is checking if the node that was popped was the last node
            self.head=None
            self.tail=None
        return temp.value

    def prepend(self,value): #This function is used to add a node to the begining of a linked list
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head #This is setting the new first to point at the prior head
            self.head=new_node #This is updating the list head
        self.length+=1
        return True

    def pop_first(self,value):#This function is used to pop the first element of a list
        if self.length == 0: #This checks if the list is already 0
            return None

        temp = self.head #This sets the temp to the head
        self.head=self.head.next #This moves the head to the next list item so we can pop the old head
        temp.next=None #This pops the old head
        self.length-= 1 #This removes it from the list
        
        if self.length==0: #This checks if after popping the item the list becomes empty
            self.tail=None
        return temp.value

    #If you want to pop an item from the middle of the list implement a counter with a while loop that returns the current count and function to then use

    def get (self,index): #This returns the value of a linked list from a given index like a regular list
        if index <0 or index >= self.length:#This checks the index value is in the list
            return None
        
        temp=self.head #Set the temporary object equal to the current head
        
        for _ in range(index): #This goes to the index value provided so if 2 it will go from 0 to 2
            temp=temp.next #This moves the temp value to the next node each time the for loop iterates through
        
        return temp.value #This returns the temp value
    
    def change_value(self, index, value): #This is changing the value of a node in a list
        
        temp = self.get(index) #This locates the head with the get function and the index provided by the user and creates an object
        
        if temp:
            temp.value=value #This sets the value to the new provided value
            return True
        
        return False #This is if the index provided is not in the list

    def insert(self,index,value):
        if index <0 or index> self.length: #This checks whether the index provided is in the list
            return False

        if index == 0: #This is if the index wants to be inserted at the begining of the list
            return self.prepend(value)

        if index == self.length: #This is if the index wants to be inserted at the end of the list
            return self.append(value)

        #BELOW IS INSERTING AT A SPECIFIC POINT MIDDLE OF THE LIST
        new_node=Node(value)#This is creating a new node with the value provided
        temp = self.get(index-1)#This creates an object located at the spot before the index so it can connect to the next of the prior node

        new_node.next = temp.next #This sets the pointer of the new node to the Node at the index the new node will occupy
        temp.next = new_node #This moves the the pointer from the node before the index # to the new node
        self.length += 1
        
        return True

    def remove(self,index):
        if index <0 or index >=self.length: #This checks if the index is in the range
            return None
        
        if index == 0:#This removes the Node if it is the begining item
            return self.pop_first()
        
        if index == self.length-1:#This removes the Node if it is the last Node in the List
            return self.pop()
        
        pre = self.get(index -1) #This is getting the Node before the one that will be removed
        temp = pre.next #This is the Node that will get removed
        pre.next=temp.next# This moves the pointer of the Node that is before the temp equal to the same Node as the index being removed
        temp.next=None #This removes the Node
        self.length-=1 #This updates the length
        
        return temp.value

    def reverse(self):#This function reverses the linked list
        temp = self.head
        self.head=self.tail#This moves the current head to the tail
        self.tail=temp #This moves the current tail to the former head position by utilizing the temp object
        
        after = temp.next #This is
        before = None #this is the last spot in the list

        for _ in range(self.length):#This function is reversing all of the pointers in the list
            after = temp.next
            temp.next=before #This flips the pointer from left to right to right to left
            before=temp #This updates before to the prior head
            temp=after #This moves the temp to the after Node. The after gets moved the next time the for loop runs.

class NodeDoubly:
    def __init__(self,value): #This node will point both forward to the next node to the right and to the left
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self, value):
        new_node=NodeDoubly(value)
        self.head=new_node
        self.tail=new_node
        self.length = 1

    def append (self,value): #Adding a new node to the end of the Node
        new_node=NodeDoubly(value)
        if self.length==0:#THIS checks if the list and empty and if it is makes the head and tail equal to the new node
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node #This sets the previous tail to point towards the new node
            new_node.prev=self.tail #Since this is a new node at the end of the list need to connect it to previous node since DOUBLY
            self.tail=new_node #This updates the tail to the new node.
        self.length+=1

    def pop(self,value):#This function is used to pop the last element of a list
        if self.length==0:
            return None
        temp=self.tail #creating a variable so one can be returned to get the value and another used to remove the node
        if self.length==1:#checks if there is only one item in the list
            self.head=None
            self.tail=None
        
        #LESS STEPS THAN LINKED LIST SINCE WE CAN GO RIGHT TO LEFT AND NOT BE STUCK GOING RIGHT TO LEFT

        else: 
            self.tail=self.tail.prev #This moves the tail to the previous Node
            self.tail.next=None #This disconnects the next pointer to the prior tail Node
            temp.prev=None #This disconnects the previous pointer from the prioer tail Node
        self.length-=1
        return temp.value

    def prepend(self,value): #This function is used to add a node to the begining of a linked list
        new_node=NodeDoubly(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        
        else:
            new_node.next=self.head #This is setting the new first to point at the prior head
            self.head.prev=new_node #This tells the prior head to now point to the new head
            self.head=new_node #This is updating the list head
        
        self.length+=1
        return True

    def pop_first(self,value):#This function is used to pop the first element of a list
        if self.length == 0: #This checks if the list is already 0
            return None

        temp = self.head #This sets the temp to the head
        
        if self.length ==1:#If there is only one item it pops it
            self.head=None
            self.tail=None
        
        else:
            self.head=self.head.next #This moves the head to the next Node
            self.head.prev=None #This disconnects the new head from the head being popped
            temp.next=None #This disconnets the old head from the new head
        
        self.length-=1
        return temp.value

    def get (self,index): #This returns the value of a linked list from a given index like a regular list
        if index <0 or index >= self.length:#This checks the index value is in the list
            return None
        
        temp=self.head #Set the temporary object equal to the current head
        
        if index<self.length/2:#This is used to check the first half of the list. It makes more sense to split it into two for speed
            for _ in range(index): #This goes to the index value provided so if 2 it will go from 0 to 2
                temp=temp.next #This moves the temp value to the next node each time the for loop iterates through
        
        else:#This checks the second half of the list
            temp=self.tail#Since we are starting at the end of the list need to start at the tail
            for _ in range(self.length-1,index,-1):#This tells the range where to start which is index of 3, and each time through it goes down from 3 to 2 to 1 etc.
                temp=temp.prev#This sets the new temp value after each time the loop runs to the new node i.e moving it left.

        return temp.value #This returns the temp value
    
    
    def change_value(self, index, value): #This is changing the value of a node in a list
        
        temp = self.get(index) #This locates the head with the get function and the index provided by the user and creates an object
        
        if temp:
            temp.value=value #This sets the value to the new provided value
            return True
        
        return False #This is if the index provided is not in the list

    def insert(self,index,value):
        if index <0 or index> self.length: #This checks whether the index provided is in the list
            return False

        if index == 0: #This is if the index wants to be inserted at the begining of the list
            return self.prepend(value)

        if index == self.length: #This is if the index wants to be inserted at the end of the list
            return self.append(value)

        #BELOW IS INSERTING AT A SPECIFIC POINT MIDDLE OF THE LIST
        new_node=Node(value)#This is creating a new node with the value provided
        before = self.get(index-1)#This creates an object located at the spot before the index so it can connect to the next of the prior node
        after=before.next #This creates an object that points to the Node after the newly created node.

        new_node.prev=before #This is having the new nodes previous pointer point to the node before the new node
        new_node.next=after #This is having the new nodes next pointer point to the node after the new node
        before.next=new_node #This has the before node next pointer now point to the new node and not the after node anymore
        after.prev=new_node #This has the after node prev pointer now point to the new node and not the before node anymore


        self.length += 1 #Updaing the list by one
        return True

    def remove(self,index):
        if index <0 or index >=self.length: #This checks if the index is in the range
            return None
        
        if index == 0:#This removes the Node if it is the begining item
            return self.pop_first()
        
        if index == self.length-1:#This removes the Node if it is the last Node in the List
            return self.pop()
        
        temp=self.get(index)

        temp.next.prev=temp.prev #This makes the next nodes previous pointer equal to the previous node and not the current temp node.
        temp.prev.next=temp.next  #This makes the prev nodes next pointer equal to the next node and not the current temp node.
        temp.next=None #This removes the Node connection to the next node
        temp.prev=None #THis removes the Nodes connection to the previous node
        
        self.length-=1 #This updates the length
        return temp.value

class Stack:
    #Think of it like each node is a golf ball in a sleeve of titleists the main pointer only can get top and if you want the bottom you have to go take all others out
    def __init__(self,value):
        new_node = Node(value) #Creates a new node
        self.top = new_node #This sets the top pointer to the new node
        self.height = 1
        #The none pointer is pointing down visually

    def push (self,value): #THis is putting a new node on the top of the stack
        new_node = Node(value)
        if self.height == 0: 
            self.top=new_node #This makes the new node the top and does not need to adjust previous top since no nodes were in the stack
        else:
            new_node.next = self.top #This is setting the pointer for the new top node to the OLD top node so when it switches it knows what to point to
            self.top=new_node #This is setting the TOP pointer to the new node at the top of the stack
        self.height +=1
        
    
    def pop (self,value): #This function takes the top node off of the stack and moves the top pointer to the previous node
        if self.height==0: #This checks if the stack is empty
            return None
        
        temp = self.top #This creates a temp object that points at current top for later reference
        self.top=self.top.next #This reassigns the top pointer to the next node that the current top points to
        temp.next=None #This is removing the next pointer from the temp top node which pops it out of the stack
        self.height-=1 #This reduces the stacks
        return temp.value #This returns the popped item

class Queues:
    #Queues add from one end and remove from the other like a roller coaster line
    def __init__(self, value):
        new_node = Node(value)
        self.first=new_node #this is setting the first pointer to the new node
        self.last=new_node #This is setting the last pointer to the new node
        self.length=1
    
    def enterqueue(self,value):#This function is if we are adding something to the queue
        new_node=Node(value)
        if self.first is None:#This checks if the line (list) is empty so a node would be both first and last
            self.first=new_node #this is setting the first pointer to the new node
            self.last=new_node #this is setting the last pointer to the new node

        else:
            self.last.next=new_node #this sets the next pointer to the new node(new person in line) who is now last
            self.last=new_node #This updates the last pointer to the new node moving it from the current last person
        self.length+=1
    
    def leavequeue(self,value):#This function is if we are removing something from the queue
        if self.length==0:#This is if the queue is empty
            return self
        temp = self.first #This lets us return the value of the node removed
        
        if self.length ==1:#This is if there is only 1 person in the queue
            self.first = None
            self.last = None
        
        else:#This removes a node if there are more than one.
            self.first=self.first.next #This is moving the first pointer from the current first node to the next node(person in the line) who is now first
            temp.next=temp #This removes the next pointer from the node(person who was 2nd and is now first)

        self.length-=1
        return temp.value

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    #Binary Trees are below
    #Think of these like a family tree. They are dicitionaries that contain a value and can go to the left or right. So the left or right can contain a dictionary within a dictionary.
    #Full means each node is pointing to two other nodes
    #Perfect is if each side of the tree is equal from left to right
    #Complete is filled completely from left to right with no gaps
    #Child nodes are the nodes conneted either to the left or right of the parent and can be parents themselves
    #Leaf are nodes without any children

    #Binary Search Trees are organized left to right such as grater than or less than. So greater to right less than to left.
    #Binary Search Tree Big o 2^1(this)
class BinarySearchTrees: 
    def _init_(self,value):
        new_node=TreeNode(value)
        self.root=new_node #Root is the top of the tree and is the pointer for trees that points to the top
        
        #self.root = None #This is creating a pointer without a node which works as well.
        
    def insert(self,value):#This function inserts a new node in the tree
        new_node=Node(value)
        
        if self.root is None:#If the tree is empty then we are adding the new node
            self.root=new_node
            return True
        
        temp = self.root.root
        
        while (True):#Useing a while loop since the number of iterations through the loop is UNKOWN!!!!!
            
            if new_node.value==temp.value: #This checks if there is already a node with that value
                return False
            
            if new_node.value<temp.value:#This is the left function
                if temp.left is None:#If the spot is empty than it adds the new node
                    temp.left=new_node
                    return True
                
                temp = temp.left #This updates the temp if there is a node in the spot to use a the comparison for the next while loop.
            
            else:#This will check the right of each node in the tree  
                if temp.right is None:#If the spot is empty it will add the new node
                    temp.right=new_node
                    return True
                
                temp = temp.right#If the spot is full it will update the temp for the next iteration of the loop


    def contains(self,value):#This function checks if a tree contains something
        # NOT NEEDED if self.root is None: #This checks if the tree is empty and would not contain anything
        # NOT NEEDED    return False
        
        temp = self.root
        while temp is not None:#Using while loop since we do not know how big the tree is
            
            if value < temp.value:#Compares the two values
                temp=temp.left#Updates temp comparison for next while loop iteration
            
            elif value > temp.value:#Compares the two values this time going to the right
                temp = temp.right#Updates temp comparison for next while loop iteration
            
            else: #This is when the value is confirmed in the tree
                return True
        
        return False #This is when the value is not in the tree

    def minimum_value_node(self,current_node):#This function looks for the node with the minimum value in a specfic subtree!
        
        while current_node.left is not None: #Since we only need to compare less than we will always be going left. If it is not none then there is a node less than the parent node.
            current_node=current_node.left #This updates the current node to run again

        return current_node.value #This happens after the while loop returns a none so it returns this node


class HashTable:
    #A hash table like a hardware store. Hash is performed on dictionary key which then returns a key and its value AND an address. Think of this like searching for screws and you get back the quantity and where they are in the store.
    #Hash's go one way so can only use key values and always returns same value
    #Data is stored in a list
    #They are a combo of using the dictionary key and address values from lists(which we create)
    #If you want multiple items stored in a location need list of lists this is known as separate chaining
    #Linear propbing(open addressing) this is searching for an opening to store a key value in a blank location rather than list of lists
    #Can also have a linked list that you iterate through

    def __init__(self, size=7):
        self.data_map=[None]*size

    def _hash(self,key):
        my_hash=0
        
        for letter in key:
            my_hash=(my_hash+ord(letter)*23%len(self.data_map))
        
        return my_hash




