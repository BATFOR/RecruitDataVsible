# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    number = models.CharField(primary_key=True, max_length=255)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    scale = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'company'


class Job(models.Model):
    number = models.ForeignKey(Company, models.DO_NOTHING, db_column='number')
    job = models.CharField(max_length=255)
    post_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    job_place = models.CharField(max_length=255)
    job_experience = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    min_wage = models.FloatField()
    max_wage = models.FloatField()
    job_duty = models.CharField(max_length=255)
    job_benefits = models.CharField(max_length=255)
    update_time = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'job'
        ordering = ['id']
