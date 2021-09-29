from django.db import models

# Create your models here.
class Employee(models.Model):
    empID = models.AutoField(primary_key=True,db_column='emp_ID')
    empName = models.CharField(max_length=50,db_column='emp_Name')
    empEmail = models.EmailField(max_length=200,db_column='emp_Email')
    password = models.CharField(max_length=50,db_column='password')
    empAddress = models.CharField(max_length=255,db_column='emp_Address')

    class Meta:
        db_table = 'employee'
