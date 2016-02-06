from django.db import models

class Document(models.Model):
    DOCUMENT_TYPES = (('w','written'),('o','oral'),('x','extra'))
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    date = models.DateField()
    total_pages = models.IntegerField()
    doc_type = models.CharField(max_length=1,choices=DOCUMENT_TYPES)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Examiner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
