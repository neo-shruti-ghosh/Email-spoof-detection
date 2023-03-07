# Approach

- Collect a dataset of email messages, including both legitimate and spoofed emails. You can use publicly available datasets or create your own by generating spoofed emails.

- Preprocess the dataset by extracting features from the email messages. Some of the important features that can be used for detecting spoofed emails are sender's email address, domain name, IP address, email header information, email body, etc.

- Create an AIML model that uses the extracted features to classify emails as either legitimate or spoofed. You can use any of the classification algorithms supported by AIML, such as decision trees, naive Bayes, etc.

- Train the model on the preprocessed dataset and test its accuracy on a validation set. You can use cross-validation to ensure that the model is not overfitting the training data.

- Once the model is trained and validated, you can deploy it as a web service that accepts an email message and returns a binary label indicating whether the email is legitimate or spoofed.

- Finally, you can test the model's performance on new email messages to evaluate its effectiveness in detecting spoofed emails.

# 1. Collecting Dataset

- We used public datasets
- This time we used the dataset Enron Email Dataset to train our model
- This is a 1.4GB dataset with legit as well as spoofed emails
- The folder containing the dataset is named as "DataSet"

# 2. Preprocessing of Data

Steps for preprocdessing of data

- Data Cleaning: Remove any unnecessary or redundant data in the dataset. This includes removing duplicate emails, emails with incomplete or missing data, and irrelevant or outdated emails.

- Email Parsing: Extract relevant information from the emails, such as the sender's email address, domain name, IP address, email header information, email body, and other relevant features that could help in detecting email spoofing.

- Feature Selection: Select the most relevant features for detecting email spoofing. You can use various techniques for feature selection, such as correlation analysis, mutual information, or principal component analysis.

- Feature Encoding: Convert categorical data into numerical data that can be processed by the machine learning algorithm. One way to do this is to use one-hot encoding to convert categorical data into binary vectors.

- Data Balancing: Ensure that the dataset is balanced to prevent bias in the machine learning model. This can be done by oversampling the minority class, undersampling the majority class, or using synthetic data generation techniques.

- Data Normalization: Normalize the numerical data to a common scale to prevent features with larger ranges from dominating the model training.

- Train-Test Split: Split the preprocessed dataset into a training set and a test set. The training set is used to train the machine learning model, while the test set is used to evaluate the model's performance.

#Training the Model

Steps to train the model using logistic regression

- Data Preparation: First, you need to prepare your data by collecting and cleaning the dataset. The dataset should be organized into input features (also known as independent variables or predictors) and the target variable (also known as the dependent variable or response variable). The input features can be continuous or categorical. If there are categorical variables, they may need to be one-hot encoded or converted to numerical values. The target variable should be binary (0 or 1) or ordinal (for multi-class classification).

- Splitting Data: Next, you need to split your dataset into training and testing sets. The training set is used to train the model, and the testing set is used to evaluate the performance of the trained model. A common ratio is 70-30 or 80-20 for training and testing data.

- Model Selection: Logistic regression can have a regularization parameter, known as C, which controls the strength of the regularization. To select the best value for the regularization parameter, you can perform cross-validation on the training data to find the optimal C value. Cross-validation involves splitting the training data into several folds and training the model on each fold while using the rest of the folds for validation.

- Model Training: Once you have selected the optimal C value, you can train the logistic regression model on the entire training set using that value. During training, the model tries to learn the relationship between the input features and the target variable by minimizing the loss function.

- Model Evaluation: After training the model, you can evaluate its performance on the testing set. The most commonly used metric for binary classification problems is the accuracy, which measures the percentage of correctly classified samples. Other metrics like precision, recall, and F1 score may also be used depending on the problem.

- Model Optimization: If the performance of the model is not satisfactory, you can try optimizing the model by tweaking hyperparameters, changing features, adding more data, or using different regularization methods.

- Model Deployment: Once you have a satisfactory model, you can deploy it in a real-world environment and use it to make predictions on new data.

Overall, training a logistic regression model involves data preparation, splitting data, model selection, model training, model evaluation, model optimization, and model deployment.

# Installation

- copy the following codes into your terminal where the project is saved: <br>
-- pip install Flask <br>
-- python app.py <br>
The app will run on a localhost as specified by the terminal <br>

# Screenshots

- Checking spam <br>
![image](https://user-images.githubusercontent.com/51224831/223398446-694fb5bb-36f5-4af4-9427-ae43ee862a41.png) <br>
- Checking ham <br> 
![image](https://user-images.githubusercontent.com/51224831/223398823-1085dc3e-0733-4221-8c83-7b5a8dbd50b2.png)



