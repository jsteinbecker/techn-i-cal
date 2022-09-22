from django.db.models import (Avg, Case, CharField, Count, F, FloatField,
                              IntegerField, Max, Min, OuterRef, Q, Sum, Value,
                              When)
from django_tables2 import tables
from django_tables2.utils import A

from .models import Employee, PtoRequest, Shift, ShiftTemplate, Slot, Workday


class EmployeeTable (tables.Table):
    """
    Base Table for All Employees
    Displays basic details about each employee
    """

    name = tables.columns.LinkColumn('employee-detail', args=[A('name')])

    class Meta:
        model           = Employee
        fields          = ['name', 'fte', 'streak_pref']
        template_name   = 'django_tables2/bootstrap.html'

class ShiftListTable (tables.Table) :
    """
    Summary for ALL SHIFTS
    """

    name = tables.columns.LinkColumn("shift", args=[A("name")])
    hours = tables.columns.Column(verbose_name="Hours", attrs={"td": {"class": "small"}})
    class Meta:
        model           = Shift
        fields          = ['name','start','hours', 'on_days_display']
        template_name   = 'django_tables2/bootstrap.html'
        
class ShiftsWorkdayTable (tables.Table):
    """
    View from a WORKDAY
    display ALL SHIFTS for a given day
    """

    class Meta:
        model           = Shift
        fields          = ['name','start','employee']
        template_name   = 'django_tables2/bootstrap.html'

class ShiftsWorkdaySmallTable (tables.Table):

    class Meta:
        model           = Shift
        fields          = ['name','employee']
        template_name   = 'django_tables2/bootstrap.html'

class WorkdayListTable (tables.Table):
    """
    Summary for ALL WORKDAYS
    """

    date = tables.columns.LinkColumn("workday", args=[A("date")])
    n_unfilled = tables.columns.Column(verbose_name="Unfilled Shifts")
    days_away = tables.columns.Column(verbose_name="Days Away") 


    class Meta:
        model           = Workday
        fields          = ['date', 'iweek', 'iperiod', 'iweekday', 'n_unfilled', 'days_away']
        template_name   = 'django_tables2/bootstrap.html'

    def render_n_unfilled(self, record):
        return record.n_unfilled

    def render_days_away(self, record):
        return record.days_away
    
class PtoListTable (tables.Table):

    workday = tables.columns.LinkColumn("workday", args=[A("workday")])

    class Meta:
        model           = PtoRequest
        fields          = ['workday', 'status', 'stands_respected' ]
        template_name   = 'django_tables2/bootstrap.html'

class WeeklyHoursTable (tables.Table):

    name = tables.columns.LinkColumn("employee-detail", args=[A("name")])
    hours = tables.columns.Column(verbose_name="Weekly Hours")

    class Meta:
        model           = Employee
        fields          = ['name', 'hours']
        template_name   = 'django_tables2/bootstrap.html'


