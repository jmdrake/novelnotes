from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Novel Notes'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = 'Application to allow note taking and studying for novels or other works of literature.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '389fc8c7-04ac-4c73-b5e5-da5aca4483aa'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
