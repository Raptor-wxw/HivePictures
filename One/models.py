from django.db import models


class Pic(models.Model):
    package = models.IntegerField(primary_key=True, db_index=True, db_column='package')
    text = models.CharField(max_length=40, db_column='text')
    first_pic = models.CharField(max_length=100, db_column='first_pic')
    available = models.BooleanField(db_column='available', default=True)

    class Meta:
        db_table = 'Pic'
        ordering = ['package']


class Pics(models.Model):
    package = models.IntegerField(db_index=True, db_column='package')
    photo = models.CharField(max_length=100, db_column='photo')

    class Meta:
        db_table = 'Pics'
        ordering = ['package']
