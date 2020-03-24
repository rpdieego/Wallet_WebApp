# Wallet_WebApp
Web app which compares a investment wallet with the BVSP index

Udacity - Data Scientist Nanodegree [Portifolio Exercise 02 - Deploy a Data Dashboard]

Link to the Dashboard [here](https://rpdieego-wallet-webapp.herokuapp.com/)

In this dashboard, it's assumed that one have invested R$ 50.000,00 on the brazilian stocks market, at 03/01/2015.
The investment was split equally betwen the following actives:

*   **VALE3** - Initial investment: R$ 12.500,00
*   **ITUB4** - Initial investment: R$ 12.500,00
*   **ABEV3** - Initial investment: R$ 12.500,00
*   **PETR4** - Initial investment: R$ 12.500,00

The dashboard gather live data from Yahoo finance, and displays 5 charts:

*   Chart one compares the performance of the wallet to the ^BVSP index;
*   Chart two to five are candlesticks charts of each active in the wallet;

## General Information

*   **Front end**: developed using Bootstrap;
*   **Back end**: develop using Python (Flask and Plotly);
*   **Deploy**: the deploy have been made at Heroku;

## Instalation

No installation needed to check the Data Dashboard (link at the top of this file)

## Libraries

*   PanDas;
*   PanDas_Datareader;
*   Plotly.graph_objects;
*   Numpy;
*   matplotlib.pyplot;
*   Seaborn;
*   Flask;
*   Gunicorn;

## Files in the repository


*   **Wallet\ __ init __.py** - File that imports the Flask library and routes;
  
*   **Wallet\ routes.py** - Renders the template at the proper web address;

*   **static\ img\ githublogo.png** - Github logo;
      
*   **static \img\ linkedinlogo.png** - LinkedIn logo;
      
*   **templates\ index.html** - File which holds the design of the web app (Boostrap used);

*   **Wrangling_scripts\ wrangle_data.py** - File which holds the Python code used to gather and prepared the data and charts;
  
*   **Procfile** - File that tells Heroku what to do when starting the web app;

*   **requirements.txt** - Python libraries which were installed in the virtual environment used;

*   **wallet.py** - File that starts the web app;

## Acknowledgments

*   [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)
*   [Rico por acaso](https://www.youtube.com/results?search_query=rico+por+acaso&page=&utm_source=opensearch)




