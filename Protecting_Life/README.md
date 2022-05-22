# Protecting Life

### Instructions

For this repo we have taken a slightly different approach. The data extraction and assembly components are seperated from the analysis side. To understand this better especially if you a new to Python we recommend starting with the 'learning_from_death' folder which has a less complicated assembly pipline. 

The second notebook is the analysis notebook. It inherits from the data preparation notebook but focuses purely on analysis. I recommend you divide these tasks during your own analytics work to prevent things becomes overly complicated / mixed. The preparation of your data should be seperate from its analysis. We have broadly followed the NHS Digital reproducible analytics pipelines in the development of this work: https://github.com/NHSDigital/rap-community-of-practice. Unit tests have not been performed as the code is meant as a template to adapt, not boilerplate deployment code. If you find any bugs in this version which was specifically re-engineered for open-source publishing please let us know.

The analytics pipeline is also fairly generic and intended to be adapted. If it proves popular we will provide some synthetic data to play with.

Please also let us know if you have any successes! You can email matt at matt@reallyusefulmodels.com.

### Clients

We have used the oracle instantclient version 11.2 for this project to keep things simple. This is a slightly older lightweight thin-client which can connect to most oracle databases. It is pretty easy to setup and install and can be obtained from the oracle website https://www.oracle.com/downloads/, however it will obviously not work if you are querying a non-oracle database in which case you will need to select and install the correct client.

### Usage

The template is there to act a guide and the SQL query wouldn't help you anyway because our PAS is unusual so we have not included the exact SQL code. You will need to speak to your local IT team to work out a SQL query that will fit your local needs - once you have the rest of the template working however this is the easy part.

### Bug Reporting 

Please report any issues on the github repo

