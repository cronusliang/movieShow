#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import requests
from media import Subject, Movie


# 获取最近上映的电影
def get_theaters():
    subjects = []
    theaters_url = 'https://api.douban.com/v2/movie/in_theaters'
    param  = {'apikey':'0b2bdeda43b5688921839c8ecb20399b',
              'city':'%E5%8C%97%E4%BA%AC',
              'start':'0',
              'count':'15',
              'client':'',
              'udid':''}

    r = requests.get(theaters_url, params = param)
    if r.status_code == requests.codes.ok:
        print r.content
        data = json.loads(r.content)
        print data['subjects']
        for d in data['subjects']:
            print d['id'] + ' -- '+ d['title'] +" -- "+d['alt'] + " -- "+d['images']['large']
            subjects.append(Subject(d['id'],d['title'],d['alt'],d['images']['large']))
    return  subjects


# 获取具体电影的资源
def get_movie(id):
    subject_url = 'http://api.douban.com/v2/movie/subject/'+id
    param = {'apikey':'0b2bdeda43b5688921839c8ecb20399b',
             'city':'%E5%8C%97%E4%BA%AC',
             'client':'',
             'udid':''}
    r = requests.get(subject_url,params=param)
    if r.status_code == requests.codes.ok:
       data = json.loads(r.content)
       return Movie(data['title'], data['original_title'], data['summary'], data['images']['large'], data['trailer_urls'][0])

# 获取最近上映的电影资源 return list
def get_movies():
  movies = []
  subjects = get_theaters()
  for subject in subjects:
      movies.append(get_movie(subject.id))
  return movies