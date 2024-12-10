from django.contrib import admin

from Tutor.models import Contact, Checkout, Member, ImageModel

# Register your models here.
admin.site.register(Checkout)
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(ImageModel)
