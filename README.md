# stw2openmensa

This is a Python script that converts canteen meal data from [Studierendenwerk Münster](https://www.stw-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

~~Studierendenwerk Münster provides meal data as XML files, see [the discussion here](https://github.com/ifgi-webteam/mensaparser/issues/4#issuecomment-260331519).~~ As of August 2020 Studierendenwerk Münster no longer provides meal data in XML format (see [issue #15](https://github.com/chk1/stw2openmensa/issues/15)).

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

## Data access

As of August 2020 converted and parsed data is no longer available from OpenMensa, since Studierendenwerk Münster hast stopped providing the source XML files.

## Todo

* Better checks for when a canteen is closed for the day

## License

Code in this repository is licensed under the [MIT license](LICENSE).
