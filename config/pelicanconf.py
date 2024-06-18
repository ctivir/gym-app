AUTHOR = 'Jaguar'
SITENAME = 'site'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Africa/Maputo'

DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Sobre', '/home'),
    ('Serviços', '/services'),
    ('Contactos', '/contacts'),
    ('Blog', '/archives.html'),
)
# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("@ctivir", "http://x.com/ctivir"),
    ("@ctivir", "http://github.com/ctivir"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-themes/semantic-ui',