from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    Popen([
        "bokeh",
        "serve",
        "app-simple-annotator",
        "app-linked-annotator",
        "--allow-websocket-origin=*",
    ])
