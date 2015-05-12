Stream of conciousness thoughts here...

We probably want to do the following:
- read domain.csv into object(s)
- read student.csv into objects
- generate a path for a particular student, given a domain ordering
(Path might be worth being it's own object?)
- unit tests
- standard python packaging stuff
- PEP8 linting

from http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
Project/
|-- bin/
|   |-- project
|
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- setup.py
|-- README


To run unit tests:
pip install -r test_requirements.txt
nosetests
