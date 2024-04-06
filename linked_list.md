# Linked List
## Linked List Structure
Linked lists are used to storing and managing collections of data. You are likely familiar with arrays which are another form of storing and manging collections of data. Arrays store each element in contiguous memory locations within memory, which means data is stored in memory locations next to each other. Linked lists stores data in a random way, all elements are stored together in the same location as **Nodes**. Each node will contain a link called a **Pointer** to the next node in the list. In this way linked lists are able to grow or shrink in size as elements are added or removed, unlike arrays which have fixed sizes. This makes adding or removing elements from a linked list easier than in arrays where you would have to shift elements.

The starting point of the linked list is called the **Head**. The has the reference for the first node in the list. By starting at the head and following the pointers you can travers the entire list.

![Figure 1](/Assets/linked_list.JPG)

<br>

The andvatages of Linked Lists can be increased with the use of a **Doubly Linked List**. In a doubly linked list each pointer stores not only the link to the next node but also a link to the previous node which allows you to travers the list in both directions. A doubly linked list will include both a Head and a **Tail**.

![Figure 2](/Assets/Doubly_Linked_List.JPG)

<br>

## Inserting into a Doubly Linked List
### Inserting at the Head
There are four steps to inserting at the head
1. Create a new node (new_node)
2. Set the "next" of the new node to the current head (new_node.next = self.head)
3. Set the "prev" of the current head to the new node (self.head.prev = new_node)
4. Set the head equal to the new node (self.head = new_node)

<br>

### Inserting at the tail
1. Create a new node (new_node)
2. Set the "prev" of the new node to the current node (new_node.prev = current)
3. Set the "next" of the new node to the next node after current (new_node.next = current.next)
4. Set the "prev" of the "next" node after current to the new node (current.next.prev = new_node)
5. Set the next of the current node to the new node (current.next = new_node)

<br>

### Inserting in the middle
1. Create a new node (we will call it new_node)
2. Set the "prev" of the new node to the current node (new_node.prev = current)
3. Set the "next" of the new node to the next node after current (new_node.next = current.next)
4. Set the "prev" of the "next" node after current to the new node (current.next.prev = new_node)
5. Set the next of the current node to the new node (current.next = new_node)

<br>

## Removing from a Linked List
### Remove Head or Tail
1. Set the "prev" of the second node (self.head.next) to nothing (self.head.next.prev = None)
2. Set the head to be the second node (self.head = self.head.next)

Note: If there is only one node in the list than both the head and tail would need to be set to none.

<br>

### Remove from the Middle
1. Set the prev of the node after current to the node before current (current.next.prev = current.prev)
2. Set the next of the node before current to the node after current (current.prev.next = current.next)

<br>

## The Deque

Python has a linked list built in that you can use called the deque. 
To initiate the deque use:

```python
import deque
#####
link_list = deque().
```
<br>
Here are some common functions in deque:

```python
# Insert at the head
my_deque.appendleft(value)

# Insert at the tail
my_deque.append(value)

# Insert in the middle
my_deque.insert(i, value) # Insert after node i

# Remove the head
value = my_deque.popleft()

# Remove the tail
value = my_deque.pop()

# Remove from the middle
del my_deque[i] # Remove node i

# Return length of Linked List
length = len(my_deque)

# Return True if length of the Linked List is 0
if len(my_deque) == 0:
```
<br>

## Example
In this example we are making a music player application, and we need to implement the functionality to manage playlists. Each playlist consists of a sequence of songs, and users can perform operations such as adding songs, removing songs, moving songs within the playlist, and playing songs form the playlist.

```python

class Song:
    def __init__(self, title, artist):
        # Initialize a Song including title, artist, duration
        self.title = title
        self.artist = artist
        self.next = None  # Pointer to the next song in the playlist
        self.prev = None  # Pointer to the previous song in the playlist

class Playlist:
    def __init__(self):
        # Initialize a Playlist object
        self.head = None  # Head pointer pointing to the first song in the playlist
        self.tail = None  # Tail pointer pointing to the last song in the playlist
        self.current_song = None  # Pointer to the currently playing song

    def add_song(self, title, artist):
        # Add a new song to the playlist
        new_song = Song(title, artist)
        if not self.head:
            # If the playlist is empty, set the new song as both head and tail
            self.head = new_song
            self.tail = new_song
        else:
            # Otherwise, append the new song to the end of the playlist
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def remove_song(self, title):
        # Remove a song from the playlist
        current = self.head
        while current:
            if current.title == title:
                # If the song to be removed is found
                if current.prev:
                    current.prev.next = current.next
                else:
                    # If the song to be removed is the head of the playlist
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    # If the song to be removed is the tail of the playlist
                    self.tail = current.prev
                return
            current = current.next
        print(f"Song '{title}' not found in the playlist.")

    def play_song(self, title):
        # Play a specific song in the playlist
        current = self.head
        while current:
            if current.title == title:
                self.current_song = current
                print(f"Now playing: {current.title} - {current.artist}")
                return
            current = current.next
        print(f"Song '{title}' not found in the playlist.")

    def next_song(self):
        # Play the next song in the playlist
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
            print(f"Now playing: {self.current_song.title} - {self.current_song.artist}")
        else:
            print("No next song in the playlist.")

    def prev_song(self):
        # Play the previous song in the playlist
        if self.current_song and self.current_song.prev:
            self.current_song = self.current_song.prev
            print(f"Now playing: {self.current_song.title} - {self.current_song.artist}")
        else:
            print("No previous song in the playlist.")

    def display_playlist(self):
        # Display all the songs in the playlist
        current = self.head
        print("Playlist:")
        while current:
            print(f"{current.title} - {current.artist}")
            current = current.next

# Example usage:
if __name__ == "__main__":
    # Create a playlist and add some songs
    playlist = Playlist()
    playlist.add_song("Come, Thou Fount of Every Blessing", "The Tabernacle Choir")
    playlist.add_song("Don't Stop Believin'", "Journey")
    playlist.add_song("Bohemian Rhapsody", "Queen")
    playlist.add_song("Livin' On A Prayer", "Bon Jovi")

    # Display the playlist
    playlist.display_playlist()

    # Play a song, then play the next song
    playlist.play_song("Don't Stop Believin")
    playlist.next_song()
    playlist.next_song()

    # Remove a song from the playlist
    playlist.remove_song("Bohemian Rhapsody")
    # Display the updated playlist
    playlist.display_playlist()

```
<br>

## Your Turn
Write a program that will store each letter of the alphabet in a linked list and display the results.

You can check your code with the solution here: ![Solution](linked_list_solution.py)
