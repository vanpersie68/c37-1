#!c:\users\vanpersie\desktop\r13r4version\r1r3r4\backend\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autobahn==23.1.2','console_scripts','xbrnetwork'
__requires__ = 'autobahn==23.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autobahn==23.1.2', 'console_scripts', 'xbrnetwork')()
    )
