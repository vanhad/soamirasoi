"""
WSGI config for SoamiRasoiProj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoamiRasoiProj.settings')
from whitenoise.django import WhiteNoise
application = get_wsgi_application()
application = WhiteNoise(application)
# application.add_files(settings.STATIC_ROOT, prefix='more-files/')