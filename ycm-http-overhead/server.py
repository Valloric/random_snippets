#!/usr/bin/env python

import bottle
from bottle import post, run, request

# num bytes for the request body buffer; request.json only works if the request
# size is less than this
bottle.Request.MEMFILE_MAX = 200 * 1024

response_json = {
  'foo': 'nthoeun honeuh onteuh notehu ntoheunthoe',
  'bar': 123,
  'soo': 122343,
  'foobar': [
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
    {
      'foo': 'goo',
      'moo': 'boo',
      'dro': 1212
    },
  ]
}

@post( '/' )
def index():
  data = request.json
  print 'Received request with body size: {} KB'.format(
    request.content_length / 1024.0 )
  resp = response_json.copy()
  resp[ 'testy' ] = data[ 'testy' ]
  return resp

run( host='localhost', port=8080, server='cherrypy' )
