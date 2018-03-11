#!/usr/bin/env python

"""
TODO: comment
"""

import pdfextract
import wandel_parser as parser


week_days = 5


__sample_path = "D:/Downloads/Mittagskarte-Wandel-1-KW-10.pdf"
__sample_url = "http://www.wandel-restaurant.de/media/downloads/Mittagskarte-Wandel-1-KW-10.pdf"


def __read_dummy_menu():
  text = ""
  with open("dummy_menu.txt", "r") as text_file:
    for line in text_file:
      text += line
  return text


def menu_path():
  return __sample_path
  # return __sample_url
  # return parser.extract_menu_path()

def extract_text():
  return "dummy text"
  # return __read_dummy_menu()
  # return pdfextract.extract_text(menu_path())


def extract_meals(text):
  return parser.extract_meals(text)


def print_meals(meals_by_category):
  for day in xrange(week_days):
    for category, meals in meals_by_category.iteritems():
      print category + ": " + str(meals[day])
    print


def print_menu():
  text = extract_text()
  meals_by_category = extract_meals(text)
  print_meals(meals_by_category)


def main():
  print "----------------------------------------------------------------------"
  print

  print_menu()

  print
  print "----------------------------------------------------------------------"


if __name__ == '__main__':
  main()
