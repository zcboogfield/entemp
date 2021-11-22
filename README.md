# EnTemp
EnTemp displays average daily temperatures and agregates for January - October 2020.
The data is sourced from the National Oceanic Atmospheric Administration. 
It is a Django app that can be run either locally or with Docker.

Current installation assumes you have Python3 and Pip installed locally.
Clone the repo and follow which ever set of instructions you're feeling:
## Docker Instructions
	Install Docker, Docker-Compose 
	Spin up container: `docker-compose up`
	
	If you add additional packages to the README you'll need to rebuild the contianer with: 
	`docker-compose build`
	
## Local Instructions
	`pip install -r requirements.txt`
	`python manage.py runserver 0.0.0.0:8000`
	
With either set of instructions you will be able to go to `[Local Host](http://localhost:8000)` and see the `EnTemp` landing page.

## Assessment ##
The majority of the logic is in `entemp/views.py` as the `entemp_view` function. 
There is a `temp_page` template under templates.

## Backlog ##
### TODO ###
- Look at performance of the scraper by converting to pure lxml.
- Style the template a bit.
- Use Actual Django Model? 

### Completes ###
- Build a Temp Page Tempalte.
- Writeup README
	- Docker Instructions
	- Local Python Instructions
- Add Average Temperature Column.
- Scrape the Data from the Site.
- Init EnTempView
- Get Initial Django/Docker setup going.
- Init README.md
