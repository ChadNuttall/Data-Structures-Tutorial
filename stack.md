# Stack
A stack is a data structure that is characterized by the order in which items are added and removed. The stack can be refered to as **Last in First Out (LIFO)** which can be used to describe the order of how tasks will be accomplished.

## STACK OF PANCAKES
The concept of Last in First Out can be visualized much like a stack of pancakes. You are cooking breakfast in the morning. As you make pancakes your family is gratefully taking some to eat, though they do not always eat them as they are finished cooking so you make a stack. Each time that you put a pancake on the stack of finished pancakes you make a **Push** and each pancake taken off the stack is called a **Pop**. While pancakes are pushed and poped from the top of the stack in python data (pancakes) are pushed and poped from the **Back** of the stack. The first pancake you made will be at the very **Front** of the stack. As your family come to pop pancakes to eat they take the most recently pushed pancake from you stack.

![Figure 1](/Assets/Stack_of_pancakes.JPG)

## UNDO
You are likely familiar with the undo, redo function common in many computer programs like mircosoft word. These functions are made possible with the utilization of the stack. As you type each word is sent as a command to be displayed on the screen as well as pushed onto a stack. If you were to type the phrase "It's not easy being green" the most recent push would have been "green" and "green" would be at the back of your stack. Now as you then use the undo function you pop the data at the back of the stack which is "green" and your phrase now says "It's not easy being" This is how undo is able to acuratly undo in the right order. 

![Figure 2](/Assets/Not_Easy_Being_Green.JPG)

## THE FUNCTION STACK
The stack is used in more than just functions like undo. Anytime a function is called it is first pushed to the function stack also known as a machine stack or an execution stack. If there are no other functions called the function will be poped from the function stack and executed. In the case that another function is called that function will be pushed to the stack and executed unless antother function is called and so on. Here is an example using 

![Figure 3](/Assets/Function_Stack.JPG)

## Example
In this example we will use append to push integers into a list called stack and pop to remove integers from the back of the stack.

```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(8)
stack.pop()
stack.append(5)
stack.append(12)
stack.append(9)
stack.pop()
stack.pop()
print(stack)
# stack will return 5, 4, 3, 2, 1
```

## Your Turn
Without running the code predict what will be printed.

```python
stack = []
stack.append("A")
stack.append("B")
stack.pop()
stack.append("C")
stack.append("D")
stack.pop()
stack.append("E")
stack.append("F")
stack.append("G")
stack.append("H")
stack.pop()
stack.pop()
stack.append("I")
stack.pop()
stack.pop()
stack.pop()
stack.append("J")
stack.append("K")
stack.append("L")
stack.append("M")
stack.pop()
stack.append("N")
stack.append("O")
stack.append("P")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.append("Q")
stack.append("R")
stack.append("S")
stack.append("T")
stack.pop()
stack.append("U")
stack.append("V")
stack.pop()
stack.append("W")
stack.append("X")
stack.pop()
stack.append("Y")
stack.append("Z")
print(stack)
```
You can check your code with the solution here: ![Solution](/Solutions/stack_solution.py)
