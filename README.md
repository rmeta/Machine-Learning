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

<h1>HW4: Bayesian Classification and Dimensionality Reduction</h1>

<h2>Part 1</h2>
<p>Implement a Bayesian classifier using Gaussian distributions on the Breast_cancer dataset, achieving about 90% accuracy. The dataset includes 6 attributes and no missing values, with 'diagnosis' as the target variable. Feature independence is checked through scatter plots, and Gaussian distributions are calculated for each predictor.</p>

<h2>Part 2</h2>
<p>Apply PCA to reduce the dataset's dimensions from 5 to 3, capturing 99.5% of the variance. The reduced dataset is then used in the Bayesian classifier, improving accuracy to 98% compared to the original dataset.</p>

<h1>HW5: Neural Networks and Sequential Models</h1>

<h2>Question 2: Sequential Model with Dense Layers</h2>
<p>The breast_cancer dataset is loaded and split into training and testing sets. A Sequential model with dense layers using the <code>Relu</code> activation function is built. The model is compiled with the <code>adamax</code> optimizer, and training is conducted with a learning rate scheduler and early stopping to avoid overfitting.</p>

<h2>Question 3: RNN with Embeddings</h2>
<p>The IMDB dataset is preprocessed, transforming text data into embeddings. A recurrent neural network (RNN) with LSTM layers is implemented, using an embedding layer to map words to vector space. Early stopping and checkpoints are used for optimal training.</p>

<h2>Question 4: GRU Model</h2>
<p>A GRU (Gated Recurrent Unit) model is employed for classification, similar to the LSTM model in question 3. The GRU model shows improved performance over LSTM with a higher accuracy and less overfitting.</p>

<h2>Question 5: LSTM Model</h2>
<p>An LSTM model is used to classify the data, showing slightly better training accuracy than the GRU model but with signs of overfitting in the test set, leading to lower test accuracy.</p>

<h2>Question 6: Bidirectional LSTM</h2>
<p>A bidirectional LSTM is implemented to capture context from both directions of the input sequences. This model achieves higher accuracy by considering both past and future information simultaneously.</p>

<h2>Question 7: Complex Model with Multiple Outputs</h2>
<p>A complex neural network model with multiple output layers is built using the <code>functional</code> API in Keras. Despite its complexity, the model experiences overfitting and underperforms compared to simpler architectures like the bidirectional LSTM or GRU.</p>

<h1>HW6: Neural Network Training and Optimization Techniques</h1>

<p>The Fashion MNIST dataset, consisting of 60,000 training and 10,000 test images, was normalized and used to train a Sequential neural network with 128 neurons in the first dense layer and 10 output neurons using <code>softmax</code>. Optimizers such as Adam and SGD were applied, with Adam achieving 90.66% accuracy after 10 epochs. Additional layers and dropout (0.3 probability) were added to prevent overfitting. Callbacks like <code>LearningRateScheduler</code>, <code>EarlyStopping</code>, and <code>ReduceLROnPlateau</code> were used to dynamically adjust learning rates and stop training when improvements halted. Finally, the <code>ModelCheckpoint</code> callback ensured the model was saved after each epoch with validation improvements, preserving training progress.</p>

<h1>UBC ML Course Project: COVID-19 Patient Intubation Prediction</h1>

<p>This project focuses on developing machine learning models to predict the need for intubation in COVID-19 patients using clinical data. The dataset, sourced from Kaggle, contains over a million entries with 21 features. Models such as Logistic Regression, K-Nearest Neighbors (KNN), and Artificial Neural Networks (ANN) were implemented to perform binary classification, with PCA used for dimensionality reduction. The Logistic Regression model with Binary Cross-Entropy cost function achieved the highest accuracy (96.85%). KNN also performed well after PCA but required more computational resources. Logistic Regression was deemed the best model due to its high accuracy and computational efficiency.</p>

