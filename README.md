# menu-scraper

Still work in progress.

## Open tasks
- [x] scrape pdf url from website
- [x] read pdf from url
- [x] parse wandel menu
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
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/). The preferred way to do this is through *pip*, which comes with your Python installation: `[sudo] pip install virtualenv`.
3. Create a virtualenv: `virtualenv ~/my_env`.
4. Activate *my_env*: `source ~/my_env/Scripts/activate`.
5. To ensure that *my_env* was indeed activated you can check, that the Python version from within your virtualenv is chosen: `which python`.
6. Install PyPDF2 inside your virtualenv: `pip install PyPDF2`.
7. To ensure that PyPDF2 was sucessfully installed check the output of: `pip list`.
8. To run the menu-scraper you have the following options:
  a. Run `./menu_scraper.py` to print the menu of the current week to console..
  b. Run `./menu_scraper.py -d` to print the menu of today to console.
  b. Run `./menu_scraper.py -d <weekday>` to print the menu of the specified weekday to console, where `<weekday>` is in a number in [0,4].
9. Should you just want to use the PDF extraction functionality, you are free to use pdfextract seperately. Running `pdfextract -h` will show its usage.
10. To deactivate *my_env* when you are done: `deactivate`.
