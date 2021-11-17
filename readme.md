# Led matrix using RPi ,ws2811 and telegram bot api

> A file by the name credentails.py must be placed inside the root directory of project. The contents of this file should be `bot_token = 'Your bot token'`

## Installation and getting started

To install all the neccessary requirements run the following commands

```
pip install -r requirements.txt
```

## Setting up the virtual environment

> Note : It is recommended to setup a virtual environment and then run the program

```
py -m pip venv ./venv  #creating virtual environment
venv\Scripts\activate  #to activate the environment after creation
pip install -r requirements.txt # for installation of libraries

```

## For running the program

Run the main.py file using

```
python main.py
```

## Tasks-

- [x] Implement the telegram bot using API
- [ ] Define Character Map
- [ ] Displaying of string in matrix
- [ ] Scrolling of string in matrix
- [ ] linking of LED matrix to the 2D array in code
