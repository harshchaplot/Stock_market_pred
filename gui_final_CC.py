import matplotlib
matplotlib.use('TkAgg')
import os
import tkinter as tk 
from tkinter import ttk 
from ML_MODEL_CC import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
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
            
            
            logo = tk.PhotoImage(file="C:/Users/Dell/Desktop/internship/summer_intern/wall2.png")
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
        
        tk.Frame.__init__(self, parent, bg='#044A80') 
        
        
        #logo = tk.PhotoImage(file="C:/Users/Dell/Desktop/INTERN/market2.png")
        #photoimage = logo.subsample(1 ,1) 

        #button_train = tk.Button(self, text ="Train Model", command = self.func) 
        #button_train.place(relx=0.36, rely= 0.1, relwidth= 0.25, relheight= 0.15)
        #button_train.config(image=photoimage)
    
        entry=tk.Entry(self,font=20, borderwidth=5)
        #entry.grid(row=0, column=0, columnspan=3, sticky="we")
        entry.place(x=80, y= 40, width=850, height=45)
        
        button_tick = ttk.Button(self, text= "Go", command= lambda: self.tickval(entry.get()))
        #button_tick.grid(row=0, column=3, padx=30, pady=30)
        button_tick.place(relx=0.78, y= 40,relwidth=0.16, height=45)
        
        button_hist = ttk.Button(self, text ="Historical data of the Company", command = self.showHistory)
        #button_hist.grid(row=1, column=0, padx=30, pady=30)
        button_hist.place(x=80, y= 125, relwidth=0.16, height=45)
        
        button_pred = ttk.Button(self, text= "Display the predictions graph", command = self.preds)
        #button_pred.grid(row=1, column=1, padx=30, pady=30)
        button_pred.place(x=395, y= 125, width= 220, height=45)
      
        button_def = ttk.Button(self, text= "Ticker Values Information", command = self.show_ticker)
        #button_def.grid(row=1, column=2, padx=30, pady=30)
        button_def.place(x=710, y= 125, width=220 , height= 45)
      
        button_exit = ttk.Button(self, text ="Exit", command = close_window) 
        #button_exit.grid(row=1, column=3, padx=30, pady=30)
        button_exit.place(relx=0.78, y=125,relwidth=0.16, height=45)
        
        #label = ttk.Label(self, text="After pressing Train Model, wait for a minute for the model to train", font = LARGEFONT) 
        #label.place(relx=0.24, rely=0.8)
        
        lower_frame=tk.Frame(self, bg='#A8D7FB', bd=50)
        lower_frame.place(x=80, y=207, relwidth=0.884, relheight=0.67)
       
       
        
        
        # print(self.tickval(entry.get()))
        
        
        #
    
#        label['text']= str(pred_price.ML_MODEL_CC)
    
    
    def tickval(self, entry):
        #df = web.DataReader(ticker,'yahoo',start='2019-11-01',end='2019-12-17')
        name=entry
        print('Printing name')
        print(name)
        string,myDict = mycompany(name)
        
        global global_df
        global validData
        global trainData
        validData = myDict["valid_data"]
        trainData = myDict["train_data"]
        global_df = myDict["df"]
        pred_price = myDict["pred_price"]
        
        if(string=='no'):
            myString = str((myDict["pred_price"]))
            label = tk.Label(self, text="The predicted price for " + str(name) + " is: ",bg='#A8D7FB', font = LARGEFONT) 
            label.place(relx=0.3, rely=0.9)
            label = tk.Label(self, text=myString, font = LARGEFONT, bg='#A8D7FB') 
            label.place(relx=0.6, rely=0.9)
        else:
            label = tk.Label(self, text="Please enter the name of the company ticker", bg='#A8D7FB',font = LARGEFONT) 
            label.place(relx=0.3, rely=0.9)
        
        
    def show_ticker(self):
                  
        label = tk.Label(self, text="Ticker values of some companies for reference are: \n\nHero MotoCorp Limited:         HEROMOTOCO.NS\nTata Motors Limited:          TATAMOTORS.NS\nReliance Power Limited:          RPOWER.NS\nMahindra & Mahindra Limited:      M&M.NS\nInfosys Limited:          INFY.NS\nIndian Oil Corporation Limited:  IOC.NS\nNestle India Limited:          NESTLEIND.NS\nBosch Limited:             BOSCHLTD.NS\nGillette India Limited:          GILLETTE.BO\nBritannia Industries Limited:    BRITANNIA.BO\n"
                         
                         , bg='#A8D7FB',font = LARGEFONT, justify="left") 
        label.place(x=85, y=210)
        
            

        
    def func(self):
        print('Training model')                
        
        myDict = myfunc()
        global global_df
        global validData
        global trainData
        validData = myDict["valid_data"]
        trainData = myDict["train_data"]
        global_df = myDict["df"]
        pred_price = myDict["pred_price"]
        print(pred_price)
        
        
        
        
    def showHistory(self):
        print('Showing historical data')

        fig = Figure(figsize=(5,5))
        a = fig.add_subplot(111)
        a.plot(global_df.Close)
        
        canvas1 = FigureCanvasTkAgg(fig, master=self)
        canvas1.get_tk_widget().pack_forget()

        canvas1.get_tk_widget().place(x=80, y=207, relwidth=0.884, relheight=0.64)
        
        canvas1.draw()
        
        toolbar = NavigationToolbar2Tk(canvas1, self)
        toolbar.update()
        canvas1._tkcanvas.place(x=80, y=207, relwidth=0.884, relheight=0.6)


    def preds(self):
        
        print('Showing predictions')
        fig = Figure(figsize=(5,5))
        a = fig.add_subplot(111)
        a.plot(trainData['Close'])
        
        b = fig.add_subplot(111)
        b.plot(validData[['Close', 'Predictions']])
        
        
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack_forget()

        canvas.get_tk_widget().place(x=80, y=207, relwidth=0.884, relheight=0.64)
        canvas.draw()
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(x=80, y=207, relwidth=0.884, relheight=0.6)

        #trainData['Close']
        #validData[['Close', 'Predictions']]
        #vis(trainData, validData)




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
