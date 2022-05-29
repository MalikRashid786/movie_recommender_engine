
# Movie Recommendation Engine 

Machine learning algorithms in recommender systems typically fit into two categories: content-based systems and collaborative filtering systems. Modern recommender systems combine both approaches.

We will be creating a content-based recommender.

## Content-Based Movie Recommendation Systems:

![Content1](https://user-images.githubusercontent.com/56771670/170863334-2408bc5d-5960-4dc2-9d5f-111bb5621e98.png)


Content-based methods are based on the similarity of movie attributes. Using this type of recommender system, if a user search one movie, similar movies are recommended. For example, if a user search a comedy movie starring Adam Sandler, the system will recommend them movies in the same genre or starring the same actor, or both. With this in mind, the input for building a content-based recommender system is movie attributes.

## Link to the working application

Check out -> https://movie-recommender-en.herokuapp.com


## Data Collection
Movie dataset Extracted the Dataset from the Kaggle you can also extract the data from this link https://www.kaggle.com/tmdb/tmdb-movie-metadata, Kaggle is an Open source and have a large community also they conduct competitions every month,Kaggle allows users to find and publish data sets, explore and build models in a web-based data-science environment, work with other data scientists and machine learning engineers, and enter competitions to solve data science challenges,Given the thousands of other people also doing them, it is becoming harder and harder for merely working through them to be enough to differentiate you. You'll learn a lot, but it won't make you stand out from your competition.Data scientists of all levels can benefit from the resources and community on Kaggle. Whether you are a beginner, looking to learn new skills and contribute to projects, an advanced data scientist looking for competitions, or somewhere in between, Kaggle is a good place to learn.


## Data Cleaning

Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled. If data is incorrect, outcomes and algorithms are unreliable, even though they may look correct. There is no one absolute way to prescribe the exact steps in the data cleaning process because the processes will vary from dataset to dataset. But it is crucial to establish a template for your data cleaning process so you know you are doing it the right way every time.

First Merging two tables(movies and credits tables) into one table on basis of movie title and Remove the unnecessary columns Below features doesn't require because it is not necessary it does not impact too much for the recommendation so we removing the below features from the table.

- id
- original_title
- genres
- keyword
- overview
- cast
- crew

Accessing required and important columns are('movie_id','title','overview','genres','keywords','cast','crew') and Find the NULL values we just remove the null values it has contains only 3 null values and "ast" Library performs a collection of nodes that are linked together based on the grammar of the Python language and applied the "ast" techniques to the genres and keywords columns and access the top 3 cast actor from the cast table and remaining actor was drop and create on the function to get the director name from crew column because there is a lot of workers name is there but we want just director name and remove the whitespace from the columns(Sam Worthington, Sam Johny) sometimes user enter Sam machine get confused that's why removing whitespace and also applied the same function for the director name, movies, caste and keywords columns and Splitting each word in overview columns Adding overview, genres, keywords, cast, and crew added into one table -->"Tag" Column table because of vectorization after merging the content of all data into one column Removing the columns overview, genres, keywords, cast and crew,

## Vectorization
Using Bag of Words Techniques for Vectorization
Text data is used in natural language processing (NLP), which interacts between humans and machines using natural language. Text data helps analyze movie reviews, products using Amazon reviews, etc. But the question that arises here is how to deal with text data when building a machine learning model? Text data is converted to a real-valued vector by various techniques. One such approach is Bag of Words (BoW), which will be discussed in this article. But why do we have to convert the text into a vector? Why can’t we use text data to build a machine learning model? Need for text vectorization Let’s say we have reviews of a product. Text reviews provided by the customers are of different lengths. By converting from text to numbers, we can represent a review by a finite length of the vector. In this way, the length of the vector will be equal for each review, irrespective of the text length. Bag of words is the most trivial representation of text into vectors. Each column of a vector represents a word. The values in each cell of a row show the number of occurrences of a word in a sentence.Vectorizing data into 5000 features and applying stop words it removes the unnecessary word from these column-like -->(Is, am, the, was, a, an).

## How to get the API key?
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

## How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![cosine](https://user-images.githubusercontent.com/56771670/170865193-b031df33-5a91-4f33-96c9-2635d17e8e25.png)

## Streamlit Framework

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps, We use the streamlit to develop the API for this project

Streamlit Tutorial : [https://streamlit.io/]

## Deployement on Heroku

Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Our platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market.

## Screenshots of Project
![screencapture-movie-recommender-en-herokuapp-2022-05-29-16_31_25](https://user-images.githubusercontent.com/56771670/170865293-9e196a9f-3adb-464a-bd4c-0518437c379d.png)


![Capture](https://user-images.githubusercontent.com/56771670/170865384-57b6533d-58d2-4136-8bd5-6a661c344350.PNG)


![screencapture-movie-recommender-en-herokuapp-2022-05-29-16_36_02](https://user-images.githubusercontent.com/56771670/170865315-bcfb314e-adfc-424c-a125-26a5b7f7efe1.png)


## Installation and Run

The Code is written in Python 3.10.4 If you don't have Python installed you can find it [here](https://www.python.org/downloads). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

Install Required Libraries

```bash
  Step 1: pip install -r requirements.txt
```
Running Project

```bash
 Step 2: streamlit run app.py
```

## Technologies Used
![nltk](https://user-images.githubusercontent.com/56771670/170866951-558a45d3-4e52-4d10-a107-2cfee56057dd.png) ![python](https://user-images.githubusercontent.com/56771670/170866942-8119b832-cfaf-43db-ac60-7c7cfcc6d84e.svg)   ![Numpy](https://user-images.githubusercontent.com/56771670/170866966-de240e4b-8c8a-481f-a6ac-758ba51db9a2.png) ![pandas](https://user-images.githubusercontent.com/56771670/170866968-9ccadd96-c2de-4939-b405-a1db1982cc7b.png) ![scikit learn](https://user-images.githubusercontent.com/56771670/170866969-c9f45dda-9df7-479c-9386-12242d275591.png) ![streamlit](https://user-images.githubusercontent.com/56771670/170866970-73872613-5607-4447-a6b0-9d46118d8c05.png)


