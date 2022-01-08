import csv

from trees.models import Family


def run():
    fhand = open('excel/family.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Family.objects.all().delete()

    for row in reader:
        print(row)

        b, created = Family.objects.get_or_create(tree_family=row[0])

        # c = Cat(nickname=row[0], breed=b, weight=row[2])
        # c.save()

