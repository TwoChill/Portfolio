# How does the argv work?

# Get '777' or '555' from argv
# Run script, and change permissions

# Or

# Show parent folder in which permissions is going to change
# Get '777' from usrinput
# Run script, and change permissions.

import os
from sys import argv

# If an argument variable is detected..
if len(argv) > 0:
    permissions = argv

class MyClass(object):

    def __init__(self):
        pass
    
    def change_permissions(self, argv):
        pass

    def get_folder_path(self):
        pass

chmd = MyClass()
chmd.