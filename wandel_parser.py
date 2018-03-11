#!/usr/bin/env python

"""
TODO: comment

see:
- https://docs.python.org/2/library/re.html
- https://docs.python.org/2/library/htmlparser.html

try algorithm in pseudocode (to be continued):

  find chunk matchin "^key$":
    if (startswith key and
        next line is not just key)
      for i in xrange(week_days):
        meal = ""
        while line ends with ' '
          meal += line
...

"""

import re
import urllib


root_url = "http://www.wandel-restaurant.de/"
start_path = "restaurants/bernhard-weiss-str/wandel8/start.html"
menu_pattern = r'href="(.+/Mittagskarte-Wandel-1.+\.pdf)"'

week_days = 5

categories = [
  "Pasta I",
  "Wok",
  "Essen III",
  "Essen II -vegetarisch-",
  "Essen I",
  "Eintopf"
]

title_for_category = {
  "Eintopf": "Eintopf",
  "Essen I": "Essen 1",
  "Essen II -vegetarisch-": "Vegetarisch",
  "Essen III": "Essen 3",
  "Wok": "Wok / Aktion",
  "Pasta I": "Pasta"
}

__dummy_dict = {
  "Eintopf": [
    "Eintopf - 0",
    "Eintopf - 1",
    "Eintopf - 2",
    "Eintopf - 3",
    "Eintopf - 4"
  ],
  "Essen I": [
    "Essen I - 0",
    "Essen I - 1",
    "Essen I - 2",
    "Essen I - 3",
    "Essen I - 4"
  ],
  "Essen II -vegetarisch-": [
    "Essen II -vegetarisch- - 0",
    "Essen II -vegetarisch- - 1",
    "Essen II -vegetarisch- - 2",
    "Essen II -vegetarisch- - 3",
    "Essen II -vegetarisch- - 4"
  ],
  "Essen III":  [
    "Essen III - 0",
    "Essen III - 1",
    "Essen III - 2",
    "Essen III - 3",
    "Essen III - 4"
  ],
  "Wok":  [
    "Wok - 0",
    "Wok - 1",
    "Wok - 2",
    "Wok - 3",
    "Wok - 4"
  ],
  "Pasta I":  [
    "Pasta - 0",
    "Pasta - 1",
    "Pasta - 2",
    "Pasta - 3",
    "Pasta - 4"
  ]
}


def extract_menu_path():
  url = root_url + start_path
  website = urllib.urlopen(url)

  for line in website:
    match = re.search(menu_pattern, line)
    if match:
      return root_url + match.group(1)


def joined_keys():
  return "|".join(keys)


def starts_with_key_line():
  return r"\n(?=" + joined_keys()  + ")"


def __dummy_impl(text):
  return __dummy_dict


# def __real_impl(text):
#   split = re.split(starts_with_key_line(), text)
#   for chunk in split:
#     if chunk.startswith("Eintopf"): # and len(chunk.split("\n")) > 1:
#       print "------------------"
#       print chunk
#       print 
#       print "------------------"


def extract_meals(text):
  return __dummy_impl(text)
  # return __real_impl(text)


# def main():
#   print "----------------------------------------------------------------------"
#   print
#   print
#   print "----------------------------------------------------------------------"


# if __name__ == '__main__':
#   main()
