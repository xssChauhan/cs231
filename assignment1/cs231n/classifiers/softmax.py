import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  dW = np.zeros_like(W)
  for e in range(num_train):
      scores = np.dot(W.T , X[e])
      scores -= np.max(scores)
      exp = np.exp(scores)
      sums = np.sum(exp)
      l = -np.log(
        exp[y[e]]/sums
      )
      for j in range(num_classes):
          if j == y[e]:
              dW[:,j] += (-1 + (exp[j]/sums))*X[e]
          else:
              dW[:,j] += ( exp[j]/sums) * X[e]
      loss += l 
  loss = loss/num_train + 0.5*reg*np.sum(W*W)
  dW = dW/num_train + reg*W 
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  num_train = X.shape[0]
  num_classes = X.shape[1]
  loss = 0.0
  dW = np.zeros_like(W)
  scores = np.dot(X, W)
  scores -= np.max(scores, axis = 1)[:,None] #Normalize along each row
  exp = np.exp(scores)
  sums = np.sum(exp , axis = 1) #Sum along each row
  loss = np.log(sums)
  loss -= scores[np.arange(num_train),y]
  loss = np.sum(loss)/float(num_train) + 0.5*reg*np.sum(W*W)
  Grad = exp/sums[:,None]
  Grad[np.arange(num_train),y] += -1
  dW = np.dot(X.T,Grad)/float(num_train) + reg*W
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

