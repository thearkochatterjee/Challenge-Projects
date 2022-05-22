import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
import functions
import nltk
from nltk.corpus import stopwords
TweetUrl = 'https://github.com/aasiaeet/cse5522data/raw/master/db3_final_clean.csv'
tweet_dataframe = pd.read_csv(TweetUrl)

# wordDict maps words to id
# X is the document-word matrix holding the presence/absence of words in each tweet
wordDict = {}
idCounter = 0
for i in range(tweet_dataframe.shape[0]):
    allWords = tweet_dataframe.iloc[i, 1].split(" ")
    for word in allWords:
        if word not in wordDict and word not in stopwords.words('english'):
            wordDict[word] = idCounter
            idCounter += 1
X = np.zeros((tweet_dataframe.shape[0], idCounter), dtype='float')
print("we have reached X")
y = np.array(tweet_dataframe.iloc[:, 2])
print("we have reached Y")
# Copy your classifyNB() function and modify as specified
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2)
print("we defined train/test split")
# compute distributions here
probWordGivenPositive, probWordGivenNegative, priorPositive, priorNegative = functions.compute_distros(xTrain, yTrain)
min_prob = 1 / yTrain.shape[0]  # Assume very rare words only appeared once
logProbWordPresentGivenPositive, logProbWordAbsentGivenPositive = functions.compute_logdistros(probWordGivenPositive, min_prob)
logProbWordPresentGivenNegative, logProbWordAbsentGivenNegative = functions.compute_logdistros(probWordGivenNegative, min_prob)
logPriorPositive, logPriorNegative = functions.compute_logdistros(priorPositive, min_prob)
print(functions.classifyNB(xTest[700, ], logProbWordPresentGivenPositive,
                 logProbWordPresentGivenNegative,
                 logPriorPositive, logPriorNegative))
sumError = 0;
std = 0;
avgError = [0] * 10
for i in range(0, 10):
  xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2)
  avgError[i] = functions.testNB(xTest, yTest,
           logProbWordPresentGivenPositive,
           logProbWordPresentGivenNegative,
           logPriorPositive, logPriorNegative);
  sumError = sumError + avgError[i];
std = np.std(avgError)
mean = sumError/10
print("the mean is " + str(mean))
print("the std is " + str(std))