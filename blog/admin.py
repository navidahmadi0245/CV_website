from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    data_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'created_date', 'published_date')
    list_filter = ['status', 'created_date', 'published_date']
    ordering =['-created_date']
    search_fields = ['title', 'content',]
    #

admin.site.register(Post,PostAdmin)