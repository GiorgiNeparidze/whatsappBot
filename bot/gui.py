import threading
from tkinter import *
from ac10.account10 import account10
from ac10.account10 import sync10
from ac10.account10 import send10
from ac10.account10 import stop10
from ac9.account9 import account9
from ac9.account9 import sync9
from ac9.account9 import send9
from ac9.account9 import stop9
from ac8.account8 import account8
from ac8.account8 import sync8
from ac8.account8 import send8
from ac8.account8 import stop8
from ac7.account7 import account7
from ac7.account7 import sync7
from ac7.account7 import send7
from ac7.account7 import stop7
from ac6.account6 import account6
from ac6.account6 import sync6
from ac6.account6 import send6
from ac6.account6 import stop6
from ac5.account5 import account5
from ac5.account5 import sync5
from ac5.account5 import send5
from ac5.account5 import stop5
from ac4.account4 import account4
from ac4.account4 import sync4
from ac4.account4 import send4
from ac4.account4 import stop4
from ac3.account3 import account3
from ac3.account3 import sync3
from ac3.account3 import send3
from ac3.account3 import stop3
from ac2.account2 import account2
from ac2.account2 import sync2
from ac2.account2 import send2
from ac2.account2 import stop2
from ac1.account1 import account1
from ac1.account1 import sync1
from ac1.account1 import send1
from ac1.account1 import stop1


root = Tk()


def swap(frame):
    frame.tkraise()


# Left frame for Account sync start stop filter
control_frame = LabelFrame(root, text='ACCOUNTS CONTROLL')
control_frame.grid(row=0, column=0, sticky='nsew')
Grid.columnconfigure(root, 0, weight=1)


# Control frames For every ACCOUNT > controll_frame
# ACCOUNT 1 controls >>>
ac1_frame = LabelFrame(control_frame, text='First Account CP')
ac1_frame.grid(row=0, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 0, weight=1)
Grid.columnconfigure(control_frame, 0, weight=1)

sync1_button = Button(ac1_frame, text='Sync.', command=threading.Thread(target=sync1).start)
sync1_button.grid(row=0, column=0, padx=10, pady=10)
start1_button = Button(ac1_frame, text='START', command=threading.Thread(target=send1).start)
start1_button.grid(row=0, column=1, padx=10, pady=10)
start1_button = Button(ac1_frame, text='STOP', command=threading.Thread(target=stop1).start)
start1_button.grid(row=0, column=2, padx=10, pady=10)
costumize1_button = Button(ac1_frame, text='Costumize', command= lambda : swap(frame=account1.costumise1_frame))
costumize1_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 1 controls >>>

# ACCOUNT 2 controls >>>
ac2_frame = LabelFrame(control_frame, text='Second Account CP')
ac2_frame.grid(row=1, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 1, weight=1)

sync2_button = Button(ac2_frame, text='Sync.', command=threading.Thread(target=sync2).start)
sync2_button.grid(row=0, column=0, padx=10, pady=10)
start2_button = Button(ac2_frame, text='START', command=threading.Thread(target=send2).start)
start2_button.grid(row=0, column=1, padx=10, pady=10)
start2_button = Button(ac2_frame, text='STOP', command=threading.Thread(target=stop2).start)
start2_button.grid(row=0, column=2, padx=10, pady=10)
costumize2_button = Button(ac2_frame, text='Costumize', command= lambda : swap(frame=account2.costumise2_frame))
costumize2_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 2 controls >>>

# ACCOUNT 3 controls >>>
ac3_frame = LabelFrame(control_frame, text='Third Account CP')
ac3_frame.grid(row=2, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 2, weight=1)

sync3_button = Button(ac3_frame, text='Sync.', command=threading.Thread(target=sync3).start)
sync3_button.grid(row=0, column=0, padx=10, pady=10)
start3_button = Button(ac3_frame, text='START', command=threading.Thread(target=send3).start)
start3_button.grid(row=0, column=1, padx=10, pady=10)
start3_button = Button(ac3_frame, text='STOP', command=threading.Thread(target=stop3).start)
start3_button.grid(row=0, column=2, padx=10, pady=10)
costumize3_button = Button(ac3_frame, text='Costumize', command= lambda : swap(frame=account3.costumise3_frame))
costumize3_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 3 controls >>>

# ACCOUNT 4 controls >>>
ac4_frame = LabelFrame(control_frame, text='Fourth Account CP')
ac4_frame.grid(row=3, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 3, weight=1)

sync4_button = Button(ac4_frame, text='Sync.', command=threading.Thread(target=sync4).start)
sync4_button.grid(row=0, column=0, padx=10, pady=10)
start4_button = Button(ac4_frame, text='START', command=threading.Thread(target=send4).start)
start4_button.grid(row=0, column=1, padx=10, pady=10)
start4_button = Button(ac4_frame, text='STOP', command=threading.Thread(target=stop4).start)
start4_button.grid(row=0, column=2, padx=10, pady=10)
costumize4_button = Button(ac4_frame, text='Costumize', command= lambda : swap(frame=account4.costumise4_frame))
costumize4_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 4 controls >>>

# ACCOUNT 5 controls >>>
ac5_frame = LabelFrame(control_frame, text='Fifth Account CP')
ac5_frame.grid(row=4, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 4, weight=1)

sync5_button = Button(ac5_frame, text='Sync.', command=threading.Thread(target=sync5).start)
sync5_button.grid(row=0, column=0, padx=10, pady=10)
start5_button = Button(ac5_frame, text='START', command=threading.Thread(target=send5).start)
start5_button.grid(row=0, column=1, padx=10, pady=10)
start5_button = Button(ac5_frame, text='STOP', command=threading.Thread(target=stop5).start)
start5_button.grid(row=0, column=2, padx=10, pady=10)
costumize5_button = Button(ac5_frame, text='Costumize', command= lambda : swap(frame=account5.costumise5_frame))
costumize5_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 5 controls >>>

# ACCOUNT 6 controls >>>
ac6_frame = LabelFrame(control_frame, text='Sixth Account CP')
ac6_frame.grid(row=5, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 5, weight=1)

sync6_button = Button(ac6_frame, text='Sync.', command=threading.Thread(target=sync6).start)
sync6_button.grid(row=0, column=0, padx=10, pady=10)
start6_button = Button(ac6_frame, text='START', command=threading.Thread(target=send6).start)
start6_button.grid(row=0, column=1, padx=10, pady=10)
start6_button = Button(ac6_frame, text='STOP', command=threading.Thread(target=stop6).start)
start6_button.grid(row=0, column=2, padx=10, pady=10)
costumize6_button = Button(ac6_frame, text='Costumize', command= lambda : swap(frame=account6.costumise6_frame))
costumize6_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 6 controls >>>

# ACCOUNT 7 controls >>>
ac7_frame = LabelFrame(control_frame, text='Seventh Account CP')
ac7_frame.grid(row=6, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 6, weight=1)

sync7_button = Button(ac7_frame, text='Sync.', command=threading.Thread(target=sync7).start)
sync7_button.grid(row=0, column=0, padx=10, pady=10)
start7_button = Button(ac7_frame, text='START', command=threading.Thread(target=send7).start)
start7_button.grid(row=0, column=1, padx=10, pady=10)
start7_button = Button(ac7_frame, text='STOP', command=threading.Thread(target=stop7).start)
start7_button.grid(row=0, column=2, padx=10, pady=10)
costumize7_button = Button(ac7_frame, text='Costumize', command= lambda : swap(frame=account7.costumise7_frame))
costumize7_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 7 controls >>>

# ACCOUNT 8 controls >>>
ac8_frame = LabelFrame(control_frame, text='Eighth Account CP')
ac8_frame.grid(row=7, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 7, weight=1)

sync8_button = Button(ac8_frame, text='Sync.', command=threading.Thread(target=sync8).start)
sync8_button.grid(row=0, column=0, padx=10, pady=10)
start8_button = Button(ac8_frame, text='START', command=threading.Thread(target=send8).start)
start8_button.grid(row=0, column=1, padx=10, pady=10)
start8_button = Button(ac8_frame, text='STOP', command=threading.Thread(target=stop8).start)
start8_button.grid(row=0, column=2, padx=10, pady=10)
costumize8_button = Button(ac8_frame, text='Costumize', command= lambda : swap(frame=account8.costumise8_frame))
costumize8_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 8 controls >>>

# ACCOUNT 9 controls >>>
ac9_frame = LabelFrame(control_frame, text='Ninth Account CP')
ac9_frame.grid(row=8, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 8, weight=1)

sync9_button = Button(ac9_frame, text='Sync.', command=threading.Thread(target=sync9).start)
sync9_button.grid(row=0, column=0, padx=10, pady=10)
start9_button = Button(ac9_frame, text='START', command=threading.Thread(target=send9).start)
start9_button.grid(row=0, column=1, padx=10, pady=10)
start9_button = Button(ac9_frame, text='STOP', command=threading.Thread(target=stop9).start)
start9_button.grid(row=0, column=2, padx=10, pady=10)
costumize9_button = Button(ac9_frame, text='Costumize', command= lambda : swap(frame=account9.costumise9_frame))
costumize9_button.grid(row=0, column=3, padx=10, pady=10)
# ACCOUNT 9 controls >>>

# ACCOUNT 10 controls >>>
ac10_frame = LabelFrame(control_frame, text='Tenth Account CP')
ac10_frame.grid(row=9, column=0, sticky='nsew')
Grid.rowconfigure(control_frame, 9, weight=1)

sync10_button = Button(ac10_frame, text='Sync.', command=threading.Thread(target=sync10).start)
sync10_button.grid(row=0, column=0, padx=10, pady=10)
start10_button = Button(ac10_frame, text='START', command=threading.Thread(target=send10).start)
start10_button.grid(row=0, column=1, padx=10, pady=10)
start10_button = Button(ac10_frame, text='STOP', command=threading.Thread(target=stop10).start)
start10_button.grid(row=0, column=2, padx=10, pady=10)
costumize10_button = Button(ac10_frame, text='Costumize', command= lambda : swap(frame=account10.costumise10_frame))
costumize10_button.grid(row=0, column=3, padx=10, pady=10)


# Control frames For every ACCOUNT 10 > controll_frame
a10 = account10.Gui10(master=root)

a9 = account9.Gui9(master=root)

a8 = account8.Gui8(master=root)

a7 = account7.Gui7(master=root)

a6 = account6.Gui6(master=root)

a5 = account5.Gui5(master=root)

a4 = account4.Gui4(master=root)

a3 = account3.Gui3(master=root)

a2 = account2.Gui2(master=root)

a1 = account1.Gui1(master=root)
# Control frames For every ACCOUNT 10 > controll_frame

for fRame in (account10.costumise10_frame, account9.costumise9_frame, account8.costumise8_frame, account7.costumise7_frame,
                account6.costumise6_frame, account5.costumise5_frame, account4.costumise4_frame, account3.costumise3_frame,
                account2.costumise2_frame, account1.costumise1_frame):
    fRame.grid(row=0, column=1, sticky='nsew')


root.mainloop()