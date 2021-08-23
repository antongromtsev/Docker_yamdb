from django.contrib import admin

from .models.users import MyUser
from .models.titles import Title


class MyUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "bio", "username", "role")
    search_fields = ("role",)
    list_filter = ("username",)
    # empty_value_display = "-пусто-"


# class GroupAdmin(admin.ModelAdmin):
#     list_display = ("pk", "title", "slug", "description")
#     search_fields = ("description",)
#     list_filter = ("slug",)
#     empty_value_display = "-пусто-"


class TitleAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description")
    search_fields = ("description",)
    list_filter = ("year",)
    # empty_value_display = "-пусто-"


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("pk", "text", "created", "author", "post")
#     search_fields = ("text",)
#     list_filter = ("created",)
#     empty_value_display = "-пусто-"


# class FollowAdmin(admin.ModelAdmin):
#     list_display = ("author", "user")
#     list_filter = ("author",)


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Title, TitleAdmin)
# admin.site.register(Group, GroupAdmin)
# admin.site.register(Post, PostAdmin)
