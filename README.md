# stw2openmensa

A Python script that converts canteen meal data from [Studentenwerk Münster](http://studentenwerk-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

## Configuration

[`config.py`](config.py) contains a few settings that you can change, the most important being `output_dir` where the output data will be written to. Make sure this folder exists before executing the script.

## Installation

### Quick start

Install dependencies and run the script.

```
pip install beautifulsoup4 lxml
python parser.py
```

### Using virtualenv

```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install beautifulsoup4 lxml
python parser.py
deactivate
```

Cronjob example:

```
0 7 * * 1-6 /home/you/mensaparser/venv/bin/python /home/you/mensaparser/parser.py
```

## Todo

Check how canteen data looks when a canteen is closed and add necessary XML attributes.