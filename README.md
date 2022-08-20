
# Price Prediction for EdTech company

* Price is a prominent factor in influencing the buying decisions of the people. Price optimization has become crucial for institutes to drive student and profitability.
* It also plays a major role in churn rate reduction of student.
* Price optimization reduces the manual work and minimizes the possibility of any human errors.
* Competitor Price behavior analysis is done which can assist Institutes for making better pricing decisions.

# Data Collection and Business Understanding

* First understanding about business problem.
* Listing out the various factors affecting the price prediction.
* Selecting important features for meeting the business target.
* Web scrapping through various Ed-Tech websites and enquiry.
* Handled noise data and generated random data.
* Considering all the necessary details and storing in the database.


## Tech Stack

**Tech Used:** Vs Code for working on models, Jupyter Notebook, 
Postgresql, Python, html, css

**Libraries Used:** ***Pandas*** for Data Manipulation, ***matplotlib*** 
and ***seaborn*** for data visualizaiton, ***make_pipe*** for making pipeline, 
***column_transformer*** for encoding data before training ***sklearn*** for data preprocessing 
and model building, ***Flask*** for web application, and ***heroku*** for deployment.

## EDA and Data Preprocessing

Not much Preprocessing was needed, removed some unnecessary columns

## Model building
In order to get the best accuracy following models were used:

    1. Random Forest Regressor
    2. Linear Regression
    3. Support Vector Regressor 
    4. KNeighbours Regressor

Out of which KNeighbours Regressor performed well with test accuracy of 99% 
and train accuracy of 98% and pickled for model deployment.

## Model deployment
Model was deployed on Heroku.

Deployment link:- https://price-prediction-for-courses.herokuapp.com/
