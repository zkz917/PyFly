from fly_bbs import create_app
from flask_script import Manager, Server
import os

config_name = os.environ.get('FLASK_CONFIG') or 'Dev'
app = create_app(config_name)
server = Server(host="0.0.0.0", port=9000)

manager = Manager(app)
manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()

