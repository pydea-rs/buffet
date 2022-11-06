from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AdminManager(UserAdmin):
    # admin section:
    # localhost:8000/admin
    # 127.0.0.1:8000/admin

    # this will customize the admin panel according to our custom account

    # fields that are displayed in all users list:
    list_display = ('username', 'contact', 'joined', 'last_login', 'is_active')
    list_display_links = ('username', 'contact')  # these fields in users list,
    # will open that account's page when clicked
    readonly_fields = ('id', 'joined', 'last_login')  # these fields can not change at all
    ordering = ('-joined', )  # sort users list by date_joined descending order
    filter_horizontal = ()
    list_filter = ()

    # fields that are shown in admin account panel
    # ( when you click on a account you will go to a page with these fields )
    fieldsets = (('Credentials', {'fields': ('username', 'password', 'id')}),
                 ('Personal Info', {'fields': ('contact', 'joined', 'last_login')}),
                 ('Permissions', {'fields': ('is_superuser', 'is_staff')}),)

    # fields in the admin add account panel
    add_fieldsets = (('Credentials', {'fields': ('username', 'password')}),
                     ('Personal Info', {'fields': ('contact', 'joined')}),
                     ('Permissions', {'fields': 'is_staff'}),)


admin.site.register(Account, AdminManager)
