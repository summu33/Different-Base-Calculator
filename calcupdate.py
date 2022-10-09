#importing needed libraries 
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

eq,oprn,oprt='',[],[]
check,ocheck=0,0
def Delete():
    """Function that backspace a character on clicking - delete- button"""
    global eq
    eq=eq[:-1]
    E1.delete(0,'end')
    E1.insert(0,eq)

def Exit():
    key.destroy()

    
def Expression(ele):
    """collect the letters and form the expression"""
    global eq
    eq+=ele
    E1.delete(0,'end')
    E1.insert(0,eq)

     
def Clear():
    """Clear the full expression"""
    global oprn
    global oprt
    global eq
    eq=''
    oprn.clear()
    oprt.clear()
    E1.delete(0,'end')

def Start():
    """ Occurs on clicking the "=" button .The functiom which defined as to valid all user selecting
        infromations that they are select correctly or no """
    
    if typ1.get()=='Select:-':
        messagebox.showwarning("WARNING","Please select the input type !")

    elif typ2.get()=='Select:-':
        messagebox.showwarning("WARNING","Please select the output type !")
        
    elif typ3.get()=='Select:-':
        messagebox.showwarning("WARNING","Please select the operation mode !")

    else:
        return Performer()
 
def Performer():
    """Collect the input type and operation type from the entries
       and perform function calls according to them"""
    try:
        global eq

        if (typ1.get()=='DECIMAL' and typ3.get()=='(Mathematical + Logical) Expressions'):
            eq=str(eval(eq))
            return Fina_Display()

        elif (typ1.get()=='HEXADECIMAL' or typ1.get()== 'BINARY' or typ1.get()=='OCTAL') and (typ3.get()=='(Mathematical + Logical) Expressions'):
            return Transformer()

        elif (typ3.get()=='Conversions'):
            return Conversion()
    except:
        messagebox.showerror("Wrong Selection !","You have selected the wrong operation type !\nPlease select the operation type according to mathematical expression .")
     

        
        
    
def Transformer():
    '''A main function of the program. it call when only "Complex Operations" occurs.
       it perform manipulation in the expression like seperate a operators,operands from the expression
       then convert geted operands into decimals then merge them and then calculate the result
       by eval() funtion'''
    try:
        global eq
        oprt,iden,ind,OP_count=[],'NO',0,0
        temp_lst=list(eq) #creat a list of given Expression to manipulate it
        for i in range(len(temp_lst)):
            if temp_lst[i] in ['+','-','*','/','&','~' ,'|','<','>','^']: #checking for operators
                if temp_lst[i]=='<':
                    oprt.append('<<');temp_lst[i]='O'

                elif temp_lst[i]=='>':
                    oprt.append('>>'); temp_lst[i]='O'

                else:
                    oprt.append(temp_lst[i]);temp_lst[i]='O' #extract the operators in a new list and remark their locations with 'O' symbol\


        new_list=''.join(temp_lst) #converting the geted list into a full expression
        oprn=new_list.split('O') #spliting that expression from the 'O' symbol by which easly extract the operands

        if '' in oprn:  #checking if any unary operator is used then identify his index by which we can place on there after operand operations .
            ind=oprn.index('')
            iden='YES'
            oprn.remove('')
        else:
            pass

 #Checking the input type selected by the user by which can convert it according to it by function calling them.
        if typ1.get()=='BINARY':
            oprn=Binary_Convert(oprn)

        elif typ1.get()=='HEXADECIMAL':
            oprn=Hexa_Convert(oprn)

        elif typ1.get()=='OCTAL':
            oprn=Octa_Convert(oprn)
        else:
            pass
        

        oprn.insert(ind,'') if iden=='YES' else 0#inserting the unary identity at their original place
        print(oprn)
        new_expr='O'.join(oprn) #to make new expression , join geted opernd list with Identity 'O' bye which we can identify where the operator are placed
        new_expr=list(new_expr)

        for i in range(len(new_expr)):
            if new_expr[i]=='O':
                new_expr[i]=oprt[OP_count];OP_count+=1
        eq=''.join(new_expr) #Making the new equation with converted numbers
        eq=str(eval(eq)) #Solving the Equation and getting the answer
        Fina_Display() #Call a funtion to display the result ..
    except :
        messagebox.showerror("Error !","Something went wrong !/Syntax Error !")
        
    
    
# and (typ1.get()=='BINARY' or typ1.get()=='HEXADECIMAL')
#and typ1.get()=='DECIMAL'


   
def Binary_Convert(oprnd_list):
    '''Function that take a list of numbers(operands) as a argument & convert
       the number of that list from binary values to decimal values by which
       easly perform the "eval()" method and return a modified list'''
    for i in range(len(oprnd_list)):
        oprnd_list[i]=Binary_Knower(oprnd_list[i]) #it calls a special function that convert the binary into decimal according to its floating point status.
    return oprnd_list


    
def Hexa_Convert(oprnd_list):
    '''Function that take a list of numbers(operands) as a argument & convert
       the number of that list from hexadecimal values to decimal values by which
       easly perform the "eval()" method and return a modified list'''
    
    for i in range(len(oprnd_list)):
        oprnd_list[i]=str(int(oprnd_list[i],16))
    return oprnd_list


def Octa_Convert(oprnd_list):
    '''Function that take a list of numbers(operands) as a argument & convert
       the number of that list from octal values to decimal values by which
       easly perform the "eval()" method and return a modified list'''
    
    for i in range(len(oprnd_list)):
        oprnd_list[i]=str(int(oprnd_list[i],8))
    return oprnd_list

    

   
def Cut_Part(str1):
    """Perfrom cutting binary parts from '.' in floating
       point binary"""
    str2=''
    for i in str1:
        if i=='.' or i=='':
            break
        else:
            str2+=i
    return str2

    
def Binary_Knower(Binary):
 """ Identify the given binary that is floating point binary
     or simple binary and convert it according to it's corresponding integer number"""
 try:
    no,sum1=1,0
    if '.' not in Binary:
        return str(int(Binary,2))
    elif '.' in Binary:
        bin_part1=Cut_Part(Binary)
        Binary=list(Binary)
        Binary.reverse()
        bin_part2=Cut_Part(Binary)
        for i in bin_part2[::-1]:
            if i=='1':
                sum1+=(1/(2**no))
            no+=1
        x=(int('0'+bin_part1,2)+sum1)
        return(str(x))
    else:
        pass

 except:
    messagebox.showerror("Error !","Syntax Error !")



def Float_Binary_Calcu(number):
 """compute the binary of floating point decimal number in the form
    of floating point binary"""
 try:
    b=0
    rp=''
    int_part=int(number);flo_part=number-int_part
    int_part=bin(int_part);lft_bin=int_part.replace('0b','')
    x=1
    count=0
    while(x!=0 and count<=9):
        if(x==1):
            x=flo_part
        x=x*2;b=int(x)
        x-=b;rp=rp+str(b)
        count+=1

    l=lft_bin+'.'+rp
    return(l)

 except:
    check=1
    messagebox.showerror("Error !","Syntax Error !")
    return ''


def Fina_Display():
    '''Function used to display the output/result
       of the expression according to user selected output
       option'''
    
    global eq
    if typ2.get()=='DECIMAL':
        pass
    
    elif typ2.get()=='HEXADECIMAL':
        eq=str(hex(int(eq))).replace('0x','')
        
    elif typ2.get()=='BINARY':
        if '.' in eq: #Checking if number is floatingpoint then convert it into floating point binary.
            eq=Float_Binary_Calcu(float(eq))
        else:
            eq=str(bin(int(eq))).replace('0b','')
            
    elif typ2.get()=='OCTAL':
        eq=str(oct(int(eq))).replace('0o','')

    else:
        pass

    E1.delete(0,'end')
    E1.insert(0,eq)
        

def Conversion():
    '''Function for the simple conversion purpose by which convert
       all inputed numbers into decimal then convert them according to user
       by calling Fina_Display function'''
    
    global eq
    if typ1.get()=='DECIMAL':
        pass
    elif typ1.get()=='HEXADECIMAL':
        eq=str(int(eq,16))
    elif typ1.get()=='OCTAL':
        eq=str(int(eq,8))
    elif typ1.get()=='BINARY':
        eq=Binary_Knower(eq)
    else:
        pass

    return Fina_Display()
        
        
def Welcome():
   """A Welcome & introduction function that exe.. first""" 
   messagebox.showinfo("CAUTION",""" Welcome To All Number System Solver Application. We would be glad that this could do some work for you..\n\n->: Select the Operation , input & output type and mode before the calculation.\n\n\n\n\nThank you ....HAVE A NICE DAY..""")
   dis = messagebox.askquestion("Confirmation","Do you want to read again the caution ?")
   if dis =='no':
       pass
   else:
       return Welcome()

#code for GUI building

key=Tk() #Creating the root element for the tkinter window.
key.state('zoomed') #open full size window with titles
key.geometry('1280x1280') #Given the size of default opening window.
key.title('Calculator By Sumit Kumar') #declaring title to the window
key.configure(bg='silver')

#Settings for the adding background image
path='C:/Users/wave/Desktop/Internet Explorer/bg10.jpg' #define the path of the image
imgg=Image.open(path) #Access the image and store it into a variable
imgg=imgg.resize((1400,650))
imag=ImageTk.PhotoImage(imgg)
lbl=Label(image=imag) #placing the image in the window as a label
lbl.pack() #packing the label

#Creating the top heading/name of the application
l0=Label(key,text='  all number system solver  ',font='algerian 25',bd=10,bg='black',fg='aquamarine')
l0.place(anchor='center',relx=.5,rely=.07) #Sets that heading in the tkinter window


 #Creating informative labels for user
ttk.Label(key,text='     select the input / output mode    ',background='royalblue',foreground='purple',font='algerian 15').place(anchor='center',relx=.78,rely=.25)
ttk.Label(key,text='     input type    ',background='royalblue',foreground='purple',font='algerian 15').place(anchor='center',relx=.67,rely=.32)
ttk.Label(key,text='    output type   ',background='royalblue',foreground='purple',font='algerian 15').place(anchor='center',relx=.9,rely=.32)

#Creating the list for input format options to selecting from the user.
typ1 = ttk.Combobox(key, textvariable=StringVar(),values=['Select:-','DECIMAL','BINARY','HEXADECIMAL','OCTAL'],state= 'readonly')
typ1.place(anchor='center',relx=.67,rely=.38,width=175,height=25)
typ1.current(0) #Set a first value to show in the list default.


lbl=Label(key,text='to',bd=5,font='algerian 15',bg='royalblue',fg='lime')
lbl.place(anchor='center',relx=.79,rely=.32)

#Creating the list for output format options to selecting from the user.
typ2 = ttk.Combobox(key, textvariable=StringVar(),values=['Select:-','DECIMAL','BINARY','HEXADECIMAL','OCTAL'],state= 'readonly')
typ2.place(anchor='center',relx=.9,rely=.38,width=175,height=25)
typ2.current(0)  #Set a first value to show in the list default.

#Creating the list for operation options to selecting from the user.
ttk.Label(key,text='   select the operation type   ',background='royalblue',foreground='purple',border=8,font='algerian 15').place(anchor='center',relx=.78,rely=.57)
typ3 = ttk.Combobox(key, textvariable=StringVar(),values=['Select:-','Conversions','(Mathematical + Logical) Expressions'],state= 'readonly')
typ3.place(anchor='center',relx=.78,rely=.63,width=250,height=25)
typ3.current(0) #Set a first value to show in the list default.

#Creating the display of the calculator.
E1=Entry(key,bd=8,font='algerian 18',justify=RIGHT,bg='slate gray4',fg='old lace')
E1.place(anchor='center',relx=.378,rely=.32,height=90,width=400)

#Creating the Buttons of digits and needed symbols for the calculations...
b0=Button(key,text='1',font='algerian 20',command=lambda: Expression('1'),fg='lime',bg='navy')
b0.place(anchor='center',relx=.25,rely=.45,width=60,height=60)

b1=Button(key,text='2',font='algerian 20',command=lambda: Expression('2'),fg='lime',bg='navy')
b1.place(anchor='center',relx=.30,rely=.45,width=60,height=60)

b2=Button(key,text='3',font='algerian 20',command=lambda: Expression('3'),fg='lime',bg='navy')
b2.place(anchor='center',relx=.35,rely=.45,width=60,height=60)

b3=Button(key,text='+',font='algerian 20',command=lambda: Expression('+'),fg='lime',bg='navy')
b3.place(anchor='center',relx=.40,rely=.45,width=60,height=60)

b4=Button(key,text='-',font='algerian 20',command=lambda: Expression('-'),fg='lime',bg='navy')
b4.place(anchor='center',relx=.45,rely=.45,width=60,height=60)

b5=Button(key,text='cl',font='algerian 20',command=lambda: Clear(),bg='mediumpurple')
b5.place(anchor='center',relx=.50,rely=.45,width=60,height=60)

b6=Button(key,text='4',font='algerian 20',command=lambda: Expression('4'),fg='lime',bg='navy')
b6.place(anchor='center',relx=.25,rely=.55,width=60,height=60)

b7=Button(key,text='5',font='algerian 20',command=lambda: Expression('5'),fg='lime',bg='navy')
b7.place(anchor='center',relx=.30,rely=.55,width=60,height=60)

b8=Button(key,text='6',font='algerian 20',command=lambda: Expression('6'),fg='lime',bg='navy')
b8.place(anchor='center',relx=.35,rely=.55,width=60,height=60)

b9=Button(key,text='x',font='algerian 20',command=lambda: Expression('*'),fg='lime',bg='navy')
b9.place(anchor='center',relx=.40,rely=.55,width=60,height=60)

b10=Button(key,text='/',font='algerian 20',command=lambda: Expression('/'),fg='lime',bg='navy')
b10.place(anchor='center',relx=.45,rely=.55,width=60,height=60)

b11=Button(key,text='.',font='algerian 20',command=lambda: Expression('.'),fg='lime',bg='navy')
b11.place(anchor='center',relx=.50,rely=.55,width=60,height=60)

b12=Button(key,text='7',font='algerian 20',command=lambda: Expression('7'),fg='lime',bg='navy')
b12.place(anchor='center',relx=.25,rely=.65,width=60,height=60)

b13=Button(key,text='8',font='algerian 20',command=lambda: Expression('8'),fg='lime',bg='navy')
b13.place(anchor='center',relx=.30,rely=.65,width=60,height=60)

b14=Button(key,text='9',font='algerian 20',command=lambda: Expression('9'),fg='lime',bg='navy')
b14.place(anchor='center',relx=.35,rely=.65,width=60,height=60)

b15=Button(key,text='f',font='algerian 20',command=lambda: Expression('F'),fg='lime',bg='navy')
b15.place(anchor='center',relx=.40,rely=.65,width=60,height=60)

b16=Button(key,text='e',font='algerian 20',command=lambda: Expression('E'),fg='lime',bg='navy')
b16.place(anchor='center',relx=.45,rely=.65,width=60,height=60)

b17=Button(key,text='a',font='algerian 20',command=lambda: Expression('A'),fg='lime',bg='navy')
b17.place(anchor='center',relx=.25,rely=.75,width=60,height=60)

b18=Button(key,text='0',font='algerian 20',command=lambda: Expression('0'),fg='lime',bg='navy')
b18.place(anchor='center',relx=.30,rely=.75,width=60,height=60)

b19=Button(key,text='b',font='algerian 20',command=lambda: Expression('B'),fg='lime',bg='navy')
b19.place(anchor='center',relx=.35,rely=.75,width=60,height=60)

b20=Button(key,text='c',font='algerian 20',command=lambda: Expression('C'),fg='lime',bg='navy')
b20.place(anchor='center',relx=.40,rely=.75,width=60,height=60)

b21=Button(key,text='d',font='algerian 20',command=lambda: Expression('D'),fg='lime',bg='navy')
b21.place(anchor='center',relx=.45,rely=.75,width=60,height=60)

b22=Button(key,text='=',font='algerian 20',command=lambda: Start(),bg='azure4')
b22.place(anchor='center',relx=.50,rely=.70,width=60,height=130)

b23=Button(key,text='exit',font='algerian 15',command=lambda: Exit(),bg='red')
b23.place(anchor='center',relx=.33,rely=.87,width=70,height=55)

b24=Button(key,text='del',font='algerian 15',command=lambda: Delete(),bg='thistle1')
b24.place(anchor='center',relx=.41,rely=.87,width=70,height=55)

b25=Button(key,text='&',font='algerian 15',command=lambda: Expression('&'),bg='sky blue' )
b25.place(anchor='center',relx=.69,rely=.72,width=70,height=50)

b26=Button(key,text='|',font='algerian 15',command=lambda: Expression('|'),bg='sky blue')
b26.place(anchor='center',relx=.75,rely=.72,width=70,height=50)

b27=Button(key,text='~',font='algerian 18',command=lambda: Expression('~'),bg='sky blue')
b27.place(anchor='center',relx=.81,rely=.72,width=70,height=50)

b28=Button(key,text='^',font='algerian 15',command=lambda: Expression('^'),bg='sky blue')
b28.place(anchor='center',relx=.69,rely=.80,width=70,height=50)

b29=Button(key,text='<<',font='algerian 15',command=lambda: Expression('<'),bg='sky blue')
b29.place(anchor='center',relx=.75,rely=.80,width=70,height=50)

b30=Button(key,text='>>',font='algerian 15',command=lambda: Expression('>'),bg='sky blue')
b30.place(anchor='center',relx=.81,rely=.80,width=70,height=50)

Welcome()#calling the Welcome function for starting with greetings

key.mainloop()


     
