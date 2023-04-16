# Data Mining and Machine Learning Algorithm Annotator

## Overview

The ML Algorithms Annotator is a Django application which enables users to annotate and query ML algorithms. The algorithms information is based on an annotation schema and it includes entities like "Document", "Optimization Problem", "Complexity", etc. Additionally, the user can query the graph database containing multiple PoC algorithms like Linear Regreession, SVC, KNN, etc.

The development process is described in detail in my [MSc thesis](https://drive.google.com/file/d/1vyV6YlN47wOhkFUvjNq_JC63hnleZo9y/view?usp=sharing).


## Installation

### Python dependencies

1. Install with conda (using environment.yml) - TBD  
`conda env create -f environment.yml`
2. Install with conda (using requirements.txt)  
`conda create --name <env_name> --file requirements.txt`  
`conda activate <env_name>`  
3. Install with venv  
`python3 -m venv env_name`  
`source ee/bin/activate`  
`python3 -m pip install -r requirements.txt`  
4. Install package - TBD  
`pip install .`

### Node dependencies

1. Install [node.js](https://nodejs.org/en/)
2. cd into the frontend folder  
`cd web-annotator/controller/frontend`
3. Install npm  
`npm install -g npm`
4. Install dependencies  
`npm i`
5. Compile the front-end  
`npm run build` - production  
`npm run dev` - development

### Neo4j setup - TBD

### Run the application
1. cd to the controller folder  
`cd web-annotator/controller`
2. Run the server  
`python manage.py runserver`

## Support
lidija.jovanovska@outlook.com
