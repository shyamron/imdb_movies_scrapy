Making own IMDB movies dataset using scrapy

This project makes use of scrapy, a free and open source web crawling framework to scrape "action" movies from
imdb.com website. Link- https://www.imdb.com/search/title/?genres=action&languages=en&sort=user_rating,desc&title_type=feature
 Following data are extracted:

1. Title
2. Actors and Directors
3. Released year
4. Runtime
5. Gross amount in $
6. Rating
7. Number of Reviews


imdbscrapy\imdbscrapy\spiders\imdb_movies.py is the main scraper and movies.csv is the extracted dataset.
The dataset contains total of 20,464 action movies.


References:
1. https://www.datacamp.com/tutorial/making-web-crawlers-scrapy-python
2. https://www.experfy.com/blog/using-scrapy-to-build-your-own-dataset
