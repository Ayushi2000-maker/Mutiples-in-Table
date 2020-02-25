from tkinter import *
root=Tk()
root.title("table game")
root.configure(bg='yellow')
l=[]
def display(t):
    b1=l[(t[0]-1)*10+t[1]-1]#index of list starts from 0
    b1['text']=str(t[0]*t[1])
for i in range(1,11):
    b=Button(text=i,font='arial 20 bold',bg='green',fg='red',relief=RAISED).grid(row=0,column=i,padx=5,pady=5,sticky='nswe')
for i in range(1,11):
    b=Button(text=i,font='arial 20 bold',bg='green',fg='red',relief=RAISED).grid(row=i,column=0,padx=5,pady=5,sticky='nswe')
for i in range(1,11):
    for j in range(1,11):
        l.append(Button(text='?',font='arial 20 bold',bg='green',fg='red',relief=RAISED,command=lambda t=(i,j):display(t)))
        l[-1].grid(row=i,column=j,padx=5,pady=5,sticky='nswe')
    
for i in range(1,11):
    root.grid_rowconfigure(i,weight=1)
for i in range(1,11):
    root.grid_columnconfigure(i,weight=1)



root.mainloop()
