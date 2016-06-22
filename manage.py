#!/usr/bin/env python
import os
from app import create_app, db
from app.models import Users, Products, Stores
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    '''Returns application and database instances
    to the shell importing them automatically
    on `python manager.py shell`.
    '''
    # db is database
    # Users is instance of the users table
    # Products is instance of products table
    # Stores is instance of stores table
    return dict(app=app, db=db, Users=Users, Products=Products,
                Stores=Stores)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# if __name__ == '__main__':
    # app.run()
