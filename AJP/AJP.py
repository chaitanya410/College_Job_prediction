#!/usr/bin/env python
# coding: utf-8

# In[22]:


import csv

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
# Create the main application window
root = Tk()
root.title("College Admission Prediction and Job Salary Prediction")
root.geometry("1030x1000")
tabControl = ttk.Notebook(root)
tab2 = ttk.Frame(tabControl)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab2, text='College Admission Prediction')
tabControl.add(tab1, text='Job Salary Prediction')
tabControl.pack(expand = 1, fill ="both")


im = Image.open('JSP.png')
ph = ImageTk.PhotoImage(im)
label = Label(tab1, image=ph)
label.image=ph
label.pack()

ima = Image.open('imagemain.jpg')
php = ImageTk.PhotoImage(ima)
label = Label(tab1, image=php)
label.image=ph
label.pack(side=LEFT)

# Create a label for the branch dropdown menu
branch_label = Label(tab1, text="Select Branch : ",font='comicsansms 15 bold')
branch_label.place(x=560,y=210)

# Create the branch dropdown menu
branch_var1 = StringVar()
branch_dropdown = ttk.Combobox(tab1, textvariable=branch_var1, values=['Computer Science', 'Software Engineering', 'Digital Marketing', 'Web Designer', 'Machine Learning', 'Data Science', 'Information Technology', 'Analytics', 'Database management', 'Cybersecurity', 'Automation', 'Electronics & Telecommunication', 'Instrumentation ', 'Embedded Systems', 'Robotics', 'Telecommunications', 'Civil ', 'Structural Engineering', 'Geotechnical Engineering', 'Environmental Engineering', 'Water Resource Engineering', 'Mechanical ', 'Aerospace', 'Mechanical Design', 'Manufacturing '])
branch_dropdown.place(x=760,y=215)

# Create a label for the state dropdown menu
state_label = Label(tab1, text="Select State :",font='timenewroman 15 bold')
state_label.place(x=560,y=260)

# Create the state dropdown menu
state_var1 = StringVar()
state_dropdown = ttk.Combobox(tab1, textvariable=state_var1, values=['Andra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal', 'Andaman and Nicobar Islands', 'Delhi', 'Pondicherry'])
state_dropdown.place(x=760,y=265)

# Create a label for the year dropdown menu
year_label = Label(tab1, text="Select Year  :",font='timenewroman 15 bold')
year_label.place(x=560,y=310)

# Create the year dropdown menu
year_var1 = StringVar()
year_dropdown = ttk.Combobox(tab1, textvariable=year_var1, values=["2023", "2024", "2025","2026","2027","2028","2029","2030","2031","2032","2033"])
year_dropdown.place(x=760,y=315)

# Create a label for the text display box
text_label = Label(tab1, text="Average Salary :",font='timenewroman 15 bold')
text_label.place(x=560,y=460)

# Create the text display box
text_box1 = Text(tab1, height=10, width=50)
text_box1.place(x=560,y=510)


# Create a function to display the selected options in the text display box
def display_selections():
    
    branch = branch_var1.get()
    state = state_var1.get()
    year = year_var1.get()
    with open('Dataset.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
        reader_obj = csv.reader(file_obj)
            #inflation rate is 4.3 so variable inflation with value 0.043
        inflation = 0.043  
        # Iterate over each row in the csv 
        # file using reader object
        for row in reader_obj:
            if(row[0]==state and row[1]==branch):
                curr_sal=float(row[2])
                out=curr_sal+inflation*(int(year)-2022)*curr_sal
        
        
        text_box1.delete(1.0, END)
        text_box1.insert(END, f"{out} LPA")

# Create a button to display the selected options
im = Image.open('submit.png')
ph = ImageTk.PhotoImage(im)
label.image=ph 
label = Label(tab1, image=ph)


submit_button1 = Button(tab1,image=ph,font='130', command=display_selections)
submit_button1.place(x=650,y=350)

# Run the main event loop
im = Image.open('CAP.png')
ph = ImageTk.PhotoImage(im)

label = Label(tab2, image=ph)
label.image=ph
label.pack()

im = Image.open('imagemain.jpg')
ph = ImageTk.PhotoImage(im)

label = Label(tab2, image=ph)
label.image=ph
label.pack(side=LEFT)

# Create a label for 1oth marks
branch_label = Label(tab2, text="10th Marks    : ",font='comicsansms 15 bold')
branch_label.place(x=570,y=215)

# Create the text box for 10th marks
branch_var = StringVar()
branch_dropdown = Entry(tab2, textvariable=branch_var, bd=2,font=('Arial 12'))
branch_dropdown.place(x=770,y=215)

# Create a label for the 12th marks
m12 = Label(tab2, text="12th Marks    :",font='timenewroman 15 bold')
m12.place(x=570,y=265)

# Create the text box 12th
m12var = StringVar()
m123 = Entry(tab2, textvariable=m12var,bd=2,font=('Arial 12'))
m123.place(x=770,y=265)

# Create a label for the 12th division
t12_label = Label(tab2, text="12th Division :",font='timenewroman 15 bold')
t12_label.place(x=570,y=315)

# Create the text box 12th division
t12_var = StringVar()
t12 = Entry(tab2, textvariable=t12_var,bd=2,font=('Arial 12'))
t12.place(x=770,y=315)

# Create a label for the AIEEE
aie_label = Label(tab2, text="AIEEE Rank    :",font='timenewroman 15 bold')
aie_label.place(x=570,y=365)

# Create the text box AIEEE
aiee_var = StringVar()
aie = Entry(tab2, textvariable=aiee_var,bd=2,font=('Arial 12'))
aie.place(x=770,y=365)


# Create a label for the state dropdown menu
state_label = Label(tab2, text="Select State  :",font='timenewroman 15 bold')
state_label.place(x=570,y=415)

# Create the state dropdown menu
state_var = StringVar()
state_dropdown = ttk.Combobox(tab2, textvariable=state_var,font=('Arial 12'), values=['Andra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal', 'Andaman and Nicobar Islands', 'Delhi', 'Pondicherry'])
state_dropdown.place(x=770,y=415)



# Create the text display box
text_box2 = Text(tab2, height=10, width=50)
text_box2.place(x=595,y=560)

# Create a function to display the selected options in the text display box
def display_selections():
    text_box2.delete(2.0, END)
    
    branch = int(branch_var.get())
    state = str(state_var.get())
    t12div=int(t12_var.get())
    m12m=int(m12var.get())
    aieee = int(aiee_var.get())
    import pandas as pd
    df=pd.read_csv("CAP.csv")

    dict1={1: 'IIT KHARAGPUR', 2:'IIT BOMBAY', 3: 'IIT KANPUR', 4:'IIT DELHI', 5: 'IIT GUWAHATI', 6: 'IIT HYDERABAD', 7: 'IIT JODHPUR', 8: 'IIT ROPAR', 9: 'IIT MANDI', 10: 'IIT PALAKKAD', 11:'IIT TIRUPATI', 12: 'IIT GOA', 13: 'IIT JAMMU', 14: 'IIT INDORE', 15: 'IIT BHILAI', 16: 'NIT WARANGAL', 17: 'NIT TRICHY', 18: 'IIIT HYDERABAD', 19: 'BITS PILANI', 20: 'DTU DELHI', 21: 'VIT VELLORE', 22: 'BITS MESRA', 23: 'MANIPAL IT', 24: 'AHEMDABAD IT', 25: 'MNIT JAIPUR', 26: 'S O A  UNIVERSITY', 27: 'MNIT ALLAHABAD', 28: 'NMIMS', 29: 'MSIT', 30: 'SSN COLLEGE OF ENGINEERING', 31: 'UNIVERSITY COLLEGE OF ENGINEERING', 32: 'SRMIST CHENNAI', 33: 'BMS COLLEGE OF ENGINEERING', 34: 'KLEF HYDRABAD', 35: 'JADAVPUR UNIVERSITY', 36: 'HBUT KANPUR', 37: 'IIEST SHIBPUR', 38: 'NETAJI SUBHAS IT'}
    X=df[['10th Marks','12th Marks','AIEEE Rank','12th Division']]
    c=0
    y=df['College Rank']
    from sklearn.tree import DecisionTreeRegressor
    dtrmodel = DecisionTreeRegressor(random_state = 3)
    from sklearn.model_selection import train_test_split
    X_train,X_test, y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=3)
    dtrmodel.fit(X_train, y_train)
    t = dtrmodel.predict([[branch,m12m,aieee,t12div]])
    
 

    filter1 = df["States"]==state
    filter2 = df["College Rank"]>=t[0]
    df.where(filter1 & filter2, inplace = True)
    df=df.sort_values("States", inplace = False)
    #pd.set_option('display.max_rows', None)
    collist=[]
    for i in df["College"]:
        if i not in collist:
            collist.append(i)
    collist.pop()
    ans=[]
    for i in dict1:
        for j in collist:
            if dict1[i]==j:
                ans.append(j)
    for a in ans:
        text_box2.insert(END, a + '\n')
    print(ans)
    #text_box.delete(1.0, END)
    
    #text_box.insert(END, f"10th Marks  : {branch}\nSelected State  : {state}\nSelected Year : {year}")

# Create a button to display the selected options
im = Image.open('submit.png')
ph = ImageTk.PhotoImage(im)

label = Label(tab2, image=ph)
label.image=ph

submit_button2 = Button(tab2,image=ph,font='130', command=display_selections)
submit_button2.place(x=660,y=470)


root.mainloop()


# In[ ]:




