#!/usr/bin/env python

"""
TODO: comment
"""

import pdfextract
import wandel_parser as parser
from datetime import datetime


week_days = [
  "Montag",
  "Dienstag",
  "Mittwoch",
  "Donnerstag",
  "Freitag",
]


__sample_path = "D:/Downloads/Mittagskarte-Wandel-1-KW-10.pdf"
__sample_url = "http://www.wandel-restaurant.de/media/downloads/Mittagskarte-Wandel-1-KW-10.pdf"


def __read_dummy_menu():
  text = ""
  with open("dummy_menu.txt", "r") as text_file:
    for line in text_file:
      text += line
  return text


def menu_path():
  # return __sample_path
  # return __sample_url
  return parser.extract_menu_path()


def menu_title(menu_path):
  return parser.menu_title(menu_path)


def extract_text(menu_path):
  return pdfextract.extract_text(menu_path)


def extract_meals(path):
  text = extract_text(path)
  return parser.extract_meals(text)


def fetch_menu():
  path = menu_path()
  title = menu_title(path)
  meals_by_category = extract_meals(path)
  return (title, meals_by_category)


def print_title(title):
  print "+-" + "-" * len(title) + "-+"
  print "| " + title + " |"
  print "+-" + "-" * len(title) + "-+"
  print


def print_week_day(day):
  day_name = week_days[day]
  print "--[ " + day_name + " ]----------------------"
  print "   --" + "-" * len(day_name)


def print_day_s_meals(day, meals_by_category):
  print_week_day(day)
  for category, meals in meals_by_category.iteritems():
    print category + " " + str(meals[day])
  print


def print_meals(title, meals_by_category):
  for day in xrange(len(week_days)):
    print_day_s_meals(day, meals_by_category)


def print_week_s_menu():
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_meals(title, meals_by_category)


def print_today_s_menu():
  day = int(datetime.now().strftime("%w")) - 1
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_day_s_meals(day, meals_by_category)


def main():
  import sys
  if len(sys.argv) > 1 and sys.argv[1] == "-d":
    print_today_s_menu()
  else:
    print_week_s_menu()


if __name__ == '__main__':
  main()
