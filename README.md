# stw2openmensa

A Python script that converts canteen meal data from [Studierendenwerk Münster](http://studentenwerk-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

## Configuration

[`config.py`](config.py) contains a few settings that you can change, the most important being `output_dir` where the output data will be written to. Make sure this folder exists before executing the script.

## Installation

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

Original meal data is available from Studierendenwerk Münster as XML, see [the discussion here](https://github.com/ifgi-webteam/mensaparser/issues/4#issuecomment-260331519).

Revised and parsed XML data for OpenMensa is available from [mensa.chrk.de/openmensa](https://mensa.chrk.de/openmensa). This is where I configured my OpenMensa sources to fetch canteen data from ([see map of canteens](http://openmensa.org/#14/51.9646/7.6159)). Data is parsed and updated daily.

JSON data is available from the [OpenMensa API](http://doc.openmensa.org/api/v2/) via e.g. `http://openmensa.org/api/v2/canteens/225/meals`.

ID `225` represents "Mensa am Ring", you can use these other IDs as well:

|OpenMensa ID | Link to OpenMensa Website            |
|-------------|--------------------------------------|
|`325`        | [Bistro Coerdehof][325]              |
|`227`        | [Bistro Denkpause][227]              |
|`326`        | [Bistro Durchblick][326]             |
|`327`        | [Bistro Frieden][327]                |
|`328`        | [Bistro Hüfferstift][328]            |
|`329`        | [Bistro KaBu][329]                   |
|`330`        | [Bistro Katholische Hochschule][330] |
|`331`        | [Bistro Oeconomicum][331]            |
|`226`        | [Mensa am Aasee][226]                |
|`225`        | [Mensa am Ring][225]                 |
|`233`        | [Mensa Bispinghof][233]              |
|`228`        | [Mensa da Vinci][228]                |
|`332`        | [Mensa Steinfurt][332]               |


[325]: http://openmensa.org/c/325
[227]: http://openmensa.org/c/227
[326]: http://openmensa.org/c/326
[327]: http://openmensa.org/c/327
[328]: http://openmensa.org/c/328
[329]: http://openmensa.org/c/329
[330]: http://openmensa.org/c/330
[331]: http://openmensa.org/c/331
[226]: http://openmensa.org/c/226
[225]: http://openmensa.org/c/225
[233]: http://openmensa.org/c/233
[228]: http://openmensa.org/c/228
[332]: http://openmensa.org/c/332

## Todo

* Check how canteen data looks when a canteen is closed and add necessary XML attributes.
* Better error handling
* Statistics maybe

## License

MIT