<h1>HW1: Time Series Analysis and Forecasting</h1>

<h2>Part 1</h2>
<p>Preprocess time series data (Brent Spot Price, Coal Power consumption) by converting the date to a <code>datetime</code> format, applying rolling averages, and conducting stationarity tests using the Augmented Dickey-Fuller (ADF) test.</p>

<h2>Part 2</h2>
<p>Perform seasonal decomposition of the time series data into trend, seasonal, and residual components, followed by generating autocorrelation (ACF) and partial autocorrelation (PACF) plots for further analysis.</p>

<h2>Part 3</h2>
<p>Implement time series forecasting models, including AutoRegressive (AR), ARIMA, and SARIMA, to predict future values, and evaluate the models using visual plots and statistical metrics like AIC.</p>

<h1>HW2: K-Means Clustering</h1>

<p>In this task, we first load the data using Pandas and extract the second and third columns into an array. We then apply the k-means algorithm: initially, each point is randomly assigned to a cluster, and the mean of points in each cluster is computed. Points are reassigned to the nearest cluster center, and this process continues until the change in the cost function (the sum of distances from points to their cluster centers) is minimal between iterations.</p>

<h1>HW3: Decision Tree Classification and Pruning</h1>
<p>The Adult dataset is divided into ten subsets of 3,256 unique records. Datasets df1 to df9 are used for training, and df10 for evaluation. After encoding categorical features, decision trees are trained, and metrics such as accuracy, recall, F1-score, and confusion matrix are calculated. Post-pruning is applied to select the optimal alpha, minimizing overfitting by balancing training and test performance.</p>
