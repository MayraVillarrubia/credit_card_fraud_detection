![credit card banner](images/banner-credit-card-fraud.jpg "Credit card fraud detection banner")

<hr style="border:2px solid gray">

# Credit card fraud detection :moneybag: :supervillain: :supervillain_woman:
Credit Card Fraud Prediction using `Logistic Regression`


### Context
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

### Objetive
Predict fraudulent transactions with the highest precision possible, using machine learning. 

### Info about Dataset
The dataset contains transactions made by credit cards in September 2013 by European cardholders.
It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, is not possible provide the original features and more background information about the data.

* The dataset has 284.807 rows and 31 columns. 
* Features V1, V2, … V28 are the principal components obtained with PCA. 
* Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. 
* The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. 
* Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.
* In the entire dataset, there are only 492 fraudulent out of 284,807 transactions.

### Jupyter Notebook table of contents
Go to: [Notebook with modeling process](analysis.ipynb)


<ol>
    <li><a href= "#Import libraries">Import libraries</a></li>
    <li><a href= "#Download dataset">Download dataset</a></li>
    <li><a href="#Preprocesing">Preprocesing</a></li>
    <li><a href="#Unbalanced data">Unbalanced data</a>
        <ol>
            <li><a href="#Define X">Define X (independent varibales)</a></li>
            <li><a href="#Define y">Define y (dependent or target variable)</a> </li>
            <li><a href="#Normalize X set">Normalize X set</a></li>
            <li><a href="#Define train/test set">Define train/test set: StratifiedShuffleSplit</a></li>
            <li><a href="#Modeling:LogisticRegression">Modeling: LogisticRegression</a></li>
            <li><a href="#Predictions">Predictions</a></li>
            <li><a href="#Metrics">Metrics</a>
                <ol>
                    <li><a href="#Classification Report">Classification Report</a></li>
                    <li><a href="#jaccard Score">Jaccard Score</a></li>
                    <li><a href="#F1-Score">F1-score</a></li>
                    <li><a href="#Accuracy Score">Accuracy Score</a></li>
                </ol>
            </li>
        </ol>
    </li>
    <li><a href="#Balanced data">Balanced data</a>
        <ol>
            <li><a href="#Define X">Define X (independent varibales)</a></li>
            <li><a href="#Define y">Define y (dependent or target variable)</a> </li>
            <li><a href="#Normalize X set">Normalize X set</a></li>
            <li><a href="#undersampling">Resample: Under sampling dataset</a></li>
            <li><a href="#Define train/test set">Define train/test set: StratifiedShuffleSplit</a></li>
            <li><a href="#Modeling: LogisticRegression">Modeling: LogisticRegression</a></li>
            <li><a href="#Predictions">Predictions</a></li>
            <li><a href="#Metrics">Metrics</a>
                <ol>
                    <li><a href="#Classification Report">Classification Report</a></li>
                    <li><a href="#jaccard Score">Jaccard Score</a></li>
                    <li><a href="#F1-Score">F1-score</a></li>
                    <li><a href="#Accuracy Score">Accuracy Score</a></li>
                </ol>
            </li>
        </ol>
    </li>
</ol>

<hr style="border:1px black">

### Conclusions


### To do
- Dimensionality reduction
- Split train/test set using another approach to compare them with each other: train_test_split
- Resample: Random Over Sampler
