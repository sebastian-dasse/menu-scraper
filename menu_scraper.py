#!/usr/bin/env python

"""
TODO: comment
"""

from argparse import ArgumentParser
from datetime import datetime

import pdfextract
import wandel_parser as parser


week_days = [
  "Montag",
  "Dienstag",
  "Mittwoch",
  "Donnerstag",
  "Freitag",
]
num_week_days = len(week_days)


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
  for day in xrange(num_week_days):
    print_day_s_meals(day, meals_by_category)


def print_week_s_menu():
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_meals(title, meals_by_category)


def print_weekday_s_menu(day):
  day = int(day) % num_week_days
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_day_s_meals(day, meals_by_category)


def today():
  return int(datetime.now().strftime("%w")) - 1


def _parse_args():
  parser = ArgumentParser(description="TODO.")
  parser.add_argument("-d", dest="day", type=int, nargs="?",
    const=-1, default=num_week_days, action="store",
    help="only print the menu of the given day, where 0 indicates Monday and no value means today")
  return parser.parse_args()


def main():
  args = _parse_args()
  
  if      args.day < 0:
    print_weekday_s_menu(today())
  elif args.day < num_week_days:
    print_weekday_s_menu(args.day)
  else:
    print_week_s_menu()


if __name__ == '__main__':
  main()
