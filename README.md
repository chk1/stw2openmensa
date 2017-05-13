# stw2openmensa

A Python script that converts canteen meal data from [Studierendenwerk Münster](http://studentenwerk-muenster.de/) XML to [OpenMensa Feed v2](http://doc.openmensa.org/feed/v2/) XML format.

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

Cronjob example using `virtualenv`:

```
0 7 * * 1-6 /home/you/mensaparser/venv/bin/python /home/you/mensaparser/parser.py
```

## Data access

Original meal data is available from Studierendenwerk Münster as XML, see [the discussion here](https://github.com/ifgi-webteam/mensaparser/issues/4#issuecomment-260331519).

Revised and parsed XML data for OpenMensa is available from [mensa.chrk.de/openmensa](https://mensa.chrk.de/openmensa). This is where I configured my OpenMensa sources to fetch canteen data from ([see map of canteens](http://openmensa.org/#14/51.9646/7.6159)). Data is parsed and updated daily.

JSON data is available from the OpenMensa API via `http://openmensa.org/api/v2/canteens/225/meals`.

ID `225` represents "Mensa am Ring", you can use these other IDs as well:

```
325 Bistro Coerdehof
227 Bistro Denkpause
326 Bistro Durchblick
327 Bistro Frieden
328 Bistro Hüfferstift
329 Bistro KaBu
330 Bistro Katholische Hochschule
331 Bistro Oeconomicum
226 Mensa am Aasee
225 Mensa am Ring
233 Mensa Bispinghof
228 Mensa da Vinci
332 Mensa Steinfurt
```

## Todo

Check how canteen data looks when a canteen is closed and add necessary XML attributes.

## License

MIT