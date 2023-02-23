
from tkinter import *
import random

root=Tk()

root.title("Random person Wheel")
root.geometry("500x500")


list1 = ["James" , "Isabella" , "Sophia" , "Oliver" , "Peter", "bobby", "joe", "Bobylina", "joelina", "Billy Bob Joe"]
print(list1)

def random_number():
	random_no = random.randint(0, 9)
	print(random_no)
	random_lucky_friend = list1[random_no]
	print("your random friend is: " + random_lucky_friend)


btn1 = Button(root, text="Who is your Random Friend?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()