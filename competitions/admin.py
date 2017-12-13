from django.contrib import admin
from competitions.models import Post
from .models import Competition, Apparatus, Group

admin.site.register(Post)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class GroupInline(admin.StackedInline):
    model = Group


@admin.register(Apparatus)
class ApparatusAdmin(admin.ModelAdmin):
    list_display = ['title', 'competition', 'created']
    list_filter = ['created', 'competition']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GroupInline]