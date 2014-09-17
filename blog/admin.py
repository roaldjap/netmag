from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
	#fields display on change list
	list_display = ['title','description']
	
	#fields to search in change list
	list_filter = ['published', 'created']
	
	#enable the date drill down on change list
	date_hierarchy = 'created'

	#enable the save buttons on top on change form
	save_on_top = True

	#prepopulate the slug from the title - big timesaver!
	prepopulated_fields = {"slug": ("title",)}

#register the models to admin side.
admin.site.register(Post, PostAdmin)