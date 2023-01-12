# ETF Forecasts
<hr>
In this project we are using historic ETF data from Yahoo Finance to predict/forecast historic ETF prices. The ETF's we are using are the ARK Innovation Fund (Ticker: ARKK), the SPDR S&P 500 ETF Trust (Ticker: SPY) and the Bank of Montreal MicroSectors FANG Index (Ticker: FNGU). We are using two machine learning models, the Facebook/Meta Prophet model as well as a Google Tensorflow LSTM Recurrent Neural Network models to predict/forecast these ETF prices. And we compare and contrast these different models and their performance against the real historic prices.

## [Video Presentation - Coming Soon]()

## Notebooks
- [Data Exploration](./Data_Exploration.ipynb)
- [Prophet Model Forecasting](./Prophet.ipynb)
- [LSTM RNN Model Forecasting](./LSTM_RNN.ipynb)

## Results
### Data
The data used was pulled from Yahoo Finance. The focus of the data was on three ETFs: ARKK, SPY, and FNGU. The timeframe of the data is from January of 2018 to March of 2022. To get a clear review and analysis of the data we used the Adjusted Close Price.

The Data is stored in a CSV and can be found here: [ETF Data CSV](./Resources/Data/etf_data.csv)

![All ETFS](./Resources/images/markdown/Analysis__etf_adjusted_closing_prices.png)
![ARKK](./Resources/images/markdown/Analysis_arkk_etf_adjusted_closing_prices.png)
![SPY](./Resources/images/markdown/Analysis_spy_etf_adjusted_closing_prices.png)
![FNGU](./Resources/images/markdown/Analysis_fngu_etf_adjusted_closing_prices.png)

### Metrics Results
Facebook/Meta Prophet Models | Google Tensorflow LSTM RNN Models
:-------------------------:|:-------------------------:
**ARKK** - *Mean Absolute Error:* 9.43 | **ARKK** - *Mean Absolute Error:* 69.88
**SPY** - *Mean Absolute Error:* 34.92 | **SPY** - *Mean Absolute Error:* 436.76
**FNGU** - *Mean Absolute Error:* 49.36 | **FNGU** - *Mean Absolute Error:* 246.19
![Prophet - Mean Absolute Error](./Resources/images/markdown/Prophet/metrics/Prophet_mean_absolute_error.png)  |  ![LSTM - Mean Absolute Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_mean_absolute_error.png)
**ARKK** - *Mean Squared Error:* 192.27 | **ARKK** - *Mean Squared Error:* 4954.66
**SPY** - *Mean Squared Error:* 1522.05 | **SPY** - *Mean Squared Error:* 190968.11
**FNGU** - *Mean Squared Error:* 3147.08 | **FNGU** - *Mean Squared Error:* 64041.90
![Prophet - Mean Squared Error](./Resources/images/markdown/Prophet/metrics/Prophet_mean_squared_error.png)  |  ![LSTM - Mean Squared Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_mean_squared_error.png)
**ARKK** - *Root Mean Squared Error:* 13.87 | **ARKK** - *Root Mean Squared Error:* 70.39
**SPY** - *Root Mean Squared Error:* 39.01 | **SPY** - *Root Mean Squared Error:* 437.00
**FNGU** - *Root Mean Squared Error:* 56.10 | **FNGU** - *Root Mean Squared Error:* 253.07
![Prophet - Root Mean Squared Error](./Resources/images/markdown/Prophet/metrics/Prophet_root_mean_squared_error.png)  |  ![LSTM - Root Mean Squared Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_root_mean_squared_error.png)
### Forecasting Results
Facebook/Meta Prophet Models | Google Tensorflow LSTM RNN Models
:-------------------------:|:-------------------------:
**All 3 ETFs** - *Tickers*: **ARKK**, **SPY**, **FNGU** - *Training Data vs Actual vs Forecasted Adjusted Closing Price* | **All 3 ETFs** - *Tickers*: **ARKK**, **SPY**, **FNGU** - *Training Data vs Actual vs Forecasted Adjusted Closing Price*
![Prophet - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**All 3 ETFs** - *Tickers*: **ARKK**, **SPY**, **FNGU** - Actual vs Forecasted Adjusted Closing Price | **All 3 ETFs** - *Tickers*: **ARKK**, **SPY**, **FNGU** - *Actual vs Forecasted Adjusted Closing Price*
![Prophet - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**ARK Innovation ETF** - *Ticker:* **ARKK** - *Training Data vs Actual vs Forecasted Adjusted Closing Price* | **ARK Innovation ETF** - *Ticker:* **ARKK** - *Training Data vs Actual vs Forecasted Adjusted Closing Price*
![Prophet - ARKK - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_arkk_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - ARKK - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_arkk_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**ARK Innovation ETF** - *Ticker:* **ARKK** - Actual vs Forecasted Adjusted Closing Price | **ARK Innovation ETF** - *Ticker:* **ARKK** - *Actual vs Forecasted Adjusted Closing Price*
![Prophet - ARKK - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_arkk_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - ARKK - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_arkk_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**SPDR S&P 500 ETF Trust** - *Ticker:* **SPY** - *Training Data vs Actual vs Forecasted Adjusted Closing Price* | **SPDR S&P 500 ETF Trust** - *Ticker:* **SPY** - *Training Data vs Actual vs Forecasted Adjusted Closing Price*
![Prophet - SPY - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - SPY - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_spy_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**SPDR S&P 500 ETF Trust** - *Ticker:* **SPY** - Actual vs Forecasted Adjusted Closing Price | **SPDR S&P 500 ETF Trust** - *Ticker:* **SPY** - *Actual vs Forecasted Adjusted Closing Price*
![Prophet -  SPY - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_spy_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - SPY - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_spy_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**Bank of Montreal MicroSectors FANG Index** - *Ticker:* **FNGU** - *Training Data vs Actual vs Forecasted Adjusted Closing Price* | **Bank of Montreal MicroSectors FANG Index** - *Ticker:* **FNGU** - *Training Data vs Actual vs Forecasted Adjusted Closing Price*
![Prophet - FNGU - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_fngu_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - FNGU - Training Data vs Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_fngu_training_data_vs_actual_vs_forecasted_etf_adjusted_closing_prices.png)
**Bank of Montreal MicroSectors FANG Index** - *Ticker:* **FNGU** - Actual vs Forecasted Adjusted Closing Price | **Bank of Montreal MicroSectors FANG Index** - *Ticker:* **FNGU** - *Actual vs Forecasted Adjusted Closing Price*
![Prophet - FNGU - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/Prophet/plots/Prophet_fngu_actual_vs_forecasted_etf_adjusted_closing_prices.png)  |  ![LSTM - FNGU - Actual vs Forecasted Adjusted Closing Price](./Resources/images/markdown/LSTM_RNN/plots/LSTM_RNN_fngu_actual_vs_forecasted_etf_adjusted_closing_prices.png)

### Facebook/Meta Prophet Model vs Tensorflow LSTM RNN Model Findings
@TODO

## Conclusion/Summary
@TODO

## Getting Started
### Prerequisites

You must have Python 3, Anaconda, Conda and Pip installed

```
$ python3 --version
Output: Python 3.10.8
$ anaconda --version
Output: anaconda Command line client (version 1.11.0)
$ conda --verison
Output: conda 22.9.0
$ pip --verison
Ouput: pip 22.2.2 from /Users/{#Username}/opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)
```

### Cloning Repo, Installing Dependencies & Running Jupyter
```
$ git clone git@github.com:SZun/ETF-Forecasts.git
$ cd ETF-Forecasts
$ sh install.sh
$ jupyter lab
```

## Built With
- [![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/) - Deep Learning Framework
- [![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/) - Machine Learning library
- [![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/#) - Data analysis library
- [![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/) - Multi-dimensional array library
- [![Python 3.7.13](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]([https://www.python.org/downloads/release/python-3713/)
[![Python](https://img.shields.io/badge/Python-3.7.13-blue)](https://www.python.org/downloads/release/python-3713/) - Programming Language
- [![Conda](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/en/latest/) - Package manager
- [Prophet](https://facebook.github.io/prophet/) - Machine learnig library for forecasting
- [Yahoo Finance](https://matplotlib.org/) - Financial data API
- [Matplotlib](https://hvplot.holoviz.org/) - Visualization library 
- [Hvplot](https://hvplot.holoviz.org/) - Visualization library for Pandas-based plots
- [Seaborn](https://seaborn.pydata.org/)  - Visualization library
- [Pathlib](https://plotly.com/python/) - Python module for paths

## Contributors
- **Gabriel Millan** - [LinkedIn](https://www.linkedin.com/in/millangabriel/) | [Github](https://github.com/gjmillan)
- **Max Heatter** - [LinkedIn](https://www.linkedin.com/in/maxwell-heatter-ba4b03194/) | [Github](https://github.com/MaxHeatter)
- **Sam G. Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [Github](https://github.com/SZun)
- **Tim Clemens** - [Github](https://github.com/AmericanHacker)

