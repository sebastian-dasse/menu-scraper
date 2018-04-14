#!/usr/bin/env python

"""
pdf extraction from url is heavily inspired by:
https://stackoverflow.com/questions/9751197/opening-pdf-urls-with-pypdf
"""

from argparse import ArgumentParser
from urllib2 import urlopen
from StringIO import StringIO

from PyPDF2 import PdfFileReader


def extract_text(path):
  return _extract_plain_text(_read_data(path))


def _read_data(path):
  if path.startswith("http"):
    return urlopen(path).read()
  else:
    with open(path, "rb") as in_file:
      return in_file.read()


def _extract_plain_text(data):
  pdf_reader = PdfFileReader(StringIO(data))
  extracted = ""
  for num in xrange(pdf_reader.getNumPages()):
    extracted += pdf_reader.getPage(num).extractText().encode('utf-8')
  return extracted


def write_binary(path, output):
  with open(output, "wb") as out_file:
    data = _read_data(path)
    stream = StringIO(data)
    out_file.write(stream.read())


def _parse_args():
  arg_parser = ArgumentParser(description="This simple tool facilitates downloading PDF files from the web and extracting plain text from PDF files.")
  arg_parser.add_argument("path",
    help="the path to the PDF file. This may be an absolute path to a file in the filesystem or an URL to a file accessible via HHTP")
  arg_parser.add_argument("-o", dest="output",
    help="the path to write the PDF to")
  return arg_parser.parse_args()


def main():
  args = _parse_args()

  if args.output:
    write_binary(args.path, args.output)
    print "PDF file saved to " + args.output
  else:
    text = extract_text(args.path)
    print text


if __name__ == '__main__':
  main()
