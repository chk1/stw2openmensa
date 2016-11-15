# Studentenwerk Münster To OpenMensa

Convert canteen meal data from Studentenwerk Münster XML to OpenMensa Feed v2 XML format

## Config

Change the output directory in parser.py line 82 if you want, goes to `./out/` by default.

## Install dependencies and Run

Quick start:

```
pip install beautifulsoup4 lxml
python parser.py
```

With virtualenv:

```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install beautifulsoup4 lxml
python parser.py
deactivate
```

Cronjob ([see here](http://stackoverflow.com/a/3287063/1781026)):

```
0 0 * * * * /home/you/mensaparser/venv/bin/python /home/you/mensaparser/parser.py
```