# CUSTOMER SEGMENTATION USING K -  MEANS CLUSTERING

## **Title:**
Customer Segmentation Using K Means Clustering


## **Problem Statement:**
We are given a dataset consisting of details regarding customers of a shopping mall. Based on this mall customers dataset, and performing K-means clustering, we need to segregate customers in form of optimal clusters.

**(Dataset link : https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)**

## **Objectives:**

1. To create accurate segments of customers based on similar annual income and spending score.
2. To understand the different kinds of customers and their needs. 
3. To make better business decisions by making suitable for policies for various types of customers.

	
##	**Clustering Algorithms:**

Clustering algorithms attempt to find natural clusters in the data and various aspects of how to tune and modify the algorithms used to cluster the data. 

Clustering is based on the principle that elements in the same cluster should be similar to each other. 
Data is grouped and related items are placed close together.

Using a clustering algorithm means you're going to give the algorithm a lot of input data with no labels and let it find any groupings in the data it can.
Clustering is used for things like feature engineering or pattern discovery.

When you're starting with data you know nothing about, clustering might be a good place to get some insight.


## **K - Means Clustering Algorithm:**

K-means clustering is an unsupervised machine learning algorithm that divides specified data into a specified number of clusters. Here 'K' is the specified number of defined clusters that need to be created.

This is a centroid-based algorithm where each cluster is associated with a centroid. The main idea is to reduce the distance between the data points and their respective cluster centroids.

The K-means clustering algorithm mainly performs two tasks:

1. Determines the best value for K center points or centroids by an iterative process.

2. Assigns each data point to its closest K-center. Those data points which are near to the particular K-center, create a cluster.

Hence each cluster has datapoints with some commonalities, and it is away from other clusters. 

It basically uses the elbow method to determine the optimum number of clusters.

K-means are very simple and easy to implement. It is highly scalable and applicable to both small and large datasets. However, there is a problem with choosing the number of clusters or K. Also, as the dimensionality increases, the stability decreases. Overall, however, K-means is a simple and robust algorithm that makes clustering very easy.


## **Process:**

1. Understanding the data.
2. Performing the elbow method to find optimal number of clusters.
3. Training a model using unsupervised learning algorithm (K - means).
4. Plotting the clusters.


## **Mall Customers Data Segmentation:**

The mall customer data is an interesting data set of hypothetical customer data. It puts you in the shoes of a supermarket owner. We have customer data and based on that we need to divide the customers into different groups.

The data includes the following features:

1. Customer ID

2. Customer Gender

3. Customer Age

4. Annual Income of the customer (in Thousand Dollars)

5. Spending score of the customer (based on customer behaviour and spending nature)

The data has 200 entries, that is data from 200 customers.

The foremost step includes determining the relationship of all features within the dataset. We do this with the help of a heatmap.

### HEATMAP SHOWING RELATIONSHIP BETWEEN ALL FEATURES

![image](https://user-images.githubusercontent.com/73705676/205503314-0a23e6cb-51c9-438a-bbe9-f979b94208d8.png)



We first observed the distributions of Annual Income and the Spending Scores of the customers present int the dataset.

### DISTRIBUTION OF SPENDING SCORE IN THE DATASET
![image](https://user-images.githubusercontent.com/73705676/205504547-e79de05d-7039-4ebc-bfad-10ed3409d4af.png)

### DISTRIBUTION OF ANNUAL INCOME IN THE DATASET
![image](https://user-images.githubusercontent.com/73705676/205504473-f8a85890-6c53-4b2a-a751-e267f5372528.png)


Then we try to determine the number of clusters that can be formed based on these two features using the elbow method.

### ELBOW PLOT
![image](https://user-images.githubusercontent.com/73705676/205504596-60195681-ce3c-4abd-a8f2-db8adfe955c6.png)


From this graph, we find that optimally 5 clusters can be formed with labels starting from 0 to 1.

### SCATTER PLOT
![image](https://user-images.githubusercontent.com/73705676/205504812-9381b0dd-9f39-4035-8283-3281e6dbdc5c.png)



It can be clearly seen that five distinct clusters formed from the data. 

1. The brown cluster (label = 2) is the lowest-income, lowest-spending customers

2. Similarly the orange cluster (label = 1) is the highest-income, highest-spending customers.

3. Whereas, the red cluster (label = 4) is the group of customers with moderate income and moderate spending score.


## **Conclusion:**

Hence we can say company should target the orange cluster (label = 1) and the red cluster (label = 4) in order to increase their sales and gnerate maximum revenue. 
