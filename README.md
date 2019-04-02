# stw2openmensa

This is a Python script that converts canteen meal data from [Studierendenwerk Münster](https://www.stw-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

Studierendenwerk Münster provides meal data as XML files, see [the discussion here](https://github.com/ifgi-webteam/mensaparser/issues/4#issuecomment-260331519).

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

### OpenMensa Feed v2 XML format

Revised and parsed XML data for OpenMensa is available from [mensa.chrk.de/openmensa](https://mensa.chrk.de/openmensa).

I configured OpenMensa sources for Münster's canteens already, you can see [a map of canteens here](http://openmensa.org/#14/51.9646/7.6159). Data is parsed and updated daily.

### JSON format

JSON data is available from the [OpenMensa API](http://doc.openmensa.org/api/v2/) via e.g. `http://openmensa.org/api/v2/canteens/225/meals`.

ID `225` represents "Mensa am Ring", you can use these other IDs as well:

|OpenMensa ID | Link to OpenMensa Website            |
|-------------|--------------------------------------|
|`325`        | ~~[Bistro Coerdehof][325]~~ ([geschlossen](https://github.com/chk1/stw2openmensa/issues/2)) |
|`227`        | [Bistro Denkpause][227]              |
|`326`        | [Bistro Durchblick][326]             |
|`327`        | [Bistro Frieden][327]                |
|`872`        | [Bistro Friesenring][872]            |
|`328`        | ~~[Bistro Hüfferstift][328]~~ ([geschlossen](https://github.com/chk1/stw2openmensa/issues/2)) |
|`329`        | [Bistro KaBu][329]                   |
|`330`        | [Bistro Katholische Hochschule][330] |
|`331`        | [Bistro Oeconomicum][331]            |
|`226`        | [Mensa am Aasee][226]                |
|`225`        | [Mensa am Ring][225]                 |
|`233`        | [Mensa Bispinghof][233]              |
|`228`        | [Mensa da Vinci][228]                |
|`332`        | [Mensa Steinfurt][332]               |


[325]: https://openmensa.org/c/325
[227]: https://openmensa.org/c/227
[326]: https://openmensa.org/c/326
[327]: https://openmensa.org/c/327
[328]: https://openmensa.org/c/328
[329]: https://openmensa.org/c/329
[330]: https://openmensa.org/c/330
[331]: https://openmensa.org/c/331
[226]: https://openmensa.org/c/226
[225]: https://openmensa.org/c/225
[233]: https://openmensa.org/c/233
[228]: https://openmensa.org/c/228
[332]: https://openmensa.org/c/332
[872]: https://openmensa.org/c/872

## Todo

* Better checks for when a canteen is closed for the day

## License

Code in this repository is licensed under the [MIT license](LICENSE).
