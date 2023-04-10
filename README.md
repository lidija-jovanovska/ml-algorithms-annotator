# Data Mining and Machine Learning Algorithm Annotator

<!--
```
cd existing_repo
git remote add origin https://gitlab.com/lickywilde/msc.git
git branch -M main
git push -uf origin main
```-->

## Description

The ML Algorithms Annotator is a Django application which enables users to annotate and query ML algorithms. The algorithms information is based on an annotation schema and it includes entities like "Document", "Optimization Problem", "Complexity", etc. Additionally, the user can query the graph database containing multiple PoC algorithms like Linear Regreession, SVC, KNN, etc.

The entire development process is documented in my Masters thesis: https://drive.google.com/file/d/1vyV6YlN47wOhkFUvjNq_JC63hnleZo9y/view?usp=sharing


## Badges
TBD - setuptools, unittest

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

<!---

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
-->
