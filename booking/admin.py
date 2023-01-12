from django.contrib import admin

from booking.models import *


# Register your models here.
class BusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bus, BusAdmin)


class SeatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seat, SeatAdmin)


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Route, RouteAdmin)


class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking, BookingAdmin)


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
