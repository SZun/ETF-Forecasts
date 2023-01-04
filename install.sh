conda activate base
conda create -n etf_forecasting_env python=3.7 -y
conda activate etf_forecasting_env
conda install -c conda-forge yfinance -y
conda install -c anaconda scikit-learn -y
conda install -c anaconda pandas -y
conda install -c anaconda numpy -y
conda install -c conda-forge matplotlib -y
conda install -c conda-forge hvplot -y
conda install -c conda-forge holoviews -y
pip install pystan
pip install prophet
pip install tensorflow