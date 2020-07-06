import math
import pandas as pd
import numpy as np
import pandas_datareader.data as web


#to plot within notebook
import matplotlib.pyplot as plt
#%matplotlib inline

#setting figure size
from matplotlib.pylab import rcParams


#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))


#Importing required libraries from sklearn
from sklearn.metrics import mean_squared_error


from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.metrics import r2_score



def history(df):
    #Plotting Closing Price wrt date
    plt.figure(figsize=(16,8))
    plt.title('Close price history')
    plt.plot(df.Close)
    plt.xlabel('Date',fontsize=18)
    plt.ylabel('Closing price ($)',fontsize=18)
    plt.show()


def vis(train_data,valid_data):
    rcParams['figure.figsize'] = 16, 8

    plt.plot(train_data['Close'])
    plt.plot(valid_data[['Close', 'Predictions']])
    plt.legend(['train', 'val', 'predictions'])
    plt.xlabel("Date")
    plt.ylabel("Closing Price in USD")
    plt.show()

def mycompany(company):
    #read the file
    global company_df
    print('Training model for ',end=' ')
    global company1
    company1= company
    print(company)
    try:
        company_df = web.DataReader(company,'yahoo',start='2012-01-01',end='2019-12-17')
    except:
        return 'error',{}
    myDict = myfunc()
    return 'no',myDict
    
def myfunc():
    #print the dataframe
    
    df= company_df
    
    #To get index value 'Date' into a column value
    #df.reset_index(inplace=True,drop=False)
    
    df.count()
    
    #Getting only the closing price 
    data=df.filter(['Close'])
    dataset = data.values
    
    # Defining sizes of each set
    test_size = 0.2                 # proportion of dataset to be used as test set
    train_size = 0.8                # proportion of dataset to be used as training set
    
    #Splitting into train and test
    
    # Getting sizes of each of the datasets
    num_test = math.ceil(test_size*len(dataset))
    num_train = math.ceil(len(dataset)*train_size)
    
    #showing the sizes
    print("num_test = " + str(num_test))
    print("num_train = " + str(num_train))
    
    #Scaling the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    
    # scaled_data
    
    # Create training data set
    
    #Create scaled training dataset
    train = scaled_data[0:num_train, :]
    
    #Splitting the data into x_train and y_train
    x_train=[]
    y_train=[]
    
    for i in range(60, len(train)):
      x_train.append(train[i-60:i, 0])
      y_train.append(train[i, 0])
      
    
    #Convert x_train and y_train to numpy arrays
    x_train, y_train= np.array(x_train), np.array(y_train)
    
    #Reshape the datastate (LSTM need 3 dimensional data)
    x_train= np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    # x_train.shape
    
    #Building the LSTM model 
    model= Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape= (x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    
    # serialize model to JSON
    '''model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")'''
    
    #Compiling the model
    model.compile(optimizer= 'adam', loss='mean_squared_error' )
    
    #Train the model
    model.fit(x_train, y_train, batch_size=128, epochs=2)
    
    #Create the tesing data set
    test= scaled_data[num_train-60: , :]
    #Creating testing datasets x_test and y_test
    x_test=[]
    y_test=dataset[num_train: , :]
    for i in range(60, len(test)):
      x_test.append(test[i-60:i, 0])
    
    
    #Convert the data to numpy array
    x_test=np.array(x_test)
    
    #Reshape the data
    x_test=np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    # x_test
    
    #Get the models predicted price value
    predictions= model.predict(x_test)
    predictions= scaler.inverse_transform(predictions)
    
    #Calculating RMSE
    rmse= np.sqrt(np.mean(predictions- y_test)**2)
    print("RMSE is = " + str(rmse))
    
    accuracy = r2_score(y_test, predictions)
    print("Accuracy is = " + str(accuracy))
    
    
    
    # Plot the data
    train_data= data[:num_train]
    valid_data= data[num_train:]
    valid_data['Predictions'] = predictions
    
    #Visualize
    # vis(train_data,valid_data)
    
    
    #Show the valid and predicted prices
    # valid_data
    
    '''
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    
    # evaluate loaded model on test data
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    score = loaded_model.evaluate(train_data, valid_data, verbose=0)
    print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
    
    '''
    #Predicting the closing price using the closing price from 60 days
    
    #Get the quote
    rel_quote=web.DataReader(company1,'yahoo',start='2012-01-01',end='2019-12-17')
    new_df= rel_quote.filter(['Close'])
    last_60_days = new_df[-60:].values
    
    #Scale the data
    last_60_days_scaled=scaler.transform(last_60_days)
    
    X_test=[]
    
    #Append past 60 days
    X_test.append(last_60_days_scaled)
    #Convert the X_test to np array
    X_test=np.array(X_test)
    #Reshape the data
    X_test=np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    #Get the models predicted price value
    pred_price= model.predict(X_test)
    pred_price= scaler.inverse_transform(pred_price)
    print(pred_price)
    
    #Get the orignal closing price for comparison with predicted value
    rel_quote2=web.DataReader(company1,'yahoo',start='2019-12-18',end='2019-12-18')
    print(rel_quote2['Close'])

    pred_dict = {"pred_price":pred_price, "rel_quote2": rel_quote2['Close'], "train_data":train_data, "valid_data":valid_data, "df":df}
    
    #Returning the value to GUI scrpit
    return pred_dict