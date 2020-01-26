from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import Photo, Booking, Feedback


@admin.register(Photo)
class PhotoAdmin(SortableAdmin):
    list_display = ['name', 'image_tag', ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'start_date', 'end_date', 'persons', 'phone', 'email', 'created_at', ]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'created_at', ]
