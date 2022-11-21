# leaf-note
# To Generate Secerect key
1st way
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
2nd way
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
copy this key and paste it in env file
# For env file variables
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

AXES_ENABLED=True
