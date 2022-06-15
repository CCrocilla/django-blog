from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # Autopopulate the slug field with the title
    prepopulated_fields = {'slug': ('title',)}

    # This will generate a Filter By in the Admin Panel
    list_filter = ('status', 'created_on')

    # Exercise 1) Display the List
    list_display = ('title', 'slug', 'status', 'created_on')

    # Exercise 2) Add a Search
    search_fields = ['title', 'content']

    # We are defining that the content field will have the summernote
    summernote_fields = ('content')

# The admin.site allow to pass in two arguments so it quickly get full.
# admin.site.register(Post)
# For the reason above we prefer to use a decorator @admin.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ The admin.ModelAdmin is a built-in Django Class """

    # Exercise 3) Use List_Display for: name, body, post, created_on, approved
    #             Use list_filter to filter by: approved and created_on
    #             Set search_fields for name, email and body

    list_display = ('name', 'body', 'post', 'created_on', 'approved')

    list_filter = ('approved', 'created_on')

    search_fields = ('name', 'email', 'body')

    # The following will perform action to approve comments
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)