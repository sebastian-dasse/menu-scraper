#!/usr/bin/env python

"""
TODO: comment
"""

from argparse import ArgumentParser
from datetime import datetime
import json
import os
import tempfile

import pdfextract
import wandel_parser as menu_parser


week_days = [
  "Montag",
  "Dienstag",
  "Mittwoch",
  "Donnerstag",
  "Freitag",
]
num_week_days = len(week_days)

output_file_path = os.path.join(tempfile.gettempdir(), "wandel_menu.json")


def menu_path():
  return menu_parser.extract_menu_path()


def menu_title(menu_path):
  return menu_parser.menu_title(menu_path)


def extract_text(menu_path):
  return pdfextract.extract_text(menu_path)


def extract_meals(path):
  text = extract_text(path)
  return menu_parser.extract_meals(text)


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


def print_meals(meals_by_category):
  for day in xrange(num_week_days):
    print_day_s_meals(day, meals_by_category)


def print_week_s_menu():
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_meals(meals_by_category)


def print_weekday_s_menu(day):
  title, meals_by_category = fetch_menu()
  print_title(title)
  print_day_s_meals(day, meals_by_category)


def today():
  return int(datetime.now().strftime("%w")) - 1

def write_menu_to_temp():
  title, meals_by_category = fetch_menu()
  with open(output_file_path, "w") as out_file:
    json.dump({
      "title": title,
      "menu":  meals_by_category
    }, out_file, indent=2, separators=(',', ': '))

def parse_args():
  arg_parser = ArgumentParser(description="TODO.")
  group = arg_parser.add_mutually_exclusive_group()
  group.add_argument("-d", dest="day", type=int, nargs="?",
    const=-1, default=num_week_days, action="store",
    help="only print the menu of the given day, where 0 indicates Monday and no value means today")
  group.add_argument("-w", dest="write", action="store_true",
    help="write the current week's menu into a json file inside the default temp directory")
  return arg_parser.parse_args()


def main():
  args = parse_args()
  day = today() if args.day < 0 else args.day
  
  if args.write:
    write_menu_to_temp()
  elif 0 <= day < num_week_days:
    print_weekday_s_menu(day)
  else:
    print_week_s_menu()


if __name__ == '__main__':
  main()
