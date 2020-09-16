from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        ''' Imports the signals we've setup in the Users app. '''
        import users.signals
