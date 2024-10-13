import os



def update_context(app, pagename, templatename, context, doctree):
    context["minimal_theme_version"] = "1234"

    # Convert 'show_powered_by' in the theme options to
    # the preferred option, html_show_sphinx.
    # html_theme_options = app.config.html_theme_options
    # if "show_powered_by" in html_theme_options:
    #     show_powered_by = html_theme_options["show_powered_by"]
    #     if isinstance(show_powered_by, str):
    #         context["show_sphinx"] = show_powered_by.lower() == "true"
    #     else:
    #         context["show_sphinx"] = bool(show_powered_by)  # to allow int values

def setup(app):
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('minimal_theme', theme_path)
    app.connect("html-page-context", update_context)