class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None

class alphabet_list:
    def __init__(self):
        # Initialize the linked list with a head node
        self.head = None

    def insert(self, data):
        # Insert a new node with given data at the end of the linked list
        new_node = Node(data)
        if not self.head:
            # If the linked list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the linked list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print("None")

# Create a linked list to store each letter of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    # Insert each letter of the alphabet into the linked list
    alphabet_list.insert(char)

# Display the linked list
print("Linked List of Alphabets:")
alphabet_list.display()
