#!/usr/bin/env python3
"""Django Manage."""
import warnings
import os
import sys

warnings.filterwarnings('ignore', category=UserWarning, module='cffi')


from psutil import virtual_memory
from resource import setrlimit, RLIMIT_AS
setrlimit(RLIMIT_AS, (int(virtual_memory().available / 5), -1))

if __name__ == '__main__':
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobsf.MobSF.settings')

    from django.core.management import execute_from_command_line
    if 'runserver' in sys.argv:
        print('We do not allow debug server anymore. '
              'Please follow official docs: '
              'https://mobsf.github.io/docs/')
        sys.exit(0)
    execute_from_command_line(sys.argv)
