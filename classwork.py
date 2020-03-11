# from tkinter import *
#
# app = Tk()
# app.title('Decision System')
# app.geometry('300x200')
#
# data_req1 = Label(app, text='What is your name?')
# data_req1.grid(row=0, column=0)
# data_entry = Entry(app)
# data_entry.grid(row=1, column=0)
#
# but_send = Button(app)
# but_send.grid(row=2, column=0)
#
#
# app.mainloop()


def greet_me():
    print('What is your name?')
    name = input()
    print('Where do you come from?')
    village = input()
    print('Hello',name,'from',village)

greet_me()