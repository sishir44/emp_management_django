from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

# to change header name in the admin panel
admin.site.site_header = 'Employee Management'

# Register your models here.

class EmpAdmin(admin.ModelAdmin):

    #to display
    list_display = ('name', 'working', 'emp_id', 'phone')

    # to edit
    list_editable = ('working', 'emp_id')

    #to search
    search_fields = ('name','phone')

    # to filter
    list_filter = ('working',)

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)

# Groups and Users are not shown in Admin Panel
admin.site.unregister(Group)
admin.site.unregister(User)


