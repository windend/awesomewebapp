import os
import sys
import time
import subprocess
from livereload import server, shell

server.watch('C:\\Users\\Bootun\\Documents\\webapp\\awesomewebapp\\www\\')
server.serve(port=9000, host='127.0.0.1')
