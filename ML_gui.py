import tkinter as tk
import pandas_datareader.data as web
#import requests
import ML_MODEL


import pandas_datareader.data as web



#def tickval(ticker):
 #   df = web.DataReader(ticker,'yahoo',start='2019-11-01',end='2019-12-17')

  
        
root = tk.Tk()

canvas= tk.Canvas(root, height=500, width=600)
canvas.pack()

frame=tk.Frame(root, bg='gray')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

'''
entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)
, command= lambda: tickval(entry.get())
'''

button_cp=tk.Button(frame, text="Close price")
button_cp.place(relx=0, relheight=1, relwidth=0.3)


button_graph=tk.Button(frame, text="Prediction graph", command=ML_MODEL.vis)
button_graph.place(relx=0.6, relheight=1, relwidth=0.3)



#print(tickval(entry.get()))

lower_frame=tk.Frame(root, bg='gray', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(lower_frame)
label.place(relheight=1, relwidth=1)

root.mainloop()

