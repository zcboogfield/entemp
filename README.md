# EnTemp
EnTemp displays average daily temperatures and agregates for January - October 2020.
The data is sourced from the National Oceanic Atmospheric Administration. 
It is a Django app that can be run either locally or with Docker.

## Docker Instructions
	Install Docker, Docker-Compose, Python, Pip 
	
## Local Instructions
	`pip install -r requirements.txt`
	
With either set of instructions you will be able to go to `[localhost:8000](localhost:8000)` and see the `EnTempView`

## Backlog ##
### TODO ###
- Scrape the data from the site.
	- Use Actual Django Model? 
- Build a TemperatureTemplate.
	- Add Average Temperature Column.
	- Add average aggregate Column.
	- Add standard deviation aggregate Column.

- Writeup README
	- Docker Instructions
	- Local Python Instructions
### Completes ###
- Init EnTempView
- Get Initial Django/Docker setup going.
- Init README.md
