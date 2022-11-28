# Customer-Segmentation-Using-K-Means-Clustering


Clustering Algorithms:

Clustering algorithms attempt to find natural clusters in the data and various aspects of how to tune and modify the algorithms used to cluster the data. Clustering is based on the principle that elements in the same cluster should be similar to each other. Data is grouped and related items are placed close together.


K-Means Clustering Algorithm:

K-Means clustering is an unsupervised machine learning algorithm that divides specified data into a specified number of clusters. where 'K' is the specified number of defined clusters that need to be created.

This is a centroid-based algorithm where each cluster is associated with a centroid. The main idea is to reduce the distance between the data points and their respective cluster centroids.

This algorithm takes raw unlabeled data as input and divides the data set into clusters. This process is repeated until the best cluster is found.

K-Means are very simple and easy to implement. It is highly scalable and applicable to both small and large datasets. However, there is a problem with choosing the number of clusters or K. Also, as the dimensionality increases, the stability decreases. Overall, however, K Means is a simple and robust algorithm that makes clustering very easy.


Mall Customer Segmentation:

The mall customer data is an interesting data set of hypothetical customer data. It puts you in the shoes of a supermarket owner. We have customer data and based on that we need to divide the customers into different groups.

The data includes the following features:

1. Customer ID

2. Customer Gender

3. Customer Age

4. Annual Income of the customer (in Thousand Dollars)

5. Spending score of the customer (based on customer behaviour and spending nature)

The data has 200 entries, that is data from 200 customers.


We first observed the distributions of Annual Income and the Spending Scores of the customers present int the dataset.

![annual income-removebg-preview](https://user-images.githubusercontent.com/73705676/204354114-09c30f23-1140-44b9-ae68-5ab0ab24a3d2.jpg)
![spending score-removebg-preview](https://user-images.githubusercontent.com/73705676/204354155-f669d39a-322b-4572-954f-732112fd187c.jpg)



Then we try to determine the number of clusters that can be formed based on these two features using the elbow method

![elbow-removebg-preview](https://user-images.githubusercontent.com/73705676/204354499-6ddbb24c-2f7d-431d-a669-3c8852e3ff2f.jpg)


From this graph, we find that 5 clusters can be formed with labels starting from 0 to 1.

![scatterplot-removebg-preview](https://user-images.githubusercontent.com/73705676/204353482-443949c5-b5b9-492b-a1fb-0b56744ddb5f.jpg)



It can be clearly seen that five distinct clusters formed from the data. The fourth cluster is the lowest-income, lowest-spending customers, and similarly the second cluster is the highest-income, highest-spending customers.

The mall should thus, develop policies that are more favourable for the second cluster of customers. 
