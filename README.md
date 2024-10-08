## Purpose
This is a Desktop Client skeleton app.

## Project structure

```
DesktopClient/
│
├── app/
│   ├── __init__.py
│   ├── chat.py         # Main chat app file
│   ├── config.json     # set API URL and GPT thread ID here
│
├── .gitignore          # Add filenames you do not want to be added to your repository here
├── requirements.txt    # Dependencies
└── README.md           # The file you are reading right now :)
```

## Project setup
### install Python
[https://www.python.org/downloads/](https://www.python.org/downloads/])

### Check Python version, it should be 3.1x
`python3 --version`

### Get the code from GitHub repository
Refer to the instructions here: [https://github.com/ingus-t/rtu-web-service](https://github.com/ingus-t/rtu-web-service)

### Create environment
`python3 -m venv [environment_name]`

### Activate environment
Linux:  
`source [environment_name]/bin/activate`

Windows:  
`[environment_name]\Scripts\activate`

### install dependencies
`pip install -r requirements.txt`  
or  
`python -m pip install -r requirements.txt`

### Start the app
`python app/chat.py`  
or  
`python3 app/chat.py`

## Ideas:
You could use [https://github.com/ParthJadhav/Tkinter-Designer](https://github.com/ParthJadhav/Tkinter-Designer) to first design a very user friendly UI, and then use it for your app.  
You could also use a different framework for building your Destktop app entirely, for example:
* PyQt / PySide (Python bindings for the Qt framework)
* Kivy
* PyGame (intended for game development)
* etc.