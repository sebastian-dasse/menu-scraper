#!/usr/bin/env python

"""
TODO: comment

"""

import re
import urllib


root_url     = "http://www.wandel-restaurant.de/"
start_path   = "restaurants/bernhard-weiss-str/wandel8/start.html"
menu_pattern = r'href="(.+/Mittagskarte-Wandel-1.+\.pdf)"'

num_week_days = 5

categories = [
  "Pasta I",
  "Wok", #
  "Essen III", #
  "Essen II -vegetarisch-", #
  "Essen I", #
  "Eintopf"
]

title_for_category = {
  "Eintopf"               : "Eintopf:      ",
  "Essen I"               : "Essen 1:      ",
  "Essen II -vegetarisch-": "Vegetarisch:  ",
  "Essen III"             : "Essen 3:      ",
  "Wok"                   : "Wok / Aktion: ",
  "Pasta I"               : "Pasta:        "
}

categories_pattern         = "|".join(categories)
category_delimiter_pattern = "\n(?=.*?" + categories_pattern + "\n)"
category_title_pattern     = "^.*?" + categories_pattern + "\n"
meal_delimiter_pattern     = "(?:^|(?<=\w))\n"


def extract_menu_path():
  url = root_url + start_path
  website = urllib.urlopen(url)
  for line in website:
    match = re.search(menu_pattern, line)
    if match:
      return root_url + match.group(1)


def menu_title(menu_path):
  match = re.search("/([^/]+?).pdf$", menu_path)
  if match:
    return match.group(1).replace("-", " ")
  return "Mittagskarte Wandel"


def extract_meals(text):
  menu = {}
  for chunk in re.split(category_delimiter_pattern, text):
    if re.match(category_title_pattern, chunk):
      title_line, meal_chunk = chunk.split("\n", 1)
      title = _normalised_title(title_line)
      
      if title in menu:
        continue
      
      meal_chunks = re.split(meal_delimiter_pattern, meal_chunk)
      missing = [""] * (len(categories) - len(meal_chunks))
      menu[title] = ([meal.replace("\n", "") for meal in meal_chunks] + missing)[:num_week_days]

  return menu


def _normalised_title(title_line):
  for category in categories:
    if category in title_line:
      return title_for_category[category]
