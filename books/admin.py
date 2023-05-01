from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review   

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    search_fields = ('title', 'author')
    #exclude = ('price',)
    #fields = ('title', 'author', 'price')
    #readonly_fields = ('title',)
    #filter_horizontal = ('author',)
    #filter_vertical = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ('price',)
    #list_editable = ('price',)
    #list_per_page = 2
    #list_max_show_all = 5
    #list_filter = ('price',)
    #actions = ('make_published',)
    #def make_published(self, request, queryset):
    #    rows_updated = queryset.update(status='p')
    #    if rows_updated == 1:
    #        message_bit = "1 book was"
    #    else:
    #        message_bit = "%s books were" % rows_updated
    #    self.message_user(request, "%s successfully marked as published." % message_bit)
    list_display = ('title', 'author', 'price')
    

admin.site.register(Book, BookAdmin)
