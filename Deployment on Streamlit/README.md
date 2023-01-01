# DEPLOYING OUR MODEL ON STREAMLIT

## **Objective:**

Our objective is to create a complete end-to-end product that can be used to predict the right cluster to which a customer belongs, based on his annual income and spending score. 

## **Process:**

1. When we have performed K Means Clustering based on our mall customers dataset and found out suitable cluster labels, we can now use it to create our own supervised model.
2. We use Random Forest Classifier to train our model and get maximum accuracy.
3. Now, we convert our model into a pickle file and load it on streamlit. 

## **Creating Supervised Model:**

Once we have obtained the clusters from K Means clustering, we can train our model to predict the cluster label on its own.

This will be based on only two features: Annual Income (k$) and Spending Score (1-100)

As a result for our model we will use Random Forest Regression to train on the previous dataset along with their respective cluster labels, and try to predict values.

## **Random Forest Classification:**

The Random forest or Random Decision Forest is a supervised Machine learning algorithm used for classification, regression, and other tasks using decision trees.

The Random forest classifier creates a set of decision trees from a randomly selected subset of the training set. It is basically a set of decision trees (DT) from a randomly selected subset of the training set and then It collects the votes from different decision trees to decide the final prediction.

## **Deployment On Streamlit:**

When our model is ready we convert it into a pickle file.


Pickle is a useful Python tool that allows you to save your ML models, to minimise lengthy re-training and allow you to share, commit, and re-load pre-trained machine learning models. 

We can use this pickle file and deploy our ML model on Streamlit. 

Streamlit is an open source app framework in Pyhon language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.


### SCREENSHOT

![Screenshot (339)](https://user-images.githubusercontent.com/73705676/208522859-dc034ec1-02bd-42f7-8887-4e9661901a34.png)

## **Conclusion:**

We have unsupervised ML algorithm to train our model amd predict accurate clusters for each customer based on their annual income and spending scores. 

Using this prediction and acquiring a complete dataset, we used the generated data to train our supervised ML model. 

We have successfully deployed our project on Streamlit to provide it with a user friendly interface as well. 

Hence, our end-to-end product is ready for use. 
