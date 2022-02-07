class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
# Node Class:
# Data is the information in the list
# Next node will point to the next node in the list
# Every instantiation will be a new node
# New nodes must be on top so previous node can point to it

# Example: 
# node2 = Node("Data2")
# node1 = Node("Data1", node2)

class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None

# Wrapper Class: LinkedList
# Helps keep track of our head and last nodes
# We can add to the beggining or the end of the linked list
# We create a method to add to the beginning of the linked list
# We create another method to add to the end of the linked list

    def print_ll(self):
        ll_string=""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

# print_ll explanation:
# print_ll will print a visual representation of the linked list in the terminal. 
# print_ll == print linked list
# ll_string variable will print at the end of the function
# node = self.head will asign the head from __init__ to the variable
# If it is None, it will let us know (print) and it is the first item in the list.
# If not, we go into a while loop. 
# While none means: while node != None
# We append to our ll_string variable (+=) node.data
# We transform it to a string in case the information is sent in a different type
# We use an f string to format it with the visual cue " ->"
# We go to the next node
# When we reach node = None the while loop will break
# We will append None to out ll_string variable
# Finally, we will print the complete variable linked list. 

# Example:
# ll = LinkedList()
# node4 = Node("Data4", None)
# node3 = Node("Data3", node4)
# node2 = Node("Data2", node3)
# node1 = Node("Data1", node2)
# ll.head =  node1
# ll.print_ll()

# Output:
# Data1 -> Data2 -> Data3 -> Data4 -> None

    def insert_beggining(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

# insert_beggining explanation:
# The funcion passes the data into a Node function
# The function then assigns the data and the next variable
# it then updates the head function to those variables
# This adds the next node to the beggining of the cue
# Once all instances have been processed, it runs the print function to display it

# Example:
# ll = LinkedList()
# ll.insert_beggining("info")
# ll.insert_beggining("new info")
# ll.insert_beggining("newer info")
# ll.print_ll()

# Output:
# newer info -> new info -> info -> None 
