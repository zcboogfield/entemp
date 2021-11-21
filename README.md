# EnTemp
EnTemp displays average daily temperatures and agregates for January - October 2020.
The data is sourced from the National Oceanic Atmospheric Administration. 
It is a Django app that can be run either locally or with Docker.

Current installation assumes you have Python3 and Pip installed locally.
## Docker Instructions
	Install Docker, Docker-Compose 
	Spin up container: `docker-compose up`
	
	If you add additional packages to the README you'll need to rebuild the contianer with: 
	`docker-compose build`
	
## Local Instructions
	`pip install -r requirements.txt`
	`python manage.py runserver 0.0.0.0:8000`
	
With either set of instructions you will be able to go to `[localhost:8000](localhost:8000)` and see the `EnTempView`

## Backlog ##
### TODO ###
- Build a TemperatureTemplate.
- Look at performance of the scraper by converting to pure lxml.
- Use Actual Django Model? 

### Completes ###
- Writeup README
	- Docker Instructions
	- Local Python Instructions
- Add Average Temperature Column.
- Scrape the Data from the Site.
- Init EnTempView
- Get Initial Django/Docker setup going.
- Init README.md
