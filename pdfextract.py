#!/usr/bin/env python

"""
pdf extraction from url is heavily inspired by:
https://stackoverflow.com/questions/9751197/opening-pdf-urls-with-pypdf
"""

from argparse import ArgumentParser
from urllib2 import Request, urlopen
from StringIO import StringIO

from PyPDF2 import PdfFileReader


def extract_text(path):
  if path.startswith("http"):
    return __extract_from_stream(StringIO(urlopen(Request(path)).read()))
  else:
    return __extract_from_stream(path)


def __extract_from_stream(stream):
  pdf_reader = PdfFileReader(stream)
  extracted = ""
  for num in xrange(pdf_reader.getNumPages()):
    extracted += pdf_reader.getPage(num).extractText().encode('utf-8')
  return extracted


def main():
  parser = ArgumentParser(description="This simple tool extracts plain text from PDF files.")
  parser.add_argument("path",
    help="the path to the PDF file. This may be an absolute path to a file in the filesystem or an URL to a file accessible via HHTP.")
  args = parser.parse_args()

  text = extract_text(args.path)
  print text


if __name__ == '__main__':
  main()
