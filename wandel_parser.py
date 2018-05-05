#!/usr/bin/env python

"""
TODO: comment

"""

import re
import urllib


root_url     = "http://www.wandel-restaurant.de/"
start_path   = "restaurants/bernhard-weiss-str/wandel8/start.html"
menu_pattern = r'href="(.+/(?:Speiseplan|Mittagskarte-Wandel-1).+\.pdf)"'

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
  def is_valid(chunk):
    return re.match(category_title_pattern, chunk)

  def normalised_title(title_line):
    for category in categories:
      if category in title_line:
        return title_for_category[category]
  
  def meal_from(chunk):
    title_line, meal_chunk = chunk.split("\n", 1)
    return normalised_title(title_line), meal_chunk
  
  def description_from(meal_chunk):
    meal_chunks = re.split(meal_delimiter_pattern, meal_chunk)
    missing = [""] * (len(categories) - len(meal_chunks))
    return ([meal.replace("\n", "") for meal in meal_chunks] + missing)[:num_week_days]
  
  menu = {}
  error_count = 0
  for chunk in re.split(category_delimiter_pattern, text):
    if is_valid(chunk):
      try:
        title, meal_chunk = meal_from(chunk)
        if title in menu:
          continue
        menu[title] = description_from(meal_chunk)
      except ValueError:
        error_count += 1

  if error_count > 0:
    print "There were " + str(error_count) + " while parsing the menu"

  return menu
