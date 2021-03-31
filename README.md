# Cali Median Income and Poverty Percentage
Data visualization of California's poverty percentage estimate and median household income in 2019. Data was imported from the United States Census Bureau and cleaned using Python, Bokeh, Pandas, and Jupyter Notebook.


## Running Locally

## Setup

Clone this repository:

`git clone https://github.com/valeriedania/CA-Poverty-And-Median-Income.git`

and [install Docker](https://docs.docker.com/get-docker/) on your platform

## Building

In the top level of this repository, execute the command

`docker build --tag cali-docker .`

## Running

Execute the command to start the Docker container:

`docker run --rm -p 5006:5006 cali-docker`


Now navigate to `http://localhost:5006` to interact with the demo site

## Live Video 

https://user-images.githubusercontent.com/73624288/113198758-4942c780-9234-11eb-873c-751af185e97a.mov

