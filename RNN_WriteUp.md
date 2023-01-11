
## LSTM Networks

Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work.1 They work tremendously well on a large variety of problems, and are now widely used.
 
 
For this project we decided to use our Machine Learning knowledge to create a forecast of 3 ETFs. We started by preparing a dataset for each symbol that we deemed appropriate for a 60 forecast.

From our research of a basic model we initially ran the model within base metrics such as the amount of neurons, bath size, and epochs.

## Evaluation
To evaluate our metrics we used 3 evaluation functions<br>


## Mean Absolute Error
ARK<br>
Mean Absolute Error: 69.88 <br>
SPY<br>
Mean Absolute Error: 436.76<br>
FNGU<br>
Mean Absolute Error: 246.19<br>
![](Resources/images/markdown/LSTM_RNN_mean_absolute_error.png)


## Mean Squared Error
ARKK<br>
Mean Squared Error: 4954.66 <br>
SPY<br>
Mean Squared Error: 190968.11<br>
FNGU<br>
Mean Squared Error: 64041.9<br>

![](Resources/images/markdown/LSTM_RNN_mean_squared_error.png)<br>
## Root Mean Squared Error
ARKK<br>
Root Mean Squared Error: 70.39 <br>
SPY<br>
Root Mean Squared Error: 437.0<br>
FNGU<br>
Root Mean Squared Error: 253.07<br>

![](Resources/images/markdown/LSTM_RNN_root_mean_squared_error.png)

Our first run had a score of <br>
Mean Absolute Error (MAE)  ??<br>
Mean Squared Error(MSE) ??<br>
Root Mean Squared Error(RMSE) ??<br>

Upon notice that our model was performing poorly  we then started  series of parameter changes..<br>


![]((Resources/images/markdown/LSTM_RNN_actual_vs_forecasted_etf_adjusted_closing_prices.png)<br>


-----------------------------

![](Resources/images/plots/LSTM_RNN_arkk_actual_vs_forecasted_etf_adjusted_closing_prices_old.png)<br>
![](Resources/images/plots/LSTM_RNN_fngu_actual_vs_forecasted_etf_adjusted_closing_prices_old.png)<br>
![](Resources/images/plots/LSTM_RNN_spy_actual_vs_forecasted_etf_adjusted_closing_prices_old.png)<br>





Mean Absolute Error<br>
ARKK<br>
Mean Absolute Error: 70.06<br>
SPY<br>
Mean Absolute Error: 437.51<br>
FNGU<br>
Mean Absolute Error: 246.58<br>

Mean Squared Error<br>
ARKK<br>
Mean Squared Error: 4980.48<br>
SPY<br>
Mean Squared Error: 191625.72<br>
FNGU<br>
Mean Squared Error: 64249.17<br>

Root Mean Squared Error<br>
ARKK<br>
Root Mean Squared Error: 70.57<br>
SPY<br>
Root Mean Squared Error: 437.75<br>
FNGU<br>
Root Mean Squared Error: 253.47<br>



---------------------------------------------------<br>
---------------------------------------------------<br>



![](Resources/images/markdown/LSTM_RNN_arkk_actual_vs_forecasted_etf_adjusted_closing_prices-Copy1.png)<br>
![](Resources/images/markdown/LSTM_RNN_fngu_actual_vs_forecasted_etf_adjusted_closing_prices-Copy1.png)<br>
![](Resources/images/markdown/LSTM_RNN_spy_actual_vs_forecasted_etf_adjusted_closing_prices-Copy1.png)<br>



ARKK<br>
Mean Absolute Error: 69.89<br>
Mean Squared Error: 4956.04<br>
Root Mean Squared Error: 70.4<br>



SPY<br>
Mean Absolute Error: 436.76<br>
Mean Squared Error: 190964.25<br>
Root Mean Squared Error: 436.99<br>


FNGU<br>
Mean Absolute Error: 246.26<br>
Mean Squared Error: 64077.45<br>
Root Mean Squared Error: 253.14<br>