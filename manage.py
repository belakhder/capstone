
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from starter.app import create_app
from starter.models import db 
import unittest

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0', port=8080, debug=True)

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    manager.run()