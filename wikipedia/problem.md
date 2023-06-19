#Problem

1. Identify the top 100 most viewed Wikipedia pages for a specified date (using the Wikimedia API: "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{year}/{month}/{day}")
1. For each page in the daily top 100, extract the associated "categories" (using the Wikipedia API: "https://en.wikipedia.org/w/api.php")
1. Save this information in BigQuery
1. Configure the process to run once a day
1. Backfill the data from April 1st, 2023, to the present
1. 

## 1 Identify top 100 Viewwd Pages

Using Postman to retrieve the GET - https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/2023/06/17

I see this JSON document: I truncated the snapshot

``` JSON 
{
    "items": [
        {
            "project": "en.wikipedia",
            "access": "all-access",
            "year": "2023",
            "month": "06",
            "day": "17",
            "articles": [
                {
                    "article": "Main_Page",
                    "views": 4493093,
                    "rank": 1
                },
                {
                    "article": "Special:Search",
                    "views": 1173012,
                    "rank": 2
                },
                {
                    "article": "Adipurush",
                    "views": 729010,
                    "rank": 3
                },
                {
                    "article": "The_Idol_(TV_series)",
                    "views": 594056,
                    "rank": 4
                }
            
                    ]
    }
        ]
}
```
Payload breakdown:

level 1 :  Items, get ready for a dump of nested data.
Level 2 :  looks like a manifest, describing the originating request. Followed by a list of records found belonging to the Request.
Level 3 :  Request SQL result data set.  The result informs us of the Article viewed, the number of veiws on the day, and rank. Rank appears to be the most viewed index for the query.  The most viewed page at 4,493,093 is the Wikipedia main page. After retrievinhg 1000 records the least viewd, in the results returns, is records 1000 is Gordon McQueen at 


``` JSON:
        {
            "article": "Gordon_McQueen",
            "views": 10322,
            "rank": 1000
        }
```
So a Rank of 1 is the most viewed, and a rank of 1000 is the least veiwed.



to fetch the top 50 viewed articles  we need  python function  passing in the Date to be reteived.

    get_top_100_wikipedia_pageviews_on ( vDate : datetime ):
        Take the above URL: https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{year}/{month}/{day}
        return in a JSON document  the articles ranked 1 to 100.


## 2 Retrweive and Wikipedia Article Categories:




