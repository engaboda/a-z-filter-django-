from django.db import models

# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    def __str__(self):
        return self.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'الموظف'
        verbose_name_plural = 'الموظفين'