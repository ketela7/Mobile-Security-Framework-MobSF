#!/usr/bin/env python3
"""Django Manage."""
import warnings
import os
import sys
import resource

warnings.filterwarnings('ignore', category=UserWarning, module='cffi')

def memory_limit():
    """Limit max memory usage to half."""
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    # Convert KiB to bytes, and divide in two to half
    resource.setrlimit(resource.RLIMIT_AS, (int(get_memory() * 1024 / 2), hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    print(free_memory)
    return free_memory  # KiB
    
if __name__ == '__main__':
    memory_limit()
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobsf.MobSF.settings')

    from django.core.management import execute_from_command_line
    if 'runserver' in sys.argv:
        print('We do not allow debug server anymore. '
              'Please follow official docs: '
              'https://mobsf.github.io/docs/')
        sys.exit(0)
    execute_from_command_line(sys.argv)
