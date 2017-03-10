#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template
import sqlite3


# Simple welcome to the project
@route('/project/welcome/<name>')
def hello(name):
    return template('<h1>Hello {{name}}!</h1>', name=name)


# Who is the project engineer to celebrate and for how long?
@route('/project/celebrate/<period:re:(day|week|month|year)>/<name>')
def projectEngineerCelebration(period, name):
    return template(
        '<h1>Project Engineer of the {{period.title()}} \
        is {{name.title()}}</h1>',
        name=name, period=period)


# Who is the project engineer to celebrate and for how long?
# - Using a template file!
@route('/project/celebrate/v2/<period:re:(day|week|month|year)>/<name>')
def projectEngineerCelebtrationTemplate(period, name):
    return template(
        'project_template',
        name=name, period=period)


# Show me some JSON
@route('/project/json/example')
def returnJson():
    from bottle import response
    from json import dumps

    someJson = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer'],
        }

    response.content_type = 'application/json'
    return dumps(someJson)


###############################################################################
# dependencies list example
# See https://bottlepy.org/docs/dev/tutorial_app.html#using-bottle-for-a-web-based-dependencies-list
###############################################################################

database = 'dependencyList.db'


# Read me a database and give me back a formatted table via a template
@route('/dependency')
def dependencies_list():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT id, task FROM dependencies WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


# Write to the database a new dependency
@route('/dependency/new', method='GET')
def new_item():
    from bottle import request

    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute("INSERT INTO dependencies (task, status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is \
            %s</p><br> <a href="../dependency">Return to list</a>' \
            % new_id
    else:
        return template('new_dependency')


# Read the database and give me back a single dependency result in JSON
# TODO: How does this now to send back JSON format and set the response header?
@route('/dependency/json/<id:re:[0-9]+>')
def show_json(id):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM dependencies WHERE id LIKE ?", (id,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'dependency': 'This item number does not exist!'}
    else:
        return {'dependency': result[0]}


# Read me a database and give me back all the results in JSON
@route('/dependency/json/all')
def show_json_all():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM dependencies")
    result = c.fetchall()
    c.close()

    if not result:
        return {'dependency': 'No results returned!'}
    else:
        return {'dependency': result}


if __name__ == "__main__":
    # reloader=true means you can edit the server and it will reload on next HTTP call
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
