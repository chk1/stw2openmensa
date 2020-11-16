# stw2openmensa

## Deprecation notice

From 2016 to August 2020, Studierendenwerk Münster provided meal data as XML files (see [the discussion here](https://github.com/ifgi-webteam/mensaparser/issues/4#issuecomment-260331519)) but they have since stopped. Canteen data is now only available via the "My Mensa" platform.

If want to use the canteen data in a machine readable format and are looking for an alternative, take a look at the [mymensa2openmensa](https://gitlab.com/BBurke/mymensa2openmensa) project (see [issue #15](https://github.com/chk1/stw2openmensa/issues/15)).

## About

stw2openmensa is a Python script that converts canteen meal data from [Studierendenwerk Münster](https://www.stw-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

## Installation

### Configuration

[`config.py`](config.py) contains a few settings that you can change, the most important being `output_dir` where the output data will be written to.

### Quick start

Install dependencies and run the script.

```
pip install -r requirements.txt
python parser.py
```

### Using virtualenv

Prepare your virtual environment:
```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

Activate your virtual environment and run the parser:
```
source venv/bin/activate
python parser.py
deactivate
```

Cronjob example using `virtualenv`:

Executes monday through saturday at 07:00

```
0 7 * * 1-6 /home/you/mensaparser/venv/bin/python /home/you/mensaparser/parser.py
```

## Todo

* Better checks for when a canteen is closed for the day (see issue #4)

## License

Code in this repository is licensed under the [MIT license](LICENSE).
