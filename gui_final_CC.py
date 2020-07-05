import matplotlib
matplotlib.use('TkAgg')
import os
import tkinter as tk 
from tkinter import ttk 
from ML_MODEL_CC import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


LARGEFONT =("Verdana", 15)


def close_window():
    app.destroy()
    

class tkinterApp(tk.Tk): 
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
        
        # creating a container 
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 

        # initializing frames to an empty array 
        self.frames = {} 

        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (StartPage, Page1, Page2): 

            frame = F(container, self) 

            # initializing frame of that object from 
            # startpage, page1, page2 respectively with 
            # for loop 
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew") 

        self.show_frame(StartPage) 

    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 

# first window frame startpage 

class StartPage(tk.Frame): 
    def __init__(self, parent, controller): 
            tk.Frame.__init__(self, parent) 
            
            
            logo = tk.PhotoImage(file="C:/Users/Dell/Desktop/INTERN/wall2.png")
            BGlabel = tk.Label(self,image=logo)
            BGlabel.image = logo
            BGlabel.place(relwidth=1,relheight=1)
            
            '''  
            mycanvas = tk.Canvas(self, width = 200, height = 25)
            mycanvas.create_rectangle(0, 0, 100, 40)
            mycanvas.pack(side = "top", fill = "both", expand = True)
              
            text_canvas = mycanvas.create_text(10, 10, anchor = "nw")
            mycanvas.itemconfig(text_canvas, text="Look no background! Thats new!")
            '''
            
            # label of frame Layout 2 
            label = tk.Label(self, text ="Welcome", font = LARGEFONT) 
            
            # putting the grid in its place by using 
            label.place(relx=0.43, rely=0.1) 
            
            button_start = tk.Button(self, text= "Start",relief='flat',command= lambda: controller.show_frame(Page1), bg='#2A942A')
            button_start.place(relx=0.1, rely= 0.4, relwidth= 0.3, relheight= 0.15 )
    

            button_close = tk.Button(self, text = "Exit", command = close_window, bg='#CC0000')
            button_close.place(relx=0.6, rely= 0.4, relwidth= 0.3, relheight= 0.15 )
            
            
                ## button to show frame 2 with text layout2 
                #         button2 = ttk.Button(self, text ="Page 2", 
                #         command = lambda : controller.show_frame(Page2)) 
        
                # putting the button in its place by 
                # using grid 
    #         button2.grid(row = 2, column = 1, padx = 10, pady = 10) 


# second window frame page1 
class Page1(tk.Frame): 
    
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent, bg='black') 
        
        
        #logo = tk.PhotoImage(file="C:/Users/Dell/Desktop/INTERN/market2.png")
        #photoimage = logo.subsample(1 ,1) 

        button_train = tk.Button(self, text ="Train Model", command = self.func) 
        button_train.place(relx=0.36, rely= 0.1, relwidth= 0.25, relheight= 0.15)
        #button_train.config(image=photoimage)
    
        
        button_back = ttk.Button(self, text ="Exit", command = close_window) 
        button_back.place(relx=0.7, rely= 0.5, relwidth= 0.2, relheight= 0.15)
        
        #label = ttk.Label(self, text="After pressing Train Model, wait for a minute for the model to train", font = LARGEFONT) 
        #label.place(relx=0.24, rely=0.8)
        
        #button3 = ttk.Button(self, text ="Load historical data of the stock", command = self.showHistory)
        #button3.place(relx=0.1, rely= 0.5, relwidth= 0.2, relheight= 0.15)

        #button4 = ttk.Button(self, text= "Display the predictions graph", command = self.preds)
        #button4.place(relx=0.39, rely= 0.5, relwidth= 0.2, relheight= 0.15)
        
        entry=tk.Entry(self,font=20)
        entry.place(relx=0.3, rely= 0.6,relwidth=0.65, relheight=0.3)
    
        button5 = ttk.Button(self, text= "Display", command= lambda: self.tickval(entry.get()))
        button5.place(relx=0.1, rely= 0.6, relwidth= 0.15, relheight= 0.1)
        
        print(self.tickval(entry.get()))
        
        
        #
    
#        label['text']= str(pred_price.ML_MODEL_CC)
    
    
    def tickval(self, entry):
        #df = web.DataReader(ticker,'yahoo',start='2019-11-01',end='2019-12-17')
        name=entry
        mycompany(name)
        
        
        

        
    def func(self):
        print('Training model')                
        
        pred_price,rel_quote2_close,valid_data,train_data,df = myfunc()
        global global_df
        global validData
        global trainData
        validData = valid_data
        trainData = train_data
        global_df = df
        print(pred_price)
        
        
        
        
    def showHistory(self):
        print('Showing historical data')
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.history(global_df)
        
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()


    def preds(self):
        print('Showing predictions')
        vis(trainData, validData)




    # third window frame page2 
class Page2(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="Page 1", 
                            command = lambda : controller.show_frame(Page1)) 
    
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

        # button to show frame 3 with text 
        # layout3 
        button2 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
    
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
        ''' 
        
        '''


# Driver Code 
app = tkinterApp() 
app.mainloop() 
