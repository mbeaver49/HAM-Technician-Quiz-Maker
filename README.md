# QuizMaker
This application is meant to generate quizzes for studying the HAM Technician exam with the provided question pool of 2018-2022 provided by AARL. There are practice exams avaiable to take through AARL and other sources, but for the purpose of cramming this could be a great alternative. It goes through every problem sequentially in order to make sure there isn't a question left out by a random question selector. 


## Requirements
This application is setup for development use right now, so running it will need Python3 to be installed along with the Pipenv Beautiful Soup package.

- [Python3.7](https://www.python.org/downloads/release/python-370/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [bs4](https://pypi.org/project/beautifulsoup4/)


## Setup & Installation
Navigate to the src folder, venv, and install bs4.

```shell

cd src

pip3 install pipenv

pipenv shell

pipenv install bs4
```

## Run in Python3.7
```shell
python3 Question_Maker.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Undecided
