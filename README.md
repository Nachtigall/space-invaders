## Space invader detector
Hello! This is simple Python script to detect possible invaders from radar input. It can
be used as is. No additional tuning is required.

### Pre-requisites:
1. Invader templates should be defined in `./invader_samples/default_invaders.txt` file.
For now, just `~~~~` is accepted as separator between invader bodies.
   
2. Radar data should be defined in `./radar_sample.sample.txt`.
3. By default, max chars difference is set to `2`. This means, that invaders are detected with probability of 75 %.
You can set `CHARS_DIFFERENCE` in `main.py` to `0`. In such case - only exact matches will be found.

### Dependencies management:
Requirements are managed by `pipenv` ([more about pipenv](https://github.com/pypa/pipenv)) 
and defined in `Pipfile`. 

### Running:
0. `pip install pipenv` (if pipenv is not installed yet)
1. `pipenv shell` - to activate your virtual pipenv
2. `python main.py` - to run scanner

### Testing:
0. `pipenv shell` - to activate your virtual pipenv
1. `python -m unittest` - to run tests

### Contributing:
Can be done via Pull Requests.

### Possible future enhancement:
1. CLI utility to accept filenames, max chars difference.
2. Acceptance of any other file separator, not only `~~~~`
3. Logging into specified file
4. etc