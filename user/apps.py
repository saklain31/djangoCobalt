from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserConfig(AppConfig):
    name = 'user'
    def ready(self):
    	try:
    		import user.signals  # noqa
    		print("Loaded")
    	except Exception as e:
    		print(e)
    	
