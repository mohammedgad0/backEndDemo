from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Employee(models.Model):
    empid = models.CharField(_('Employee ID'), db_column='EmpId', unique=True, max_length=50)  # Field name made lowercase.
    empname = models.CharField(_('Employee name'), db_column='EmpName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deptcode = models.CharField(_('Dept code'),db_column='DeptCode', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    deptname = models.CharField(_('Department name'),db_column='DeptName', max_length=200, blank=True,
                                null=True)  # Field name made lowercase.
    ismanager = models.IntegerField(db_column='IsManager', blank=True, null=True)  # Field name made lowercase.
    ext = models.CharField(_('Extension'), db_column='Ext', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(_('Mobile'), db_column='Mobile', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(_('Email'), db_column='Email', max_length=100, unique=True, null=False)  # Field name made lowercase.
    jobtitle = models.CharField(_('Job Title'), db_column='JobTitle', max_length=200, blank=True,
                                null=True)  # Field name made lowercase.
    managercode = models.BigIntegerField(db_column='ManagerCode', blank=True, null=True)  # Field name made lowercase.
    sexcode = models.CharField(_('Gender'), db_column='SexCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    iscontract = models.IntegerField(db_column='IsContract', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.empname
    class Meta:
        managed = True
        db_table = 'employee'
        verbose_name_plural = _('Employees')