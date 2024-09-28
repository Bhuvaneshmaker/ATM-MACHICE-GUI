from tkinter import *
import tkinter.font as font
import random

#Creating Bhuvanesh ATM new window

window = Tk()
window.title("BHUVANESH ATM")
window.geometry("600x500")

font_01= font.Font(family='Times', size=40, weight='bold', slant='italic') 
style_01 = font.Font(family='Courier', size=20, weight='bold')   
style_02 = font.Font(family='Courier', size=15, weight='bold')   
check_count = 0

# show message after selecting no    

def show_func():
    qustn_func.qustn_win.withdraw()
    show_win = Toplevel(window)
    show_win.geometry("600x500")
    msg =  Message(show_win, text='\n\nYour transaction has been successful...\n\nThank you for using our' ,font=style_01, fg="#6439FF",bg='white')
    msg.pack()
    txt =  Label(show_win, text='BHUVANESH ATM ☺...', font=font_01,fg="#6439FF")
    txt.pack()

    quit_btn = Button(show_win, text='EXIT', font=style_02,bg="black", fg='red', command=lambda: window.destroy())
    quit_btn.pack(side=BOTTOM,pady=10)

# window asking to show balance or not

def qustn_func():
    global check_count
    check_count+=1

    withdrawal_func.withdrawal_win.withdraw()
    qustn_func.qustn_win =Toplevel(window)
    qustn_func.qustn_win.geometry('600x500') 

    frame_1 = Frame(qustn_func.qustn_win)
    frame_1.pack(side=BOTTOM)

    msg_box = Message(qustn_func.qustn_win,text='\nYour transaction has been successful!!!\n\nPlease collect your money...\n\nYou can remove your card...\n\nDo you want to check your balance???', font=style_02,fg="#6439FF",bg='white')
    msg_box.pack(pady=40)

    btn_yes = Button(frame_1, text='YES', font=style_02,bg="black", fg='green', command=balance_func)
    btn_yes.pack(side=LEFT,pady=60)

    btn_no = Button(frame_1, text='NO', font=style_02,bg="black", fg='green', command=show_func)
    btn_no.pack(pady=60 , padx =20)

#Money withdrawal window makes 
def withdrawal_func():

    option_func.option_win.withdraw()
    withdrawal_func.withdrawal_win = Toplevel(window)
    withdrawal_func.withdrawal_win.geometry('600x500')

    enter_lbl = Label(withdrawal_func.withdrawal_win, text='\nPlease enter amount : \n', font=style_01,fg="#6439FF")
    enter_lbl.pack()
    money_entry = Entry(withdrawal_func.withdrawal_win, font=style_02, justify='center')
    money_entry.pack()


    bf = Frame(withdrawal_func.withdrawal_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(withdrawal_func.withdrawal_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(withdrawal_func.withdrawal_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(withdrawal_func.withdrawal_win)
    bf1.pack(side=BOTTOM)

    btn1 = Button(bf1, text='1', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '1'))
    btn1.pack(side=LEFT, pady=10)

    btn2 = Button(bf1, text='2', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '2'))
    btn2.pack(side=LEFT, padx=10)

    btn3 = Button(bf1, text='3', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '3'))
    btn3.pack(side=LEFT)

    btn4 = Button(bf2, text='4', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '4'))
    btn4.pack(side=LEFT)

    btn5 = Button(bf2, text='5', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '5'))
    btn5.pack(side=LEFT, padx=10)

    btn6 = Button(bf2, text='6', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '6'))
    btn6.pack(side=LEFT)

    btn7 = Button(bf3, text='7', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '7'))
    btn7.pack(side=LEFT, pady=10)

    btn8 = Button(bf3, text='8', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '8'))
    btn8.pack(side=LEFT, padx=10)

    btn9 = Button(bf3, text='9', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '9'))
    btn9.pack(side=LEFT)

    btn_1 = Button(bf4, text='*', font=style_02,bg="black",fg="white",command=lambda: money_entry.insert('end', '*'))
    btn_1.pack(side=LEFT)

    btn0 = Button(bf4, text='0', font=style_02,bg="black",fg="white", command=lambda: money_entry.insert('end', '0'))
    btn0.pack(side=LEFT, padx=10)

    btn_2 = Button(bf4, text='#', font=style_02,bg="black",fg="white",command=lambda: money_entry.insert('end', '#'))
    btn_2.pack(side=LEFT)

    btn_enter = Button(bf, text='ENTER', font=style_02,bg="black", fg='green', command=qustn_func)
    btn_enter.pack(side=LEFT, pady=10)

    btn_clear = Button(bf, text='CLEAR', font=style_02,bg="black", fg='orange', command=lambda: money_entry.delete(1))
    btn_clear.pack(side=LEFT, padx=10)




# balance displaying window
def balance_func():

    global check_count

    if check_count == 1:
        qustn_func.qustn_win.withdraw()

    option_func.option_win.withdraw()
    balance_win = Toplevel(window)
    balance_win.geometry('600x500')
    #balance_win.grab_set()
    balance = random.randrange(1000,1000000)
    message = Message(balance_win,text='\nYour transaction is successful....\n\nAvailable Balance : '+str(balance)+'\n\nThank you for using our', font=style_01,fg="#6439FF",bg='white')
    message.pack(pady=30)
    text = Label(balance_win, text='BHUVANESH ATM ☺...', font=font_01, bg="#6439FF", fg='skyblue')
    text.pack(pady=20)

    btn_exit = Button(balance_win, text='EXIT', font=style_02,bg="black", fg='red', command=lambda: window.destroy())
    btn_exit.pack(side=BOTTOM, pady=10)


# displays message after change has been changed
def message_func():
    change_pin_func.change_pin_win.withdraw()
    window_2 = Toplevel(window)
    window_2.geometry('600x500')
    message = Message(window_2, text='\nYour transaction is successful...\n\nYour PIN has been successfully changed...\n\nThank you for using our', font=style_01, fg="#6439FF",bg='white')
    message.pack(pady=20)
    text = Label(window_2, text='BHUVANESH ATM ☺...', font=font_01, bg="#6439FF", fg='skyblue')
    text.pack(pady=30)

    exit_button = Button(window_2, text='EXIT', font=style_02,bg="black", fg='red', command=lambda: window.destroy())
    exit_button.pack(side=BOTTOM, pady=10)


# changing pin function
def change_pin_func():
    option_func.option_win.withdraw()
    change_pin_func.change_pin_win = Toplevel(window)
    change_pin_func.change_pin_win.geometry('600x500')

    pin_lbl = Label(change_pin_func.change_pin_win, text='\nEnter new-PIN :', font=style_02, fg="#6439FF")
    pin_lbl.pack()
    pin_entry = Entry(change_pin_func.change_pin_win, font=style_02,justify='center', show='*')
    pin_entry.pack()

    re_entry_lbl = Label(change_pin_func.change_pin_win, text='\nRe-enter new-PIN :', font=style_02, fg="#6439FF")
    re_entry_lbl.pack()
    re_entry = Entry(change_pin_func.change_pin_win, font=style_02, justify='center', show='*')
    re_entry.pack()

    bf = Frame(change_pin_func.change_pin_win)
    bf.pack(side=BOTTOM)

    bf4 = Frame(change_pin_func.change_pin_win)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(change_pin_func.change_pin_win)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(change_pin_func.change_pin_win)
    bf1.pack(side=BOTTOM)

    b1 = Button(bf1, text='1', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','1'), re_entry.insert('end','1')])
    b1.pack(side=LEFT,pady=10)

    b2 = Button(bf1, text='2', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','2'), re_entry.insert('end','2')])
    b2.pack(side=LEFT, padx=10)

    b3 = Button(bf1, text='3', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','3'), re_entry.insert('end','3')])
    b3.pack(side=LEFT)

    b4 = Button(bf2, text='4', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','4'), re_entry.insert('end','4')])
    b4.pack(side=LEFT)

    b5 = Button(bf2, text='5', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','5'), re_entry.insert('end','5')])
    b5.pack(side=LEFT, padx=10)

    b6 = Button(bf2, text='6', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','6'), re_entry.insert('end','6')])
    b6.pack(side=LEFT)

    b7 = Button(bf3, text='7', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','7'), re_entry.insert('end','7')])
    b7.pack(side=LEFT,pady=10)

    b8 = Button(bf3, text='8', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','8'), re_entry.insert('end','8')])
    b8.pack(side=LEFT, padx=10)

    b9 = Button(bf3, text='9', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','9'), re_entry.insert('end','9')])
    b9.pack(side=LEFT)

    btn = Button(bf4, text='*', font=style_02,bg="black",fg="white",command=lambda: [pin_entry.insert('end','9'), re_entry.insert('end','*')])
    btn.pack(side=LEFT)

    b0 = Button(bf4, text='0', font=style_02,bg="black",fg="white", command=lambda: [pin_entry.insert('end','0'), re_entry.insert('end','0')])
    b0.pack(side=LEFT, padx=10)                         

    btn_ = Button(bf4, text='#', font=style_02,bg="black",fg="white",command=lambda: [pin_entry.insert('end','9'), re_entry.insert('end','#')])
    btn_.pack(side=LEFT)

    enter_btn = Button(bf, text='ENTER', font=style_02,bg="black", fg='green', command=message_func )
    enter_btn.pack(side=LEFT, pady=10)

    clear_btn = Button(bf, text='CLEAR', font=style_02,bg="black", fg='orange', command=lambda: [pin_entry.delete(0), re_entry.delete(0)])
    clear_btn.pack(side=LEFT, padx=10)


# options window
def option_func():
    enter_pin.new_win.withdraw()                
    option_func.option_win = Toplevel(window)
    option_func.option_win.geometry('600x500')
   # option_win.grab_set()                       

    text_title = Label(option_func.option_win, text='\nBHUVANESH ATM ☺...', font=font_01,fg="#6439FF")
    text_title.pack(pady=10)

    rig_frame = Frame(option_func.option_win)         
    rig_frame.pack(side=RIGHT)

    left_frame = Frame(option_func.option_win)          
    left_frame.pack(side=LEFT)

    withdrawal_btn = Button(rig_frame, text=' WITHDRAWAL ', font=style_02,bg="black", fg='blue', command=withdrawal_func)
    withdrawal_btn.pack(padx=20, pady=10)

    balance_btn = Button(rig_frame, text='BALANCE ENQU', font=style_02,bg="black",fg='blue', command=balance_func)
    balance_btn.pack(padx=20, pady=10)

    deposit_btn = Button(left_frame, text='DEPOSIT RS', font=style_02,bg="black",fg='blue', command=balance_func)
    deposit_btn.pack(padx=20, pady=10)

    change_pin_btn = Button(left_frame, text='CHANGE PIN', font=style_02,bg="black",fg='blue', command=change_pin_func)
    change_pin_btn.pack(padx=20, pady=10)

    btn_exit = Button(left_frame, text='   EXIT   ', font=style_02,bg="black", fg='red', command=lambda: [option_func.option_win.destroy(), enter_pin.new_win.deiconify()])
    btn_exit.pack(padx=20, pady=10)                                                                         


# enter_pin window
def enter_pin():
    window.withdraw()
    enter_pin.new_win = Toplevel(window)

    enter_pin.new_win.geometry('600x500')       

    #enter_pin.new_win.grab_set()               


    def setInputText(text):
        entry_box.insert('end',text)            

    def text_delete():
        entry_box.delete(0)                     

    lbl = Label(enter_pin.new_win,text='Enter your PIN :',font=style_01,bg="#6439FF",fg='skyblue')
    lbl.pack(pady=20)

    entry_box = Entry(enter_pin.new_win,font=style_02, show='*', justify='center')  
    entry_box.pack()

    bf = Frame(enter_pin.new_win)
    bf.pack(side=BOTTOM)

    bf0 = Frame(enter_pin.new_win)
    bf0.pack(side=BOTTOM)

    bf1 = Frame(enter_pin.new_win)
    bf1.pack(side=BOTTOM)

    bf2 = Frame(enter_pin.new_win)
    bf2.pack(side=BOTTOM)

    bf3 = Frame(enter_pin.new_win)
    bf3.pack(side=BOTTOM)

    bf4 = Frame(enter_pin.new_win)
    bf4.pack(side=BOTTOM)

    rig_frame = Frame(enter_pin.new_win)
    rig_frame.pack(side=RIGHT)

    btn1 = Button(bf4,text='1',font=style_02,bg="black",fg="white",command=lambda:setInputText('1'))
    btn1.pack(side=LEFT, pady=10)

    btn2 = Button(bf4, text='2', font=style_02,bg="black",fg="white", command=lambda:setInputText('2'))
    btn2.pack(side=LEFT,padx=10)

    btn3 = Button(bf4, text='3', font=style_02,bg="black",fg="white", command=lambda:setInputText('3'))
    btn3.pack(side=LEFT)

    btn4 = Button(bf3, text='4', font=style_02,bg="black",fg="white", command=lambda:setInputText('4'))
    btn4.pack(side=LEFT)

    btn5 = Button(bf3, text='5', font=style_02,bg="black",fg="white", command=lambda:setInputText('5'))
    btn5.pack(side=LEFT,padx=10)

    btn6 = Button(bf3, text='6', font=style_02,bg="black",fg="white", command=lambda:setInputText('6'))
    btn6.pack(side=LEFT)

    btn7 = Button(bf2, text='7', font=style_02,bg="black",fg="white", command=lambda:setInputText('7'))
    btn7.pack(side=LEFT,pady=10)

    btn8 = Button(bf2, text='8', font=style_02,bg="black",fg="white", command=lambda:setInputText('8'))
    btn8.pack(side=LEFT, padx=10)

    btn9 = Button(bf2, text='9', font=style_02,bg="black",fg="white", command=lambda:setInputText('9'))
    btn9.pack(side=LEFT)

    btn = Button(bf1, text='*', font=style_02,bg="black",fg="white",command=lambda:setInputText('*'))
    btn.pack(side=LEFT)

    btn0 = Button(bf1, text='0', font=style_02,bg="black",fg="white", command=lambda:setInputText('0'))
    btn0.pack(side=LEFT, padx=10)

    btn_ = Button(bf1, text='#', font=style_02,bg="black",fg="white",command=lambda:setInputText('#'))
    btn_.pack(side=LEFT)

    enter_btn = Button(bf0, text='ENTER', font=style_02,bg="black",fg='green', command=option_func)
    enter_btn.pack(side= LEFT, pady=10,padx=10)

    exit_btn = Button(bf0, text='EXIT', font=style_02,bg="black", fg='red', command=lambda:[enter_pin.new_win.destroy(), window.deiconify()])  
    exit_btn.pack(side=RIGHT, padx=10)

    clear_btn = Button(bf0,text='CLEAR', font=style_02,bg="black", fg='orange', command=text_delete)
    clear_btn.pack(side=LEFT)

    note = Label(bf, text='Note:Enter pin either from keyboard or keypad',font=style_02,bg="#6439FF", fg='skyblue')
    note.pack()

# main opening window
title_label = Label(window, text='BHUVANESH ATM ☺...', font=font_01,bg="#6439FF", fg='skyblue')             
title_label.pack(pady=10)                                               

#displaying some introduction
user_id = random.randrange(1000,10000)
intro = Label(window, text='\nWelcome User '+str(user_id), font=style_02,bg="#6439FF", fg='skyblue')
intro.pack(pady=20)
option_label = Label(window, text='\nSelect your account type : ', font=style_02,bg='skyblue', fg="#6439FF")
option_label.pack(pady=30)

bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)
right_frame = Frame(window)
right_frame.pack(side=RIGHT)

note = Label(bottom_frame, text='NOTE:Use only EXIT button to exit!!!', font=style_02,bg="#6439FF", fg='skyblue')
note.pack(pady=10)
saving = Button(right_frame, text='Savings', font=style_02, bg='sky blue', fg='white', command=enter_pin)
saving.pack(padx=30, pady=10)
current = Button(right_frame, text="Current", font=style_02, bg='sky blue', fg='white', command=enter_pin)
current.pack(padx=30, pady=10)

window.mainloop()
