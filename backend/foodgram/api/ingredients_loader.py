import csv
import os
import sys

from api.models import Ingredient
from django.core.wsgi import get_wsgi_application

csv_filepathname = "ingredients.csv"
your_djangoproject_home = "foodgram"


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'foodgram.settings'


application = get_wsgi_application()


dataReader = csv.reader(open(csv_filepathname, encoding='UTF-8'), delimiter=',', quotechar='"')
next(dataReader)

id_count = 1

for row in dataReader:
    ingredient = Ingredient()
    ingredient.id = id_count
    ingredient.name = row[0]
    ingredient.measurement_unit = row[1]
    ingredient.save()
    id_count += 1
