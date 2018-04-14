# menu-scraper

Still work in progress.

## Open tasks
- [x] scrape pdf url from website
- [x] read pdf from url
- [x] parse wandel menu
- [x] code cleanup
- [ ] add csv option
- [ ] complete documentation

## Prerequisites

### mandatory
- Python 2
- PyPDF2

### recommended
- virtualenv

## Installation

It is recommended to install PyPDF2 inside a virtualenv, to keep your system setup nice and tidy. However, if you don't care to mess up your system -- feel free to skip all steps related to virtualenv.

To install on Windows do the following:

1. Install the latest [Python 2](https://www.python.org/download/).
2. Open the git bash.
3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/). The preferred way to do this is through *pip*, which comes with your Python installation: `[sudo] pip install virtualenv`.
4. Create a virtualenv: `virtualenv ~/my_env`.
5. Activate *my_env*: `source ~/my_env/Scripts/activate`.
6. To ensure that *my_env* was indeed activated you can check, that the Python version from within your virtualenv is chosen: `which python`.
7. Install PyPDF2 inside your virtualenv: `pip install PyPDF2`.
8. To ensure that PyPDF2 was sucessfully installed check the output of: `pip list`.
9. To run the menu-scraper you have the following options:
    1. Run `./menu_scraper.py` to print the menu of the current week to console..
    2. Run `./menu_scraper.py -d` to print the menu of today to console.
    3. Run `./menu_scraper.py -d <weekday>` to print the menu of the specified weekday to console, where `<weekday>` is in a number in [0,4].
10. Should you just want to use the PDF extraction functionality, you are free to use pdfextract seperately. Running `./pdfextract.py -h` will show its usage.
11. To deactivate *my_env* when you are done: `deactivate`.
