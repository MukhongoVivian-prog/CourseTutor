from django.contrib import admin

from Tutor.models import Contact, Checkout, Member, Images

# Register your models here.
admin.site.register(Checkout)
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(Images)

