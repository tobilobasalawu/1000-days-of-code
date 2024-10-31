import tkinter

window = tkinter.Tk()
window.title('Tkinter GUI')
window.minsize(width=500, height=400)


#label
myLabel = tkinter.Label(text="This is a label", font=('Arial', 24), )
myLabel.pack(side='left')

myLabel['text'] = 'New Text' #updating the text of a component by using dict keys

window.mainloop()