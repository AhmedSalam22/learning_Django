
import csv  # https://docs.python.org/3/library/csv.html

# python3 manage.py shell < many/load.py

from unesco.models import Category , States , Site  ,Iso , Region 

fhand = open('whc-sites-2018-clean.csv')
reader = csv.reader(fhand)

Category.objects.all().delete()
States.objects.all().delete()
Iso.objects.all().delete()
Region.objects.all().delete()
States.objects.all().delete()


for row in reader:
    print(row)

    c, created = Category.objects.get_or_create(name=row[7])
    s, created = States.objects.get_or_create(name=row[8])
    i, created = Iso.objects.get_or_create(name=row[10])
    r, created = Region.objects.get_or_create(name=row[9])
    m = Site(
            name=row[0], 
            description=row[1], 
            justification= row[2],
            year = row[3] ,
            longitude =  row[4] ,
            latitude =  row[5] ,
            area_hectares =  row[6] ,
            category = c ,
            states = s ,
            region = r ,
          	iso = i
              )
    m.save()