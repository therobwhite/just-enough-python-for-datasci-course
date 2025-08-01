# jupyter_server_config.py

from traitlets.config import get_config

c = get_config()

# bind on 0.0.0.0 so all interfaces are available
c.ServerApp.ip = '0.0.0.0'

# explicit port (optional if you’re fine with 8888)
c.ServerApp.port = 9000

# don’t open a browser inside the container
c.ServerApp.open_browser = False

# allow connections from any origin (for CORS)
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_root = True

c.ServerApp.websocket_ping_timeout = 90000

# disable auth if you really want, or set a token/password
# c.ServerApp.token       = ''
# c.ServerApp.password    = ''
