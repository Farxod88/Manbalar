from django.contrib import admin

from sources.models import Sources, Atribute, Contents, Interive_contents


# class SourcesAdmin(admin.ModelAdmin):
#     list_display = ('category','title', 'created', 'updated', )
#     list_display_links = ('category', 'title')
#     list_filter = ('category', 'title')
#     search_fields = ('category', 'title')
#     ordering = ('-created',)
#     list_per_page = 10


class SourcesInline(admin.TabularInline):
    model = Atribute
    extra = 1
    list_display = ('title', 'description',  'count', )
    list_display_links = ('title', 'description',  'count', )


class ContentsInline(admin.TabularInline):
    model = Contents
    extra = 1
    list_display = ('title', 'tex',  'count', )
    list_display_links = ('title', 'tex',  'count', )
    list_filter = ('title', 'tex',  'count', )
    search_fields = ('title', 'tex',  'count', )
    list_per_page = 10
    list_editable = ('title', 'tex',  'count', )








class Interive_contentsInline(admin.TabularInline):
    model = Interive_contents
    extra = 1


@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    inlines = [SourcesInline, ContentsInline, Interive_contentsInline, ]
    list_display = ('title', 'created', 'updated', )
    list_display_links = ('title',)





# admin.site.register(Sources, SourcesAdmin)
# admin.site.register(Province)
# admin.site.register(Atribute)
# admin.site.register(Select_filter)
