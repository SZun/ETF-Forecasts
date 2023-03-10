# ETF Forecasts
<hr>
In this project we are using historic ETF data from Yahoo Finance to predict/forecast historic ETF prices. The ETF's we are using are the ARK Innovation Fund (Ticker: ARKK), the SPDR S&P 500 ETF Trust (Ticker: SPY) and the Bank of Montreal MicroSectors FANG Index (Ticker: FNGU). We are using two machine learning models, the Facebook/Meta Prophet model as well as a Google Tensorflow LSTM Recurrent Neural Network models to predict/forecast these ETF prices. And we compare and contrast these different models and their performance against the real historic prices.

## [Presentation Video](https://youtu.be/YlUh1zznbOA)

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

### Metrics
Facebook/Meta Prophet Models | Google Tensorflow LSTM RNN Models
:-------------------------:|:-------------------------:
**ARKK** - *Mean Absolute Error:* 9.43 | **ARKK** - *Mean Absolute Error:* 69.90
**SPY** - *Mean Absolute Error:* 34.92 | **SPY** - *Mean Absolute Error:* 436.71
**FNGU** - *Mean Absolute Error:* 49.36 | **FNGU** - *Mean Absolute Error:* 246.19
![Prophet - Mean Absolute Error](./Resources/images/markdown/Prophet/metrics/Prophet_mean_absolute_error.png)  |  ![LSTM - Mean Absolute Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_mean_absolute_error.png)
**ARKK** - *Mean Squared Error:* 192.27 | **ARKK** - *Mean Squared Error:* 4956.81
**SPY** - *Mean Squared Error:* 1522.05 | **SPY** - *Mean Squared Error:* 190925.27
**FNGU** - *Mean Squared Error:* 3147.08 | **FNGU** - *Mean Squared Error:* 64040.12
![Prophet - Mean Squared Error](./Resources/images/markdown/Prophet/metrics/Prophet_mean_squared_error.png)  |  ![LSTM - Mean Squared Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_mean_squared_error.png)
**ARKK** - *Root Mean Squared Error:* 13.87 | **ARKK** - *Root Mean Squared Error:* 70.40
**SPY** - *Root Mean Squared Error:* 39.01 | **SPY** - *Root Mean Squared Error:* 436.95
**FNGU** - *Root Mean Squared Error:* 56.10 | **FNGU** - *Root Mean Squared Error:* 253.067
![Prophet - Root Mean Squared Error](./Resources/images/markdown/Prophet/metrics/Prophet_root_mean_squared_error.png)  |  ![LSTM - Root Mean Squared Error](./Resources/images/markdown/LSTM_RNN/metrics/LSTM_RNN_root_mean_squared_error.png)
### Forecasting Results

### Facebook/Meta Prophet Model vs Tensorflow LSTM RNN Model Findings
Both models were train on the same data, as well as used the same data for forecasting.

The data used for LSTM RNN had to be scaled using the MinMaxScaler from sklearn. But the data for Prophet simply had to have the names of the columns changed to 'ds' and 'y'.

Both of the models had a train-test-split. The Prophet model simply split the DataFrame into train and test data, not features and targets. The LSTM train-test-split was much more involved. Not only was the data split into training and testing features and targets, but had to be reshaped using numpy.

Creating the Prophet model was simpler and less time consuming than that of the LSTM RNN. The Prophet model class was already built and just needed to have certain parameters filled in and tuned. Whereas the LSTM RNN model was built from scratch using a Sequential model, two LSTM layers, a third Dense layer, and a final Dense outplut layer. We also used the adam optimizer, and calculated the mean absolute error and mean squared error for our loss function and metrics.  

Though when tuning the models, the LSTM RNN took much less hyperperamater tuning and resulted in much better forecasting. For the LSTM RNN we increased the amount of training data, as well as upped the epochs to 35 (where we saw the beginning of dimished returns). Though for the Prophet model, we used a technique of automatic hyperparameter tuning. To do this we fed in a dictionary with the names of the parameters as keys and an array of possible values. We then ran the Prophet model with every combination of the values to assertain the best fitting parameters.

Forecasting was simple for both models. Both models supplied a predict method that took the training data.

The evaluation and results for the two models was stark and quite interesting. The Prophet models had much better results for Mean Absolute Error, Mean Squared Error and Root Mean Squared Error for their forecasts. But when looking at the results as visualizations, we can clearly see that the LSTM RNN models performed much better, and had much better predictive power when it came to forecasting these ETF prices. The disparity in metrics results is likely due to the learning rate causing spikes in the metrics.

## Conclusion/Summary
In conclusion, we saw that the Prophet model was easier to develop when it came to processing the data, doing the train-test-split, creating and training the model, as well as scoring high well in terms of the metrics. Though we know that for tuning as well as the final visualized results, we can see that the Prophet model fell very short compared to the LSTM RNN. The LSTM RNN was much more involved and harder to develop. Everything from scaling the data, the tran-test-split and reshaping of the data, to creating and training the models, as well as scoring poorly on the metrics. But when it came to tuning as well as the predictive power of the model, we can see that investing the time was well worth it. All in all, we would reccomend using the LSTM RNN model for its highly performant deep learning predictive power, whereas we would reccomend using the Prophet model when development time and ease of use is paramount.

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

