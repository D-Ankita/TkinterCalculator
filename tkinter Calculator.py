#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


my_root = Tk()  #tk class instance


# In[3]:


my_root.geometry("312x324" ) #width x height


# In[4]:


my_root.resizable(0, 0)  # this is to prevent from resizing the window


# In[5]:


my_root.title("Calculator")


# In[11]:


# 'btn_click' function : This Function continuously updates the input field whenever you enter a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# In[12]:


# 'bt_clear' function :This is used to clear the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")


# In[13]:


# 'bt_equal':This method calculates the expression present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


# In[14]:


expression = ""


# In[15]:


# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()


# In[16]:


# Let us creating a frame for the input field
 
input_frame = Frame(my_root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)


# In[17]:


#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 


# In[18]:


#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(my_root, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 


# In[19]:


# first row
 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 


# In[20]:


# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 


# In[21]:


# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 


# In[22]:


# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 


# In[23]:


# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 


# In[24]:


my_root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:


#my_root.mainloop()


# In[7]:


#my_root.maxsize(1200,988)#width,height


# In[6]:


#my_root.minsize(200,100)#width,height


# In[8]:


#varimg = Label(image = PhotoImage(file"1.jfif"))
#var1 = Label(text = " PyCharm Community Edition \n Version 2017.2 \n\n Create \n Open ")


# In[9]:


#varimg = pack()
#var1.pack()

