#!/usr/bin/env python3
"""Django Manage."""
import warnings
import os
import sys

warnings.filterwarnings('ignore', category=UserWarning, module='cffi')

def memory_limit():
    import resource
    """Limit max memory usage to half."""
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Convert KiB to bytes, and divide in two to half
    #po = int(get_memory() * 1024 / 2)
    resource.setrlimit(resource.RLIMIT_AS, (1073741824, hard))

memory_limit()

if __name__ == '__main__':
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobsf.MobSF.settings')

    from django.core.management import execute_from_command_line
    if 'runserver' in sys.argv:
        print('We do not allow debug server anymore. '
              'Please follow official docs: '
              'https://mobsf.github.io/docs/')
        sys.exit(0)
    execute_from_command_line(sys.argv)
