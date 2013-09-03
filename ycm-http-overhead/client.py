#!/usr/bin/env python

import requests
import json
import random
import string
from pandas import Series

url = "http://localhost:8080"
base_json = {
  'testy': 'foo',
  'line': 13,
  'column': 55,
  'foozy': 'notheusn oeunthoe nuthonu thonstueh sotnheunth'
}

headers = {
  'Content-type': 'application/json',
  'Accept': 'text/plain'
}

setup_code = '''
from __main__ import TalkToServer, GenerateTestJson
test_data = GenerateTestJson()
'''

num_runs = 50
iters_per_run = 10
num_test_bytes = 100 * 1024
num_test_files = 4

def TalkToServer(req_json):
  r = requests.post( url, data=json.dumps( req_json ), headers=headers )
  # Parse the json and then drop it on the floor. No, this won't get optimized
  # away; remember, this is Python, not C++.
  r.json()


def GenerateTestJson():
  test_data = base_json.copy()
  for i in xrange( num_test_files ):
    data = ''.join( random.choice( string.hexdigits ) for n in xrange(
      num_test_bytes / num_test_files ) )
    test_data[ 'file{}'.format( i ) ] = data
  return test_data


def Main():
  # 'stats' is an array of num_runs floats representing num seconds it took to
  # run the test code iters_per_run times. 'setup_code' code is run once per num_run
  # and is not timed.
  stats = timeit.Timer( 'TalkToServer(test_data)', setup=setup_code ).repeat(
    num_runs, iters_per_run )

  # Multiplying by 1000 to get milliseconds instead of seconds
  true_stats_in_ms = [ ( stat / iters_per_run ) * 1000 for stat in stats ]

  print "All times in milliseconds"
  print Series( true_stats_in_ms ).describe()

if __name__ == '__main__':
  import timeit
  Main()
