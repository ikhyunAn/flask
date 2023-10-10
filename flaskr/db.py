import sqlite3

import click
from flask import current_app, g


# retrieve database, create if it doesn't already exist
def get_db():
    '''
    g is a special object that is used to store data
    the stored data should be accessible by multiple functions during the request (shared resource)
    connection is stored and reused instead of creating a new connection
    '''
    if 'db' not in g:
        # sqlite3.connect establishes connection to the file pointed by the DATABASE configuration
        g.db = sqlite3.connect(
            # current app: object pointing to the Flask application handling the request
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.row returns rows that in "dict" format
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


'''
run SQL commands to the db.py file
'''
def init_db():
    # get_db(): returns db connection which is used to execute commands
    db = get_db()
    
    # open_resource(): opens a file relative to the specified package (flaskr)
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


'''
defines command line command called init-db
the command will then perform specified actions
'''
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


'''
init_app() takes an application and does registration for close_db and init_db_command
'''
def init_app(app):
    # clean-up
    app.teardown_appcontext(close_db)
    # command is called with the flask command
    app.cli.add_command(init_db_command)
