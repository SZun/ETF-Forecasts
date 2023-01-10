# ETF Forecasts

In this project we are using historic ETF data from Yahoo Finance to predict/forecast historic ETF prices. The ETF's we are using are the ARK Innovation Fund (Ticker: ARKK), the SPDR S&P 500 ETF Trust (Ticker: SPY) and the Bank of Montreal MicroSectors FANG Index (Ticker: FNGU). We are using two machine learning models, the Facebook/Meta Prophet model as well as a Google Tensorflow LSTM Recurrent Neural Network models to predict/forecast these ETF prices. And we compare and contrast these different models and their performance against the real historic prices.

## [Video Presentation - Coming Soon](https://youtu.be/C1Gt66dgpBQ)

## Notebooks
- [Data Analysis](./Data-Exploration.ipynb)
- [Prophet Model Forecasting](./Prophet.ipynb)
- [LSTM RNN Forecasting](./LSTM_RNN.ipynb)
- [Model Analysis](./Prophet_vs_RNN_Analysis.ipynb)

## Analysis

### Data
The data that used was pulled from Yahoo Finance. The focus of the data was on three ETFs: ARKK, SPY, and FNGU. The timeframe of the data is from January of 2018 to March of 2022. To get a clear review and analysis of the data we used the "Adjusted Close" price.

### Facebook Prophet vs Tensorflow LSTM RNN Forecasting Results
@TODO

## Conclusion

## Getting Started

### Prerequisites
​
​You must have Python 3, Anaconda, Conda and Pip installed

```
$ python3 --version
Output: Python 3.10.8
$ anaconda --version
Output: anaconda Command line client (version 1.11.0)
$ conda --verison
Output: conda 22.9.0
$ pip -- verison
Ouput: pip 22.2.2 from /Users/{#User}/opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)
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

## Authors
- **Gabriel Millan** - [LinkedIn](https://www.linkedin.com/in/millangabriel/) | [Github](https://github.com/gjmillan)
- **Max Heatter** - [LinkedIn](https://www.linkedin.com/in/maxwell-heatter-ba4b03194/) | [Github](https://github.com/MaxHeatter)
- **Sam G. Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [Github](https://github.com/SZun)
- **Tim Clemens** - [Github](https://github.com/AmericanHacker)

