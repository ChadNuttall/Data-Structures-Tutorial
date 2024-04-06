# Stack
A stack is a data structure that is characterized by the order in which items are added and removed. The stack can be refered to as **Last in First Out (LIFO)** which can be used to describe the order of how tasks will be accomplished.

## STACK OF PANCAKES
The concept of Last in First Out can be visualized much like a stack of pancakes. You are cooking breakfast in the morning. As you make pancakes your family is gratefully taking some to eat, though they do not always eat them as they are finished cooking so you make a stack. Each time that you put a pancake on the stack of finished pancakes you make a **Push** and each pancake taken off the stack is called a **Pop**. While pancakes are pushed and poped from the top of the stack in python data (pancakes) are pushed and poped from the **Back** of the stack. The first pancake you made will be at the very **Front** of the stack. As your family come to pop pancakes to eat they take the most recently pushed pancake from you stack.

![Figure 1](/Stack_of_pancakes.jpg)

## UNDO
You are likely familiar with the undo, redo function common in many computer programs like mircosoft word. These functions are made possible with the utilization of the stack. As you type each word is sent as a command to be displayed on the screen as well as pushed onto a stack. If you were to type the phrase "It's not easy being green" the most recent push would have been "green" and "green" would be at the back of your stack. Now as you then use the undo function you pop the data at the back of the stack which is "green" and your phrase now says "It's not easy being" This is how undo is able to acuratly undo in the right order. 

![Figure 2](Not_Easy_Being_Green.jpg)

## THE FUNCTION STACK
The stack is used in more than just functions like undo. Anytime a function is called it is first pushed to the function stack also known as a machine stack or an execution stack. If there are no other functions called the function will be poped from the function stack and executed. In the case that another function is called that function will be pushed to the stack and executed unless antother function is called and so on. Here is an example using 

![Figure 3](Function_Stack.jpg)

## Example
In this example we will use uppend to push integers into a list called stack and pop to remove integers from the back of the stack.

```python
stack = []
stack.uppend(1)
stack.uppend(2)
stack.uppend(3)
stack.uppend(8)
stack.pop()
stack.uppend(5)
stack.uppend(12)
stack.uppend(9)
stack.pop()
stack.pop()
print(stack)
# stack will return 5, 4, 3, 2, 1
```

## Your Turn
Without running the code predict what will be printed.

```python
stack = []
stack.uppend("A")
stack.uppend("B")
stack.pop()
stack.uppend("C")
stack.uppend("D")
stack.pop()
stack.uppend("E")
stack.uppend("F")
stack.uppend("G")
stack.uppend("H")
stack.pop()
stack.pop()
stack.uppend("I")
stack.pop()
stack.pop()
stack.pop()
stack.uppend("J")
stack.uppend("K")
stack.uppend("L")
stack.uppend("M")
stack.pop()
stack.uppend("N")
stack.uppend("O")
stack.uppend("P")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.uppend("Q")
stack.uppend("R")
stack.uppend("S")
stack.uppend("T")
stack.pop()
stack.uppend("U")
stack.uppend("V")
stack.pop()
stack.uppend("W")
stack.uppend("X")
stack.pop()
stack.uppend("Y")
stack.uppend("Z")
print(stack)
```
You can check your code with the solution here: ![Solution](stack_solution.py)
