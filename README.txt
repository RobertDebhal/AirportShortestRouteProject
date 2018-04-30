Airports12751005
================

This is a candidate solution for the term project of COMP20230. Credit to Khalil Muhammad for the README template.

Prerequisites
----------------------

This project was created in a Python 3.6 environment. It will be easier to set up the project if you install [Anaconda](https://conda.io/docs/user-guide/install/download.html) or [Miniconda](https://conda.io/miniconda.html). Other options, such as [PyEnv](https://github.com/pyenv/pyenv) and classic virtual environment (i.e. `venv`), will also work.


Installation and Setup
----------------------

Run the following commands in Terminal:

```
git clone https://github.com/RobertDebhal/AirportShortestRouteProject.git && cd AirportShortestRouteProject
conda create -n environment
source activate environment
pip install -r requirements.txt
```

Running the Program
-------------------

From the project directory (in Terminal), run this command

python main.py

You will be prompted to enter the path to an itinerary file. The correct path must be specified and the file mustbe in the format specified below.
Format: The file should be a csv with 6 columns of data, the first five columns should be valid three letter airport codes which can be found in input/airport.csv and the last column shoul be an aircraft code which can be found in input/aircraft.csv 

Running the Tests
------------------

From the project directory (in Terminal), run this command

python -m unittest discover

