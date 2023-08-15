from django.contrib import admin
from users.models import Profile, Ticket
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    search_fields = ["user"]


class TicketAdmin(admin.ModelAdmin):
    list_display = ["author", "subject", "created_date", "updated_date"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ticket, TicketAdmin)
