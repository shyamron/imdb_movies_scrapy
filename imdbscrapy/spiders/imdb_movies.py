import scrapy
class ImdbMoviesSpider(scrapy.Spider):
    name = 'imdb_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = 'http://www.imdb.com/'
    genres=['action']

    def start_requests(self):
        urls=[]
        for genre in self.genres:
            urls.append(f"{self.start_urls}/search/title/?genres={genre}&languages=en&sort=user_rating,desc&title_type=feature")
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        movies_list=response.css('div.lister-list')
        for movie in movies_list:
            movies=movie.css('div.lister-item.mode-advanced')
            year=''
            title=''
            rating=''
            reviews=''
            directors_actors=''
            genres=''
            gross=''
            runtime=''
            for items in movies:
                rating=items.css("div.inline-block.ratings-imdb-rating strong::text").get()
                runtime=items.css("span.runtime::text").get()
                year=items.css('span.lister-item-year.text-muted.unbold::text').get()
                title=items.css("h3.lister-item-header a::text").get()
                genres=items.css("p.text-muted  span.genre::text").get()
               
                for item in items.css('p.sort-num_votes-visible'):
                    reviews=item.css("span:nth-child(2)::text").get()
                    gross=item.css('span:nth-child(5)::text').get()
                    
                for item in items.css('div.lister-item-content'):
                    for names in item.xpath('.//p[3]'):
                        directors_actors = [name.strip() for name in names.css('::text').extract()]
                yield{
                    "year":year,
                    "title":title,
                    'rating':rating,
                    'no_of_reviews':reviews,
                    'directors_actors':directors_actors,
                    'genres':genres.strip(),
                    'runtime':runtime,
                    'gross':gross
                }

        next_page = response.css('a.lister-page-next.next-page').attrib['href']
        next_page = f"{self.start_urls}/{next_page}"
        print(f"temp:{next_page}")
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)      


       