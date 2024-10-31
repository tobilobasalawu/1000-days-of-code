import tkinter

window = tkinter.Tk()
window.title('Tkinter GUI')
window.minsize(width=500, height=400)


#label
myLabel = tkinter.Label(text="This is a label", font=('Arial', 24), )
myLabel.pack(side='left')

myLabel['text'] = 'New Text' #updating the text of a component by using dict keys
myLabel.config(text = 'New Text') #updating the text of a component using config method

def buttonClicked():
  print('I got clicked')
  myLabel['text'] = 'Button Got Clicked!'

button = tkinter.Button(text='Click Me', command=buttonClicked) #command - event listener, enter the functions name
button.pack() 

window.mainloop()
