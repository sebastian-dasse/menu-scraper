#!/usr/bin/env python

"""
TODO: comment
"""

import pdfextract
import wandel_parser as parser


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


def extract_meals(text):
  return parser.extract_meals(text)


def print_meals(title, meals_by_category):
  print "+-" + "-" * len(title) + "-+"
  print "| " + title + " |"
  print "+-" + "-" * len(title) + "-+"
  print
  for num, day in enumerate(week_days):
    print "--[ " + day + " ]----------------------"
    print "   --" + "-" * len(day)
    for category, meals in meals_by_category.iteritems():
      print category + " " + str(meals[num])
    print


def print_menu():
  path = menu_path()
  title = menu_title(path)
  text = extract_text(path)
  meals_by_category = extract_meals(text)
  print_meals(title, meals_by_category)


def main():
  print_menu()


if __name__ == '__main__':
  main()
