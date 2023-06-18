#Problem

1. Identify the top 100 most viewed Wikipedia pages for a specified date (using the Wikimedia API: "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{year}/{month}/{day}")
1. For each page in the daily top 100, extract the associated "categories" (using the Wikipedia API: "https://en.wikipedia.org/w/api.php")
1. Save this information in BigQuery
1. Configure the process to run once a day
1. Backfill the data from April 1st, 2023, to the present
