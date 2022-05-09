from django.contrib import admin
from .models import Worker, SellsPoint, Visit

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(SellsPoint)
class SellsPointAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    readonly_fields = ("time", "sells_point", "longitude", "latitude",)
    search_fields = ("sells_point__name", "sells_point__worker__name")