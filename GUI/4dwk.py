from sre_parse import State
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv

#GUI#

window = Tk()

window.title("Rota")
window.geometry('800x200')

monList = ["Mon"]
tueList = ["Tue"]
wedList = ["Wed"]
thuList = ["Thu"]
friList = ["Fri"]

week = []

mydict = {}

lblMon = Label(window, text="Monday:", font=("Arial Bold", 10))
lblMonVal = Label(window, text="", font=("Arial Bold", 10))
lblTue = Label(window, text="Tuesday:", font=("Arial Bold", 10))
lblTueVal = Label(window, text="", font=("Arial Bold", 10))
lblWed = Label(window, text="Wednesday:", font=("Arial Bold", 10))
lblWedVal = Label(window, text="", font=("Arial Bold", 10))
lblThu = Label(window, text="Thursday:", font=("Arial Bold", 10))
lblThuVal = Label(window, text="", font=("Arial Bold", 10))
lblFri = Label(window, text="Friday:", font=("Arial Bold", 10))
lblFriVal = Label(window, text="", font=("Arial Bold", 10))

lblMon.grid(column=0, row=6)
lblMonVal.grid(column=1, row=6)
lblTue.grid(column=0, row=7)
lblTueVal.grid(column=1, row=7)
lblWed.grid(column=0, row=8)
lblWedVal.grid(column=1, row=8)
lblThu.grid(column=0, row=9)
lblThuVal.grid(column=1, row=9)
lblFri.grid(column=0, row=10)
lblFriVal.grid(column=1, row=10)

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
lblU1.grid(column=5, row=0)
comboU1.grid(column=6, row=0)
lblU2 = Label(window, text="VB")
lblU2.grid(column=7, row=0)
comboU2.grid(column=8, row=0)
lblU3 = Label(window, text="CA")
lblU3.grid(column=9, row=0)
comboU3.grid(column=10, row=0)
lblU4 = Label(window, text="RF")
lblU4.grid(column=11, row=0)
comboU4.grid(column=12, row=0)
lblU5 = Label(window, text="MG")
lblU5.grid(column=13, row=0)
comboU5.grid(column=14, row=0)
lblU6 = Label(window, text="GW")
lblU6.grid(column=15, row=0)
comboU6.grid(column=16, row=0)
lblU7 = Label(window, text="DP")
lblU7.grid(column=17, row=0)
comboU7.grid(column=18, row=0)


#END GUI#

#LOGIC#

def btn_clicked():

    # Reset lists
    monList = ["Mon"]
    tueList = ["Tue"]
    wedList = ["Wed"]
    thuList = ["Thu"]
    friList = ["Fri"]
    
    # Build dictionary of user choices
    mydict = {
        lblU1.cget("text"): comboU1.get(),
        lblU2.cget("text"): comboU2.get(),
        lblU3.cget("text"): comboU3.get(),
        lblU4.cget("text"): comboU4.get(),
        lblU5.cget("text"): comboU5.get(),
        lblU6.cget("text"): comboU6.get(),
        lblU7.cget("text"): comboU7.get()}
    
    # Compare choice with day of week and populate list if they don't match
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
    
    # Update label to display current lists        
    lblMonVal.configure(text=monList[1:])
    lblTueVal.configure(text=tueList[1:])
    lblWedVal.configure(text=wedList[1:])
    lblThuVal.configure(text=thuList[1:])
    lblFriVal.configure(text=friList[1:])
    
    # Enable export menu item
    file.entryconfig("Export CSV", state="normal")
    
    # save all days as a list updating global variable
    global week
    week = [
        monList,
        tueList,
        wedList,
        thuList,
        friList
    ]
    
    return week
            
# Button to generate the rota
btn = Button(window, text="Generate", command=btn_clicked)
btn.grid(column=0, row=11)
lblBtn = Label()
lblBtn.grid(column=1, row=2)

# Save the rota as a csv file
def savecsv():
    try:
        with open('GUI\\files\\shifts.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(week)
        messagebox.showinfo("Export CSV", "Export Completed")  
    except:
        messagebox.showinfo("Export CSV", "Export Failed")
            
# Creating Menubar
menubar = Menu(window)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Export CSV', command = savecsv)
file.add_separator()
file.add_command(label ='Exit', command = window.destroy)
file.entryconfig("Export CSV", state="disabled")  
# display Menu
window.config(menu = menubar)

#END LOGIC#

window.mainloop()

