#!/usr/bin/env python
# -*- coding: utf8 -*-

import pytesseract, pickle, re, datetime, pywhatkit
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showwarning, showinfo
from os import listdir,remove

entered_class_name = ""

class wp_automation_frontend():
    
    def __init__(self):
        
        self.ui = Tk()
        self.ui.title("Wp Automation by ika")
        self.ui.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.ui.configure(bg="#282d35")
        self.ui.resizable(False, False)
        self.center_window(245,750,self.ui)


    def center_window(self,x,y, window) :
        window_width = x
        window_height = y 
        window_x = int((window.winfo_screenwidth() / 2) - (window_width / 2)) 
        window_y = int((window.winfo_screenheight() / 2) - (window_height / 2))

        window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(window_y) 
        window.geometry(window_geometry) 
        return

    def select_file(self): 
        
        self.i = Tk()
        self.i.title("Wp Automation by ika")
        self.i.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.i.configure(bg="#282d35")
        self.i.resizable(False, False)
        self.center_window(175,65,self.i)
        self.entry = Entry(self.i, width= 20,bg="grey30",fg="white")
        self.entry.focus_set()
        self.entry.place(x=5,y=5)

        Button(self.i, text= "Enter The Class Name",bg="grey30",fg="white",width=20, command=self.save_text).place(x=3,y=30)

    def save_text(self):

        filetypes = (
            #('text files', '*.txt'),
            ('All files', '*.*'),
            ('png files', '*.png'),
            ('jpeg files', '*.jpeg'),
            ('jpg files', '*.jpg'),
            
        )

        self.entered_class_name = self.entry.get()
        global entered_class_name
        entered_class_name = self.entered_class_name
        self.i.destroy()
        self.image_path = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

        backend = wp_automation_backend
        backend.start2(self)

    

    def show_info(self):

        self.info_screen = Tk()
        self.info_screen.title("Wp Automation by ika")
        self.info_screen.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.info_screen.configure(bg="#282d35")
        self.info_screen.resizable(False, False)

        

        self.class_folder = listdir('C:\wp_automation\data')
        
        self.list_of_class_numbers = []
        self.list_of_class_letters = []

        for self.class_numbers in self.class_folder:

            self.class_level = re.findall(r'\d+',self.class_numbers )

            for k in range(len(self.class_level)):
                char = self.class_numbers.replace(self.class_level[k],"")

            self.list_of_class_letters.append(char)

            for i in range(len(self.class_level)):
                
                bişey = int(self.class_level[i])
                self.list_of_class_numbers.append(bişey)

        
        self.list_of_class_letters.sort()
        self.list_of_class_numbers.sort(reverse=True)

        self.list_of_class_letters = list(dict.fromkeys(self.list_of_class_letters))
        self.list_of_class_numbers = list(dict.fromkeys(self.list_of_class_numbers))


        self.max_row = 0
        i = 0
        for i in range(len(self.class_folder)):

            self.make_the_buttons(i)

        size_x = self.max_row * 53
        
        self.center_window(750,size_x,self.info_screen)

    def make_the_buttons(self,bla):
        
        class_button = Button(self.info_screen, text=self.class_folder[bla],font="Arial 15",height=1,width=5,bg="grey30",fg="white",command=lambda : self.show_info_button(self.class_folder[bla]))

        self.level_of_button = re.findall(r'\d+',self.class_folder[bla] )
    
        for k in range(len(self.level_of_button)):

            self.letter_of_button = self.class_folder[bla].replace(str(self.level_of_button[k]),"")
        
        #print(self.class_folder[bla]," letter:",self.letter_of_button ,"     level: ",self.level_of_button)

        counter2 = 1
        for letter in self.list_of_class_letters:
            if str(letter) == self.letter_of_button:
                button_column = counter2
                break
            counter2 += 1


        counter1 = 1
        for j in self.list_of_class_numbers:
            
            if j == int(self.level_of_button[0]):
                button_row = counter1
            
            counter1+=1

        class_button.grid(row=button_row,column=button_column,padx=2,pady=2)

        if self.max_row < button_row:
            self.max_row = button_row
        #print(button_row)

    #____________________________________________________________________________________________________________original is top one
    def show_info_phone(self):

        self.info_screen_phone = Tk()
        self.info_screen_phone.title("Wp Automation by ika")
        self.info_screen_phone.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.info_screen_phone.configure(bg="#282d35")
        self.info_screen_phone.resizable(False, False)

        

        self.class_folder_phone = listdir('C:\wp_automation\data')
        
        self.list_of_class_numbers_phone = []
        self.list_of_class_letters_phone = []

        for self.class_numbers_phone in self.class_folder_phone:

            self.class_level_phone = re.findall(r'\d+',self.class_numbers_phone )

            for k in range(len(self.class_level_phone)):
                char = self.class_numbers_phone.replace(self.class_level_phone[k],"")

            self.list_of_class_letters_phone.append(char)

            for i in range(len(self.class_level_phone)):
                
                bişey = int(self.class_level_phone[i])
                self.list_of_class_numbers_phone.append(bişey)

        
        self.list_of_class_letters_phone.sort()
        self.list_of_class_numbers_phone.sort(reverse=True)

        self.list_of_class_letters_phone = list(dict.fromkeys(self.list_of_class_letters_phone))
        self.list_of_class_numbers_phone = list(dict.fromkeys(self.list_of_class_numbers_phone))

         
        self.max_row_phone = 0
        i = 0
        for i in range(len(self.class_folder_phone)):

            self.make_the_buttons_phone(i)

        size_x = self.max_row_phone * 53
        
        self.center_window(750,size_x,self.info_screen_phone)

    def make_the_buttons_phone(self,bla):
        
        class_button = Button(self.info_screen_phone, text=self.class_folder_phone[bla],font="Arial 15",height=1,width=5,bg="grey30",fg="white",command=lambda : self.add_phone_number(self.class_folder_phone[bla]))

        self.level_of_button_phone = re.findall(r'\d+',self.class_folder_phone[bla] )
    
        for k in range(len(self.level_of_button_phone)):

            self.letter_of_button_phone = self.class_folder_phone[bla].replace(str(self.level_of_button_phone[k]),"")
        
        

        counter2 = 1
        for letter in self.list_of_class_letters_phone:
            if str(letter) == self.letter_of_button_phone:
                button_column = counter2
                break
            counter2 += 1


        counter1 = 1
        for j in self.list_of_class_numbers_phone:
            
            if j == int(self.level_of_button_phone[0]):
                button_row = counter1
            
            counter1+=1

        class_button.grid(row=button_row,column=button_column,padx=2,pady=2)

        if self.max_row_phone < button_row:
            self.max_row_phone = button_row
        #print(button_row)
    #____________________________________________________________________________________________________________
    def show_info_delete_class_version(self):

        self.info_screen_del = Tk()
        self.info_screen_del.title("Wp Automation by ika")
        self.info_screen_del.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.info_screen_del.configure(bg="#282d35")
        self.info_screen_del.resizable(False, False)

        

        self.class_folder_del = listdir('C:\wp_automation\data')
        
        self.list_of_class_numbers_del = []
        self.list_of_class_letters_del = []

        for self.class_numbers_del in self.class_folder_del:

            self.class_level_del = re.findall(r'\d+',self.class_numbers_del )

            for k in range(len(self.class_level_del)):
                char = self.class_numbers_del.replace(self.class_level_del[k],"")

            self.list_of_class_letters_del.append(char)

            for i in range(len(self.class_level_del)):
                
                bişey = int(self.class_level_del[i])
                self.list_of_class_numbers_del.append(bişey)

        
        self.list_of_class_letters_del.sort()
        self.list_of_class_numbers_del.sort(reverse=True)

        self.list_of_class_letters_del = list(dict.fromkeys(self.list_of_class_letters_del))
        self.list_of_class_numbers_del = list(dict.fromkeys(self.list_of_class_numbers_del))


        self.max_row_del = 0
        i = 0
        for i in range(len(self.class_folder_del)):

            self.make_the_buttons_delete_class_version(i)

        size_x = self.max_row_del * 53
        
        self.center_window(750,size_x,self.info_screen_del)

    def make_the_buttons_delete_class_version(self,bla):
        
        class_button = Button(self.info_screen_del, text=self.class_folder_del[bla],font="Arial 15",height=1,width=5,bg="grey30",fg="white",command=lambda : self.del_class_command(str(self.class_folder_del[bla])))

        self.level_of_button_del = re.findall(r'\d+',self.class_folder_del[bla] )
    
        for k in range(len(self.level_of_button_del)):

            self.letter_of_button_del = self.class_folder_del[bla].replace(str(self.level_of_button_del[k]),"")
        
        #print(self.class_folder[bla]," letter:",self.letter_of_button ,"     level: ",self.level_of_button)

        counter2 = 1
        for letter in self.list_of_class_letters_del:
            if str(letter) == self.letter_of_button_del:
                button_column = counter2
                break
            counter2 += 1


        counter1 = 1
        for j in self.list_of_class_numbers_del:
            
            if j == int(self.level_of_button_del[0]):
                button_row = counter1
            
            counter1+=1

        class_button.grid(row=button_row,column=button_column,padx=2,pady=2)

        if self.max_row_del < button_row:
            self.max_row_del = button_row
        #print(button_row)
    #____________________________________________________________________________________________________________

    def add_phone_number(self,class_name):
        self.extra_space = 0
        showwarning(title="Wp Automation by ika",message="You must click both students individual buttons and the save button which placed bottom of list!")

        self.phone_number_screen = Tk()
        self.phone_number_screen.title("Wp Automation by ika")
        self.phone_number_screen.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.phone_number_screen.configure(bg="#282d35")
        self.phone_number_screen.resizable(False, False)

        

        self.add_phone_numbers_to_this_dict = wp_automation_backend.read_data_from_file(self,class_name)

        style = ttk.Style(self.phone_number_screen)
        style.configure("Togglebutton.TButton", foreground='black')
        self.phone_number_screen.call("source", 'C:/wp_automation/Azure-ttk-theme-main/Azure-ttk-theme-main/azure.tcl')
        self.phone_number_screen.call("set_theme", "dark")
        style.configure("Entry.TEntry")

        

        self.frame=Frame(self.phone_number_screen,width=50,height=1600,background="#282d35",bg="#282d35",name="frame")
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas=Canvas(self.frame,name="canvas",bg='#282d35',width=500,height=5000)#1570 - 1522 width of an entry: 48 

        bar=Scrollbar(self.frame,orient=VERTICAL)
        bar.pack(side=RIGHT,fill=Y)
        bar.config(command=self.canvas.yview)

        self.canvas.config(width=50,height=1200)
        self.canvas.config(yscrollcommand=bar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)

        self.frame = Frame(self.phone_number_screen)
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)

        

        counter = 1
        entry_array  = []
        button_array = []    

        for self.key in list(self.add_phone_numbers_to_this_dict.keys()):
            
            entry_name = str(list(self.add_phone_numbers_to_this_dict.items())[counter-1][1]['number'])
            """pn_entry =    Entry(self.frame,
                                width=30,
                                fg="white",
                                bg="grey35",
                                bd=2,
                                name=entry_name
                                )"""

            pn_entry = ttk.Entry(self.frame,width=30,name=entry_name,style="Entry.TEntry")

            try:              
                pn_entry.insert(0,str(list(self.add_phone_numbers_to_this_dict.items())[counter][1]['phone_number']))
            except:
                pass



            pn_entry.focus_set()
            
            pn_entry.grid(column=0,row=counter,padx=0,ipady=3,pady=0,sticky=W)
            entry_array.append(pn_entry)
            #print(str(pn_entry))

            pn_button =  Button(self.frame,
                                fg="white",
                                bg="grey30",
                                activebackground='grey35',
                                bd=2,
                                width=40,
                                text=str(list(self.add_phone_numbers_to_this_dict.items())[counter-1][1]['name']),
                                
                                )

                                
            pn_button.grid(column=1,row=counter,padx=0,pady=0,sticky=W)
            button_array.append(pn_button)

            counter +=1


        for i in range(len(button_array)):

            button_array[i].configure(command= lambda e=entry_array[i]: self.add_pn_button(e,str(e)))
            
        
        #save_button = Button(self.frame,text="SAVE",font="Arial_bold",width=51,height=2,bd=3,bg="green2",activebackground="grey35",command=lambda : wp_automation_backend.store_data(self,class_name,self.add_phone_numbers_to_this_dict))
        save_button = ttk.Button(self.frame,text="SAVE",width=51,style="Togglebutton.TButton",command=lambda : wp_automation_backend.store_data(self,class_name,self.add_phone_numbers_to_this_dict))

        save_button.grid(row=0,columnspan=10)

        extra = len(entry_array)-33
        if extra >= 0:
            self.extra_space = 48*extra
        else:
            self.extra_space = 0

        self.canvas.configure(scrollregion=(0,0,50,1522+self.extra_space))

        self.center_window(718,700,self.phone_number_screen)



        #print(self.add_phone_numbers_to_this_dict)
        self.phone_number_screen.mainloop()

    def add_pn_button(self,entry,entry_name):
        
        txt = entry.get()
        student_number = re.findall(r'\d+',entry_name )
        

        if len(txt) == 10 or len(txt) == 11 or len(txt) == 12 or len(txt) == 13: #11 or 10 FOR TURKEY +905530513710
            
            key = str(student_number[0])                                    
            self.add_phone_numbers_to_this_dict[key]['phone_number']= txt

            entry.config(state= "disabled")

            print(self.add_phone_numbers_to_this_dict[key])
            
        else:
            showwarning(title="Wp Automation by ika",message="Enter a valid phone number!")

    def del_class_screen(self):

        self.del_screen = Tk()
        self.del_screen.title("Wp Automation by ika")
        self.del_screen.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.del_screen.configure(bg="#282d35")
        self.del_screen.resizable(False, False)

        self.center_window(345,30,self.del_screen)

        self.del_entry = Entry(self.del_screen,width=35)
        self.del_entry.insert(0, "Which class do you want to remove:")
        self.del_entry.focus_set()
        self.del_entry.pack(side=LEFT)
        self.del_entry.bind("<FocusIn>", self.temp_text)  

        self.del_button =Button(self.del_screen,fg="white",bg='#282d35', text= "Submit",command=self.del_class_command).pack(side=RIGHT)
        
    def del_class_command(self,a):

        #a = self.del_entry.get()
        try:
            remove('C:\wp_automation\data\{}'.format(a))
            #self.del_screen.destroy()
            showinfo(title="Done!", message="{} has deleted.".format(a))

        except:
            showwarning(title="Warning!", message="Something went wrong!")

    def show_info_button(self,class_name):

        self.info_dict = wp_automation_backend.read_data_from_file(self,class_name)
        
        self.info_screen2 = Tk()
        self.info_screen2.title("Wp Automation by ika")
        self.info_screen2.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.info_screen2.configure(bg="#282d35")
        self.info_screen2.resizable(False, False)
        #self.center_window(900,500,self.info_screen2)

        style = ttk.Style(self.info_screen2)
        self.info_screen2.call("source", 'C:/wp_automation/Azure-ttk-theme-main/Azure-ttk-theme-main/azure.tcl')
        self.info_screen2.call("set_theme", "dark")
        style.configure("Treeview.Treeview")

        columns = ('number', 'name', 'phone_number')

        tree = ttk.Treeview(self.info_screen2, columns=columns, show='headings',style="Treeview.Treeview",height=20)

        tree.heading('number', text='Student Numbers')
        tree.heading('name', text='Names')
        tree.heading('phone_number', text='Phone Numbers')

        tree.column('name',width=350)
        contacts = []
        for n in range(len(self.info_dict)):
            
            first_value = list(self.info_dict.values())[n]
            student_name = list(first_value.values())[0]
            student_number = list(first_value.values())[1]

            try:
                phone_number = list(first_value.values())[2]
                contacts.append((f'{student_number}', f'{student_name}', f'{phone_number}'))
            except:
                contacts.append((f'{student_number}', f'{student_name}', f'--'))

                            

        for contact in contacts:
            tree.insert('', END, values=contact)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.info_screen2, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def show_info_button_oldOneWithListbox(self,class_name):#cancelled
        #print(class_name)
        self.info_dict = wp_automation_backend.read_data_from_file(self,class_name)
        
        self.info_screen2 = Tk()
        self.info_screen2.title("Wp Automation by ika")
        self.info_screen2.iconbitmap("C:\wp_automation\icons\icon.ico")
        self.info_screen2.configure(bg="#282d35")
        self.info_screen2.resizable(False, False)


        scrollbar = Scrollbar(self.info_screen2,orient="vertical")
        scrollbar.pack( side = RIGHT, fill = Y )
        student_list = Listbox(self.info_screen2, height=30,width=65,bg="#282d35",fg="white",yscrollcommand = scrollbar.set )

        i = 0
        for i in range(len(self.info_dict)):
            
            

            first_value = list(self.info_dict.values())[i]
            student_name = list(first_value.values())[0]
            student_number = list(first_value.values())[1]

            try:
                phone_number = list(first_value.values())[2]

                txt = str((str(student_number)+"                       ")[:10]+ "{}".format(str(phone_number)) +"     "+student_name+"     ")

                student_list.insert(END,txt )
            except:
                txt = str(str(str(student_number)+"                      ")[:10] +student_name)
                student_list.insert(END,txt )

        
        student_list.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = student_list.yview )

    def progress_bar(self):#no need it is not used right now     

            # root window
        self.pb_root = Tk()
        self.center_window(300,120,self.pb_root)
        self.pb_root.title('Wp Automation by ika')

        self.pb = ttk.Progressbar(
            self.pb_root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        
        self.value_label = ttk.Label(self.pb_root, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)
        
    def update_progress_label(self):
            return f"Current Progress: {self.pb['value']}%"

    def pb_update(self,v):
            
            if self.pb['value'] < 100:
                self.pb['value'] += v
                self.value_label['text'] = self.update_progress_label()

            else:
                showinfo(message='The progress completed!')
                self.pb_root.destroy()

    def start1(self):

        style = ttk.Style(self.ui)
        self.ui.call("source", 'C:/wp_automation/Azure-ttk-theme-main/Azure-ttk-theme-main/azure.tcl')
        self.ui.call("set_theme", "dark")
        

        canvas =Canvas(self.ui, width=1280, height=780,bg="#282d35",)
        canvas.place(x=-10,y=-10)
        canvas.create_line(0,720,1280,720, fill="grey30", width=54)

        with Image.open('C:\wp_automation\icons\icons8-opened-folder-96.png') as img_button_folder :
            img_button_folder.load()

        img_button_folder = img_button_folder.resize((50, 50), Image.ANTIALIAS)
        img_button_folder = ImageTk.PhotoImage(img_button_folder)

        folder_button = Button(
            self.ui,image=img_button_folder,
            borderwidth=0,
            bg="grey30",
            activebackground='grey30',
            #compound = LEFT,
            #text="Open File",
            #font=('Arial',25)
            command=self.select_file
            )
        
        with Image.open('C:\wp_automation\icons\icons8-info-96.png') as img_button_info :
            img_button_info.load()

        img_button_info = img_button_info.resize((50, 50), Image.ANTIALIAS)
        img_button_info = ImageTk.PhotoImage(img_button_info)

        info_button = Button(
            self.ui,image=img_button_info,
            borderwidth=0,
            bg="grey30",
            activebackground='grey30',
            #compound = LEFT,
            #text="Open File",
            #font=('Arial',25)
            command=self.show_info
            )

        with Image.open('C:\wp_automation\icons\del_bin.png') as del_image :
            del_image.load()

        del_image = del_image.resize((40, 40), Image.ANTIALIAS)
        del_image = ImageTk.PhotoImage(del_image)

        delete_button = Button(self.ui,image=del_image ,borderwidth=0,bg="grey30",activebackground="grey30",command=self.show_info_delete_class_version)#del_class_screen
        

        with Image.open('C:\wp_automation\icons\phone_add.png') as phone_image :
            phone_image.load()

        phone_image = phone_image.resize((40, 40), Image.ANTIALIAS)
        phone_image = ImageTk.PhotoImage(phone_image)

        phone_button = Button(self.ui,image=phone_image ,borderwidth=0,bg="grey30",activebackground="grey30",command=self.show_info_phone)

        style.configure("Accentbutton.TButton", foreground='black')
        style.configure("send.TButton", foreground='black',background='green')
        style.configure("Togglebutton.TButton", foreground='white')
        style.configure("Entry.TEntry")
        style.configure("TNotebook.TNotebook")
        style.configure("label.TLabel")

        	

        self.list_of_receivers = []
        self.list_of_labels = []
        self.notebook_row = 0
        self.notebook_column = 0


        def add_to_receivers():
            
            receiver = self.absenteeism_entry.get()

            if receiver == "":
                showwarning(title="Warning",message="Invalid input!")

            elif receiver.isnumeric():
                self.list_of_receivers.append(receiver) 

                eren = Label(frame1,text="•"+ receiver)
                eren.grid(row=self.notebook_row,column=self.notebook_column)
                self.list_of_labels.append(eren)
                self.notebook_column += 1

            if self.notebook_column%4 == 0:
                self.notebook_row += 1
                self.notebook_column = 0

            print(self.list_of_receivers)          
            self.absenteeism_entry.delete(0,"end")

        
        def del_receiver_button():

            try:
                self.list_of_receivers.clear()
                for y in range(len(self.list_of_labels)):
                    self.list_of_labels[y].destroy() 
                self.notebook_column = 0
                self.notebook_row = 0
            except: 
                pass

  
            print(self.list_of_receivers)


            # print(self.list_of_labels)

        def send_message_button():
            showwarning(title="Warning!",message="This operation may take long time!\nYou must not do something on your pc when it is working!")
            classes = listdir('C:\wp_automation\data')
            for p in classes:
                check_dict = wp_automation_backend.read_data_from_file(self,p)

                for r in self.list_of_receivers:

                    try:#checks for the class

                        student = check_dict[r]
                        #print(f"{student} , {p} , {r}")
                        try:
                            phone_number = check_dict[r]['phone_number']
                            print(f"{r}'s phone number is: {phone_number}")
                            wp_automation_backend.send_wp_message_instant(self,f"{str(check_dict[r]['name'])} did not come school today!",str(phone_number))

                        except:
                            print(f"{p},{r} has no phone number entered!")
                            showwarning(title="Warning!",message=f"{r} has no phone number entered! ({p})")
                    except:
                        #print("except worked")
                        pass
                    
                    """try:
                        #print(str(p) +" "+str(check_dict[r]))
                        phone_number = check_dict[r]['phone_number']
                        print(f"{r}'s phone number is: {phone_number}")
                        #self.list_of_receivers.remove(r)
                    except:
                        print(f"{p},{r} has no phone number entered!")
                        pass"""
                        
            del_receiver_button()

        


        send_button = ttk.Button(self.ui,width=10,text= "Send",style="send.TButton",command= lambda : send_message_button())
        delete_receiver_button = ttk.Button(self.ui,width=10,text= "Clear",style="Accentbutton.TButton",command= lambda : del_receiver_button())
        

        absenteeism_add_button = ttk.Button(self.ui,text= "Add",style="Accentbutton.TButton",command=lambda : add_to_receivers())
        self.absenteeism_entry = ttk.Entry(self.ui, style="Entry.TEntry",width=11)
        self.absenteeism_entry.bind('<Return>',lambda a : add_to_receivers())


        for x in self.list_of_receivers:
            print(x)

        notebook = ttk.Notebook(self.ui,style="TNotebook.TNotebook")
        
        frame1 = ttk.Frame(notebook, width=225, height=510)#510
        frame1.pack(fill='both', expand=True)
        frame1.grid_propagate(False)
        notebook.add(frame1, text='Receivers')

       
        main_screen_label1 = ttk.Label(self.ui,style="label.TLabel",font=("arial" ,13),text="Absenteeism Message:")

        #switch1 = ttk.Checkbutton(self.ui,text="switch1",style="TCheckbutton")
        
        notebook2 = ttk.Notebook(self.ui,style="TNotebook.TNotebook")
        frame2 = ttk.Frame(notebook2, width=510, height=225)#510
        frame2.pack(fill='both', expand=True)
        frame2.grid_propagate(False)
        notebook2.add(frame2, text='Message')

        text_box = Text(frame2,font=('Calibri'),height=10)


        folder_button.place(x=5, y=685)
        info_button.place(x=70,y=683)
        delete_button.place(x=133,y=688)
        phone_button.place(x=190,y=688)

        send_button.place(x=5,y=80)
        delete_receiver_button.place(x=125,y= 80)
        notebook.place(x=5,y=125)
        self.absenteeism_entry.place(x=5,y=35)
        absenteeism_add_button.place(x=125,y=35)

        main_screen_label1.place(x=5,y=5)
        #notebook2.place(x=250,y=5)
        #text_box.pack()
        #switch1.place(x=5,y=525)
    
        """
            yapılıcaklar:

            ✓• Devamsızlık mesajı 

            2x (anlık/ileri tarihli)
            • Herkese mesaj yolla
            • Belirli sınıfa mesaj yolla
            • belirli bir sınıf düzeyine mesaj yolla
            • gruba mesaj yolla
            • bir kişiye yolla 
        """
        self.ui.mainloop()

    def temp_text(self,e):
        self.del_entry.delete(0,"end")



class wp_automation_backend(wp_automation_frontend):

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = r'C:\wp_automation\tesseract\tesseract.exe'# The path of tesseract.exe it turn's image into text
         


    def img_manipulation(self,img_path):# Take's students info as photo

        self.img_path = img_path #"C:\wp_automation\A.jpg"
        
        with Image.open(self.img_path) as img:
            img.load()

        img = img.resize((1500,2100))# resize image for cropping

        x1 = 0
        x2 = 1500
        y1 = 350
        y2 = 1850

        img= img.convert('RGB')

        cropped_img = img.crop((x1, y1, x2, y2))
        limit = y2/30.385
        y_sum = 0

        self.list_name = []
        self.list_number = []
        scale = 1.8

        #percentage = 100/int(limit)
        #progress_value = 0
        #self.progress_bar()

        for i in range(int(limit)):

            student_name = cropped_img.crop((350, y_sum, 1250, y_sum+30.385))
            #student_name.show()
            self.list_name.append(student_name)



            student_number = cropped_img.crop((120, y_sum, 350, y_sum+30.385))


            #student_number.show()
            self.list_number.append(student_number)
            i_width = student_number.size[1] * scale
            i_height = student_number.size[0] * scale
            student_number = student_number.resize((int(i_width), int(i_height)), Image.BILINEAR)
            y_sum += 30.385
            
            #progress_value += percentage
            #self.pb_update(progress_value)

        #print(self.list)
        
    def read_from_img(self,class_name):

        self.dict = {}
        self.error = []

        
        self.class_name  = class_name 

        for i in range(len(self.list_name)):

            name = pytesseract.image_to_string(self.list_name[i], lang="tur")
            number = pytesseract.image_to_string(self.list_number[i], config="-c page_separator=''") #"--psm 6 digits" can be used

            if number == "":
                if name != "":
                    self.error.append(" ".join(name.split()))
            else:
                self.dict["{}".format(" ".join(number.split()))] = {'name': '{}'.format(" ".join(name.split())), 'number': "{}".format(" ".join(number.split()))}
            
        #print(self.dict)
        #print(self.error)
    

    def fix_number_errors_button(self):

        self.entered_student_number = self.fix_entry.get()

        self.dict["{}".format(self.entered_student_number)] = {'name': '{}'.format(" ".join(self.error[0].split())), 'number': "{}".format(self.entered_student_number)}
        #print(self.dict)
        del self.error[0]
        
        self.fix_screen.destroy()
        
        if len(self.error) !=0:
            self.fix_number_errors()

        else:
            global entered_class_name
            showinfo(title="Wp Automation by ika",message="All students of {} correctly added to the system.".format(entered_class_name))
            wp_automation_backend.store_data(self,str(self.class_name),self.dict)


    def temp_text1(self,e):
        self.fix_entry.delete(0,"end") 


    def fix_number_errors(self):

        if len(self.error) !=0:

            showwarning(title="Warning!", message="There are numbers program couldn't read. Enter them by hand!\n\nWhat are the numbers of these students?\n{}".format(self.error))
             
            self.fix_screen = Tk()
            self.fix_screen.title("Wp Automation by ika")
            self.fix_screen.iconbitmap("C:\wp_automation\icons\icon.ico")
            self.fix_screen.configure(bg="#282d35")
            self.fix_screen.resizable(False, False)
            self.fix_screen.geometry('300x50')
                
            self.fix_button =Button(self.fix_screen,fg="white",bg='#282d35', text= "Submit",command=self.fix_number_errors_button).pack(side=RIGHT)

            self.fix_entry = Entry(self.fix_screen,width=200)
            self.fix_entry.insert(0, "{}".format(self.error[0]))
            self.fix_entry.focus_set()
            self.fix_entry.pack(side=LEFT)
            self.fix_entry.bind("<FocusIn>", self.temp_text1)
                

    def store_data(self,file_name,data):
        
        try:
                    
            file = open('C:\wp_automation\data\{}'.format(file_name), 'wb')
            pickle.dump(data, file)
            file.close()
            showinfo(title="Wp Automation by ika",message="Saved Successfuly.")
        except:
            print("Something went wrong")


    def read_data_from_file(self,read_file):

        self.read_file = read_file

        pickle_in = open("C:\wp_automation\data\{}".format(self.read_file),"rb")
        self.new_dict = pickle.load(pickle_in)
        #print(self.new_dict)

        return self.new_dict
        


    def send_wp_message_instant(self,message,receiver):

        check = False
        if receiver[0] == '+' and len(receiver) == 13:
            check = True

        elif receiver[0] == '9' and len(receiver) == 12:

            receiver = '+' + receiver
            check = True
        
        elif receiver[0] == '0' and len(receiver) == 11:

            receiver = '+9' + receiver
            check = True
        
        elif receiver[0] == '5' and len(receiver) == 10:
            
            receiver = '+90' + receiver
            check = True
        
        else:
            showwarning(message="Invalid Phone Number!")
        
        
        if check:
            pywhatkit.sendwhatmsg_instantly(receiver,"{}".format(message),20,tab_close=True)

        

    def send_wp_message_later(self,message,receiver,hour,minute):

        check = False
        if receiver[0] == '+' and len(receiver) == 13:
            check = True

        elif receiver[0] == '9' and len(receiver) == 12:

            receiver = '+' + receiver
            check = True
        
        elif receiver[0] == '0' and len(receiver) == 11:

            receiver = '+9' + receiver
            check = True
        
        elif receiver[0] == '5' and len(receiver) == 10:
            
            receiver = '+90' + receiver
            check = True
        
        else:
            showwarning(message="Invalid Phone Number!")
        
        
        if check:
            pywhatkit.sendwhatmsg(receiver,"{}".format(message),time_hour= hour, time_min= minute,wait_time=20)
        

    
    def get_time(self):
        now = datetime.datetime.now()
        self.current_time_hour    = now.strftime("%H")
        self.current_time_minute  = now.strftime("%M")
        self.current_time_second  = now.strftime("%S")

        self.time ="Current Time = {}:{}:{}".format(self.current_time_hour,self.current_time_minute,self.current_time_second)





    def start2(self):

        if __name__ == "__main__":

            run = wp_automation_backend()
            run.img_manipulation(self.image_path)
            run.read_from_img(self.entered_class_name)#class_name
            run.fix_number_errors()
            #run.store_data()
            #run.read_data_from_file("{}".format(self.entered_class_name))

#program1 = wp_automation_backend()
#program1.start()



program2 = wp_automation_frontend()
program2.start1() 
