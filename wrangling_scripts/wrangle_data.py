import pandas as pd
import plotly.graph_objs as go
import pandas as pd
from pandas_datareader import data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
     
    # create empty dataframes to store the data into
    vale_df = pd.DataFrame()
    itub_df = pd.DataFrame()
    abev_df = pd.DataFrame()
    petr_df = pd.DataFrame()
    ibov_df = pd.DataFrame()
    
    # Get data from Yahoo Finance
    vale = 'VALE3.SA'
    itub = 'ITUB4.SA'   
    abev = 'ABEV3.SA'
    petr = 'PETR4.SA'
    ibov = '^BVSP'

    vale_df = web.DataReader(vale, data_source = 'yahoo', start = '03/01/2015')
    itub_df = web.DataReader(itub, data_source = 'yahoo', start = '03/01/2015')
    abev_df = web.DataReader(abev, data_source = 'yahoo', start = '03/01/2015')
    petr_df = web.DataReader(petr, data_source = 'yahoo', start = '03/01/2015')
    ibov_df = web.DataReader(ibov, data_source = 'yahoo', start = '03/01/2015')
          
    
    # Creating the wallet ( Vale + Itub + Abev + Petr)
    wallet_df = pd.concat([vale_df['Adj Close'], itub_df['Adj Close'], abev_df['Adj Close'], petr_df['Adj Close']], axis=1)
    wallet_df.columns = [ 'VALE3','ITUB4','ABEV3','PETR4']
    # Normalizing the wallet by the first value and supposing the initial investment were R$ 12.500,00 in each active
    wallet_df = (wallet_df / wallet_df.iloc[0]*12500)
    # Create column to represent the total value of the wallet
    wallet_df['Wallet'] = wallet_df.sum(axis=1)
    # Create column to represent the equivalent value at the ^BVSP index
    wallet_df['BVSP'] = (ibov_df['Adj Close'] / ibov_df['Adj Close'].iloc[0])*50000
    
    active_list = ['Wallet', 'BVSP']
    
        
    #GRAPH One - Comparing the Wallet performance with the Ibov index    
    
    graph_one = []    
    
    for active in active_list:
        
        graph_one.append(
        go.Scatter(
        x = wallet_df.index.tolist(),
        y = wallet_df[active].tolist(),
        mode = 'lines',
        name = active   
      
         )
        )      


    layout_one = dict(title = 'Wallet x ^BVSP',
                xaxis = dict(title = 'Time'),
                yaxis = dict(title = 'Value (R$)'),
                )

    
    # GRAPH TWO - Candlesticks graph - VALE 3   
    
    trace_vale = {        
        'x': vale_df.index,
        'open': vale_df.Open,
        'close': vale_df.Close,
        'high' :vale_df.High,
        'low': vale_df.Low,
        'type': 'candlestick',
        'name' : vale,
        'showlegend': False
    }
    
    graph_two = [trace_vale]
    layout_two = go.Layout()    
    
    
    # GRAPH THREE - Candlesticks graph - ITUB4  

    trace_itub = {        
        'x': itub_df.index,
        'open': itub_df.Open,
        'close': itub_df.Close,
        'high' :itub_df.High,
        'low': itub_df.Low,
        'type': 'candlestick',
        'name' : itub,
        'showlegend': False
    }
    
    graph_three = [trace_itub]
    layout_three = go.Layout()
    
     # GRAPH FOUR - Candlesticks graph - ABEV3 

    trace_abev = {        
        'x': abev_df.index,
        'open': abev_df.Open,
        'close': abev_df.Close,
        'high' :abev_df.High,
        'low': abev_df.Low,
        'type': 'candlestick',
        'name' : abev,
        'showlegend': False
    }
    
    graph_four = [trace_abev]
    layout_four = go.Layout()
    
    # GRAPH FIVE - Candlesticks graph - PETR4 

    trace_petr = {        
        'x': petr_df.index,
        'open': petr_df.Open,
        'close': petr_df.Close,
        'high' :petr_df.High,
        'low': petr_df.Low,
        'type': 'candlestick',
        'name' : petr,
        'showlegend': False
    }
    
    graph_five = [trace_petr]
    layout_five = go.Layout()   

    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))

    return figures