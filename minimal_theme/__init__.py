import os

def setup(app):
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('minimal_theme', theme_path)