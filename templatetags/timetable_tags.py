# your_app/templatetags/timetable_tags.py

from django import template

register = template.Library()

@register.filter
def get_class_timetable(timetables, class_name):
    return timetables.filter(class_name__class_name=class_name)

@register.filter
def get_day_timetable(timetables, day):
    return timetables.filter(day=day)
