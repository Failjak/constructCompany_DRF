from django.contrib import admin

from .models import Order, Worker


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass
