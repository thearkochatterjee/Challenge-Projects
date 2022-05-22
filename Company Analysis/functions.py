import numpy as np
import math
def compute_distros(x, y):
    # probWordGivenPositive: P(word|Sentiment = +ive)
    probWordGivenPositive = np.sum(x[y >= 0, :],
                                   axis=0)  # Sum each word (column) to count how many times each word shows up (in positive examples)
    probWordGivenPositive = probWordGivenPositive / np.sum(
        y >= 0)  # Divide by total number of (positive) examples to give distribution

    # probWordGivenNegative: P(word|Sentiment = -ive)
    probWordGivenNegative = np.sum(x[y < 0, :], axis=0)
    probWordGivenNegative = probWordGivenNegative / np.sum(y < 0)

    # priorPositive: P(Sentiment = +ive)
    priorPositive = np.sum(y >= 0) / y.shape[0]  # Number of positive examples vs. all examples
    # priorNegative: P(Sentiment = -ive)
    priorNegative = 1 - priorPositive
    #  (note these last two form one distribution)

    return probWordGivenPositive, probWordGivenNegative, priorPositive, priorNegative


def compute_logdistros(distros, min_prob):
    if True:
        # Assume missing words are simply very rare
        # So, assign minimum probability to very small elements (e.g. 0 elements)
        distros = np.where(distros >= min_prob, distros, min_prob)
        # Also need to consider minimum probability for "not" distribution
        distros = np.where(distros <= (1 - min_prob), distros, 1 - min_prob)

        return np.log(distros), np.log(1 - distros)
    else:
        # Ignore missing words (assume they have P==1, i.e. force log 0 to 0)
        return np.log(np.where(distros > 0, distros, 1)), np.log(np.where(distros < 1, 1 - distros, 1))


# classifyNB:
#   words - vector of words of the tweet (binary vector)
#   logProbWordPresentGivenPositive - log P(x_j = 1|+)
#   logProbWordPresentGivenNegative - log P(x_j = 1|-)
#   logPriorPositive - log P(+)
#   logPriorNegative - log P(-)
#   returns (label of x according to the NB classification rule, confidence about the label)

def classifyNB(words, logProbWordPresentGivenPositive,
               logProbWordPresentGivenNegative,
               logPriorPositive, logPriorNegative):
    logProbWordPresentGivenNegative = logProbWordPresentGivenNegative.tolist()
    logProbWordPresentGivenPositive = logProbWordPresentGivenPositive.tolist()

    # fill in function definition here
    logProbTweetPos = logPriorPositive
    logProbTweetNeg = logPriorNegative
    length = len(words.tolist())
    for i in range(0, length):
        logProbTweetPos = logProbTweetPos + logProbWordPresentGivenPositive[i]
        logProbTweetNeg = logProbTweetPos + logProbWordPresentGivenNegative[i]
    if (logProbTweetPos > logProbTweetNeg):
        binaryValue = 1
    else:
        binaryValue = 0
    if (logProbTweetPos == 0):
        strength = math.log(abs(logProbTweetNeg))
    elif (logProbTweetNeg == 0):
        strength = math.log(abs(logProbTweetPos))
    else:
        strength = abs(math.log(abs(logProbTweetPos)) - math.log(abs(logProbTweetNeg)))
    return (binaryValue, strength)


def testNB(xTest, yTest,
           logProbWordPresentGivenPositive,
           logProbWordPresentGivenNegative,
           logPriorPositive, logPriorNegative):
  true = 0;
  for i in range(0, len(xTest.tolist())):
    binaryvalue, strength = classifyNB(xTest[i],logProbWordPresentGivenPositive,
               logProbWordPresentGivenNegative,
               logPriorPositive, logPriorNegative)
    if binaryvalue == yTest[i]:
      true = true + 1
  # compute avgErr
  avgErr =  true/len(xTest)
  print("Average error of NB is", avgErr)
  return avgErr