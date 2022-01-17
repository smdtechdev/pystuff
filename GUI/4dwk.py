from tkinter import *
from tkinter import ttk

#GUI#

window = Tk()

window.title("Rota")
window.geometry('1000x250')



lblMon = Label(window, text="Monday:", font=("Arial Bold", 20))
lblMonVal = Label(window, text="", font=("Arial Bold", 20))
lblTue = Label(window, text="Tuesday:", font=("Arial Bold", 20))
lblTueVal = Label(window, text="", font=("Arial Bold", 20))
lblWed = Label(window, text="Wednesday:", font=("Arial Bold", 20))
lblWedVal = Label(window, text="", font=("Arial Bold", 20))
lblThu = Label(window, text="Thursday:", font=("Arial Bold", 20))
lblThuVal = Label(window, text="", font=("Arial Bold", 20))
lblFri = Label(window, text="Friday:", font=("Arial Bold", 20))
lblFriVal = Label(window, text="", font=("Arial Bold", 20))

lblMon.grid(column=0, row=4)
lblMonVal.grid(column=1, row=4)
lblTue.grid(column=0, row=5)
lblTueVal.grid(column=1, row=5)
lblWed.grid(column=0, row=6)
lblWedVal.grid(column=1, row=6)
lblThu.grid(column=0, row=7)
lblThuVal.grid(column=1, row=7)
lblFri.grid(column=0, row=8)
lblFriVal.grid(column=1, row=8)

comboU1 = ttk.Combobox(window, width=4)
comboU2 = ttk.Combobox(window, width=4)
comboU3 = ttk.Combobox(window, width=4)
comboU4 = ttk.Combobox(window, width=4)
comboU5 = ttk.Combobox(window, width=4)
comboU6 = ttk.Combobox(window, width=4)
comboU7 = ttk.Combobox(window, width=4)

comboU1['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU2['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU3['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU4['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU5['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU6['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")
comboU7['values']= ("IN", "Mon", "Tue", "Wed", "Thu", "Fri", "AL")

comboU1.current(0) #set the selected item
comboU2.current(0) #set the selected item
comboU3.current(0) #set the selected item
comboU4.current(0) #set the selected item
comboU5.current(0) #set the selected item
comboU6.current(0) #set the selected item
comboU7.current(0) #set the selected item

lblU1 = Label(window, text="JS")
lblU1.grid(column=1, row=0)
comboU1.grid(column=2, row=0)
lblU2 = Label(window, text="VB")
lblU2.grid(column=3, row=0)
comboU2.grid(column=4, row=0)
lblU3 = Label(window, text="CA")
lblU3.grid(column=5, row=0)
comboU3.grid(column=6, row=0)
lblU4 = Label(window, text="RF")
lblU4.grid(column=7, row=0)
comboU4.grid(column=8, row=0)
lblU5 = Label(window, text="MG")
lblU5.grid(column=9, row=0)
comboU5.grid(column=10, row=0)
lblU6 = Label(window, text="GW")
lblU6.grid(column=11, row=0)
comboU6.grid(column=12, row=0)
lblU7 = Label(window, text="DP")
lblU7.grid(column=13, row=0)
comboU7.grid(column=14, row=0)


#END GUI#

#LOGIC#

monList = ["Mon"]
tueList = ["Tue"]
wedList = ["Wed"]
thuList = ["Thu"]
friList = ["Fri"]

mydict = {}

def btn_clicked():

    monList = ["Mon"]
    tueList = ["Tue"]
    wedList = ["Wed"]
    thuList = ["Thu"]
    friList = ["Fri"]
    
    
    #lblTue.configure(text=lblU1.cget("text"))
    mydict = {
        lblU1.cget("text"): comboU1.get(),
        lblU2.cget("text"): comboU2.get(),
        lblU3.cget("text"): comboU3.get(),
        lblU4.cget("text"): comboU4.get(),
        lblU5.cget("text"): comboU5.get(),
        lblU6.cget("text"): comboU6.get(),
        lblU7.cget("text"): comboU7.get()}
    #lblWed.configure(text=mydict)
    
    for k,j in mydict.items():
        print (k,j)
        print(monList[0])
        print(tueList[0])
        if j != monList[0] and j != "AL":
            monList.append(k)
        if j != tueList[0] and j != "AL":    
            tueList.append(k) 
        if j != wedList[0] and j != "AL":    
            wedList.append(k) 
        if j != thuList[0] and j != "AL":    
            thuList.append(k) 
        if j != friList[0] and j != "AL":    
            friList.append(k)             
        else:
            print("error")
            
    lblMonVal.configure(text=monList[1:])
    lblTueVal.configure(text=tueList[1:])
    lblWedVal.configure(text=wedList[1:])
    lblThuVal.configure(text=thuList[1:])
    lblFriVal.configure(text=friList[1:])
            
            


btn = Button(window, text="Click Me", command=btn_clicked)
btn.grid(column=0, row=2)
lblBtn = Label()
lblBtn.grid(column=1, row=2)

#END LOGIC#

window.mainloop()

