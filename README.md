# leaf-note
# To Generate Secerect key
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
copy this key and paste it in env file
#.env file\n
#Project Credentials
SECRET_KEY=


#Database
OtherDB=True/False
if True:
  DATABASE_NAME=
  DATABASE_USER=
  DATABASE_PASSWORD=
  DATABASE_HOST=
  DATABASE_PORT=




#Email Credentials
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

#Axes
AXES_ENABLED=True
