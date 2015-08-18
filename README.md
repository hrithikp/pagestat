#PageStat

An application that reports on tag usage statistics for web pages

##Installation

To install and manage package data manually:

```
$ python setup.py install
```

Installing and managing package via make:

```
$ make install # Installs the package
$ make clean # Uninstalls the package
```

##Running Tests
Using make:

```
$ make test # clean + install + test
```

Using setup.py:

```
$ python setup.py test
```

##Usage

```
$ pagestat --help
usage: pagestat [-h] [--show-top SHOW_TOP] [--stat-type {tags,attrs}] url

positional arguments:
  url                   URL to read for generating stats

optional arguments:
  -h, --help            show this help message and exit
  --show-top SHOW_TOP   Number of top items to show
  --stat-type {tags,attrs}
                        Item type to use for gathering stats
```

Sample output from a valid run

```
$ pagestat http://www.google.com
Total names: 20
Total count: 207

Rank: 1
Name: div
Count: 56
Ratio: 0.27

Rank: 2
Name: span
Count: 49
Ratio: 0.24

Rank: 3
Name: a
Count: 39
Ratio: 0.19

Rank: 4
Name: li
Count: 19
Ratio: 0.09

Rank: 5
Name: script
Count: 11
Ratio: 0.05
```


