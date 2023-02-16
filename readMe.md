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
