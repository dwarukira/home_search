from django.contrib import admin

from listing.models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass