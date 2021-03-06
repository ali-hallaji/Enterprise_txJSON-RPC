#!../bin/python
# Core import
import sys
import random
from json import dumps
from config.settings import CREDENTIALS


cred = random.choice(CREDENTIALS)
get_token = cred[0] + ':' + cred[1]


usage = """
Options:\n\n[General options]:\n\n\n
 help                       Show this usage information.
                            for func help please send second arg
                            as a method name.
                            e.g:
                            ./manage.py help main.stop

 version                    Show version information

 runserver                  Start your server (For custom port, please
                            see settings file.)

 shutdown                   Shutdown your server
[0
 start_component            Create your component. send your
                            component name as second argument.
                            e.g: python manage.py start_component test

 logs                       Show all logs(error, jobs, debug, object,
                            service, request)

 plugin                     Show All components with their plugins.

 memory                     Access to all data of the shared memory.
                            Just pass your key to memory option.
                            e.g: python manage.py memory local_airports

 generate_settings          Generate your settings_local from scratch.
                            e.g: python manage.py generate_settings
"""


def main():

    if len(sys.argv) > 1:

        if sys.argv[1] == 'runserver':
            from runner import initRPC

            
            # Start server from here
            initRPC()

        elif sys.argv[1] == 'start_component':
            from core.manager.execute_start_component import start_component

            # Create component
            start_component(sys.argv[2])

        elif sys.argv[1] == 'shutdown':
            from jsonrpclib import Server
            from socket import error
            from config.settings import CORE_PORT

            try:
                conn = Server(
                    'http://{0}@localhost:{1}'.format(get_token, CORE_PORT)
                )
                conn.main.stop()

            except error:
                print 'Core Services shutdown \t\t\t\t\t\t[OK]'

        elif sys.argv[1] == 'logs':
            from os import system
            from config.settings import CORE_ID

            system('tail -f /var/log/core/{0}/*'.format(CORE_ID))

        elif sys.argv[1] == 'memory':
            from jsonrpclib import Server
            from socket import error
            from config.settings import CORE_PORT

            try:
                key = sys.argv[2]
                conn = Server(
                    'http://{0}@localhost:{1}'.format(get_token, CORE_PORT)
                )
                data = conn.main.access_shared_memory(key)
                pretty(data)

            except error:
                print 'Core Services shutdown \t\t\t\t\t\t[OK]'

        elif sys.argv[1] == 'generate_settings':
            from shutil import copyfile
            from config.settings import BASE_DIR

            raw = BASE_DIR + '/config/settings_local.txt'
            gen = BASE_DIR + '/config/settings_local.py'

            copyfile(raw, gen)

        elif sys.argv[1] == 'plugin':
            from jsonrpclib import Server
            from socket import error
            from config.settings import CORE_PORT

            try:
                conn = Server(
                    'http://{0}@localhost:{1}'.format(get_token, CORE_PORT)
                )
                data = conn.listMethods()
                pretty(dumps(data))

            except error:
                print 'Core Services shutdown \t\t\t\t\t\t[OK]'

        elif sys.argv[1] == 'help':

            if len(sys.argv) == 3:
                from os import system
                from jsonrpclib import Server
                from socket import error
                from config.settings import CORE_PORT

                try:
                    conn = Server(
                        'http://{0}@localhost:{1}'.format(
                            get_token,
                            CORE_PORT
                        )
                    )
                    data = conn.methodHelp(sys.argv[2])
                    system('echo {}'.format(data))

                except error:
                    print 'Core Services shutdown \t\t\t\t\t\t[OK]'

            elif len(sys.argv) == 2:
                print usage


def pretty(data):
    from os import system

    try:
        import pjson

    except ImportError:
        print "Please install pjson module. \t( sudo pip install pjson )"
        return

    system("""echo '{0}' | pjson""".format(data))


if __name__ == "__main__":
    # execute only if run as a script
    main()
