from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from apps.workspaces.models import Floor, RoomLayout, Room, Workspace, Spot


@admin.register(Spot)
class CustomRoomAdmin(admin.ModelAdmin):
    list_filter = ("enabled", "room", "row", "column", "identifier")
    list_display = admin.ModelAdmin.list_display + ("enabled", "room", "row", "column", "identifier")


@admin.register(Room)
class CustomRoomAdmin(admin.ModelAdmin):
    list_filter = ("floor", "layout", "capacity", "number", "name")
    list_display = admin.ModelAdmin.list_display + list_filter


class RoomInLine(admin.StackedInline):
    model = Room
    verbose_name_plural = 'Rooms'
    fk_name = 'floor'


@admin.register(Floor)
class CustomFloorAdmin(admin.ModelAdmin):
    inlines = [RoomInLine, ]
    list_filter = ("workspace", "number", "name")
    list_display = admin.ModelAdmin.list_display + list_filter


class FloorInLine(admin.StackedInline):
    model = Floor
    verbose_name_plural = 'Floors'
    fk_name = 'workspace'


@admin.register(Workspace)
class CustomWorkspaceAdmin(admin.ModelAdmin):
    inlines = [FloorInLine, ]


app_models = apps.get_app_config('workspaces').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
