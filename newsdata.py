#!/usr/bin/env python3
import psycopg2
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis</title>
    <style>
      h1, form { text-align: center; }
    </style>
  </head>
  <body>
    <h1>Log Analysis</h1>
    <!-- post content will go here -->
%s
%s
%s
  </body>
</html>
'''

# HTML template for an individual comment
summary = '''\
    <div>%s - %s %s</div>
'''

# queries for database
top_articles = "select articles.title, count(*) as num " \
               "from log_ok left join articles " \
               "on articles.slug = log_ok.path_sliced " \
               "group by articles.title order by num desc limit 3"
top_authors = "select name, count(*) as num from (select n1.name, n1.title " \
              "from log_ok inner " \
              "join LATERAL (select authors.name, articles.title," \
              " articles.slug from articles " \
              "join authors on authors.id = articles.author)" \
              " as n1 on n1.slug = log_ok.path_sliced) as author_num  " \
              "group by name order by num desc"
errors = "select error.date, " \
         "round((error.num_of_error::float/total.num::float*100)::numeric, " \
         "2) as percent " \
         "from (select date(time) as date, count(*) " \
         "as num_of_error from log " \
         "where status !='200 OK' group by date) as error " \
         "join (select date(time) as date," \
         " count(*) as num from log group by date) " \
         "as total on error.date = total.date " \
         "where " \
         "round((error.num_of_error::float" \
         "/total.num::float*100)::numeric, 2) > 1"

# database name
DBNAME = "news"


def get_results(query):
    '''Return the results based on query(input) from database.'''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_results(query, title, unit):
    '''Return the post combined by
    the results from query, title, and the proper unit.'''
    if query == top_articles:
        post = "".join(summary % (("\"%s\"" % (key[0])), key[1], unit)
                       for key in get_results(query))
    else:
        post = "".join(summary % (key[0], key[1], unit)
                       for key in get_results(query))
    results = '<strong>' + title + '</strong>' + post + '<br>'

    return results


@app.route('/', methods=['GET'])
def main():
    '''Post the results requested all together.'''
    html = HTML_WRAP % (print_results(top_articles,
                                      'The most popular three '
                                      'articles of all time:',
                                      'views'),
                        print_results(top_authors,
                                      'The most popular authors of all time:',
                                      'views'),
                        print_results(errors,
                                      'The days with more than 1% '
                                      'of requests lead to errors:',
                                      '%'))
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
