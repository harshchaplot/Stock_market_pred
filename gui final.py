import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import figure


import tkinter as tk
from PIL import Image, ImageTk
import ML_MODEL


LARGE_FONT= ("Verdana", 12)

class collection(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        container = tk.Frame(self)
        container.place(relx=0, rely=0, relwidth=1, relheight=1)


        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        

   
def close_window():
    app.destroy()
    
    


    
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Canvas.__init__(self,parent, bg='#1C0D84')
        
    
        
  
        #label = tk.Label(self, text="Start Page", font=LARGE_FONT)
       # label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Start", command=lambda: controller.show_frame(PageOne), bg='#2A942A')
        button.place(relx=0.1, rely= 0.4, relwidth= 0.3, relheight= 0.15 )

       
        
        button_close = tk.Button(self, text = "Exit", command = close_window, bg='#CC0000')
        button_close.place(relx=0.6, rely= 0.4, relwidth= 0.3, relheight= 0.15 )


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg='white')
      
        
        
        label = tk.Label(self, text="Start Predicting", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        button_cp = tk.Button(self, text="Closing Price",command=lambda: controller.show_frame(StartPage) , bg='#2A942A')
        button_cp.place(relx=0.3, rely= 0.1, relwidth= 0.15, relheight= 0.10 )

       
        
        button_graph = tk.Button(self, text = "Prediction Graph", command=lambda: controller.show_frame(PageTwo), bg='#CC0000')
        button_graph.place(relx=0.5, rely= 0.1, relwidth= 0.15, relheight= 0.10 )
        
       

        
        lower_frame=tk.Frame(self, bg='yellow', bd=10)
        lower_frame.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.6, anchor='n')
        
        
        label=tk.Label(lower_frame)
        label.place(relheight=1, relwidth=1)
            
        label['text'] = ML_MODEL.pred_price
        
        
        




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



        
        button_close = tk.Button(self, text = "Good-bye.", command = close_window)
        button_close.pack()

        
        f= figure(figsize=(5,5), dpi=100)
        
        a=f.add_subplot(111)
        
        a=ML_MODEL.vis()
        
        canvas= FigureCanvasTkAgg(f, self)
        canvas.show()
        
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
        
        

app = collection()
app.mainloop()