import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
myapp = create_app(config_name)
myapp.app_context().push()

if __name__ == '__main__':
    myapp.run()
