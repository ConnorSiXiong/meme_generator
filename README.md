# Meme Generator

The goal of this project is to build a "meme generator".

A multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. You could manually copy and paste these quotes into one standard format.

# Installation

Install the libraries via ```pip install -r requirements.txt```

```
charset-normalizer==2.0.9
click==8.0.3
Flask==2.0.2
idna==3.3
Jinja2==3.0.3
lxml==4.7.1
MarkupSafe==2.0.1
numpy==1.21.5
pandas==1.3.5
Pillow==8.4.0
python-docx==0.8.11
pytz==2021.3
requests==2.26.0
six==1.16.0
urllib3==1.26.7
Werkzeug==2.0.2

```

# How to start it?
## 1. Web App
```python app.py```
This will be deployed on AWS later.

## 2. Command Line
```
usage: python meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

optional arguments:
  -h, --help       show this help message and exit
  --body BODY      The text of the quote
  --author AUTHOR  The author of the quote
  --path PATH      The path for saving the meme generated.
```

# What is the app looks like?
<img src="https://github.com/AlexSiXiong/udacity_intermediate_python_nanodegree2/blob/main/dog_demo.gif" width="800" height="800">
