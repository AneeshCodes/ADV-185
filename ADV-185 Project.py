from tkinter import *
import requests
import json

root = Tk()
root.geometry("675x550")

root.overrideredirect(True)

heading = Label(root,text="News")
heading.place(relx=0.5,rely=0.1,anchor=CENTER)

news1_title = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news1_title.place(relx=0.2,rely=0.17,anchor=W)

news1_description = Label(root,font=("arial", 12,'bold'), fg="black",wraplength=500,justify=LEFT)
news1_description.place(relx=0.2,rely=0.24,anchor=W)

news2_title = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news2_title.place(relx=0.2,rely=0.32,anchor=W)

news2_description = Label(root,font=("arial", 12,'bold'), fg="black",wraplength=500,justify=LEFT)
news2_description.place(relx=0.2,rely=0.41,anchor=W)

news3_title = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news3_title.place(relx=0.2,rely=0.5,anchor=W)

news3_description = Label(root,font=("arial", 12,'bold'), fg="black",wraplength=500,justify=LEFT)
news3_description.place(relx=0.2,rely=0.59,anchor=W)

api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d19e527b11df48c0bcc07c26dfe0a65e")

open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page["articles"][0]["title"]
print(title1)
description1 = open_bbc_page["articles"][0]["description"]
print(description1)

title2 = open_bbc_page["articles"][1]["title"]
print(title2)
description2 = open_bbc_page["articles"][1]["description"]
print(description2)

title3 = open_bbc_page["articles"][2]["title"]
print(title3)
description3 = open_bbc_page["articles"][2]["description"]
print(description3)

news1_title["text"] = "Title 1:" + title1
news2_title["text"] = "Title 2:" + title2
news3_title["text"] = "Title 3:" + title3

news1_description["text"] = "Title 1:" + description1
news2_description["text"] = "Title 2:" + description2
news3_description["text"] = "Title 3:" + description3

root.mainloop()