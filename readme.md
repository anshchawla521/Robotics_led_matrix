# Led matrix using RPi ,ws2811 and telegram bot api

## Description

Led matrix which displays messages sent to a telegram chat bot .This is being made using python ,raspberry pi and ws2811 individually addressably led. This is a group project which is being developed by a group of students interested in robotics🙂.

## Tasks

### Overall Project

- [x] Implement the telegram bot using API
- [ ] Improve Interface for Telegram Chatbot
- [x] Define Character Map
- [ ] Displaying of string in matrix
- [ ] Scrolling of string in matrix
- [ ] linking of LED matrix to the 2D array in code

#### Ansh Chawla

- [x] Guide everyone
- [x] link files

#### Harsh Kumar

- [x] Guide everyone
- [x] Write code and design interface for telegram chat bot

#### Shubham Singla

- [x] Guide everyone
- [x] Write code and design interface for telegram chat bot

#### Ankit Rupal

- [x] Implement Character mapping for letter A , B , C , 1
- [x] Write code for compiling Character map arrays into dict

#### Sahil Ahmed

- [x] Implemented Character mapping for letter D , E , F , J , K , L , 2 , 4

#### Mayur Garg

- [x] Implement Character mapping for letter G , H , I , 3

#### Kanishk

- [x] Implemented Character mapping for letter M , N , O , 5

#### Lakshay

- [x] Implemented Character mapping for letter P , Q , R , 6

#### Rohan

- [x] Implemented Character mapping for letter S , T , U , 7

#### Mayank

- [x] Implemented Character mapping for letter V , W , X , 8

#### Saksham

- [x] Implemented Character mapping for letter Y , Z , ! , 9

&nbsp;

## Installation and getting started

To install all the neccessary requirements run the following commands

```bash
pip install -r requirements.txt
```

> Note : This way is not recommended as all libraries would be installed globally.

### Setting up the virtual environment

> Note : It is recommended to setup a virtual environment and then run the program.

```bash
py -m pip venv ./venv  #creating virtual environment
venv\Scripts\activate  #to activate the environment after creation
pip install -r requirements.txt # for installation of libraries

```

### For running the program

Run the main.py file using

```python
python main.py
```

> Note : A file by the name credentails.py must be placed inside the root directory of project. The contents of this file should be as shown below

```python
bot_token = 'Your bot token'
```
