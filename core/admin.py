from django.contrib import admin

# Register your models here.
from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
	list_display = ('propietario', 'todo', 'hecho')
	exclude = ('propietario',)

	def save_model(self, request, obj, form, change):
		obj.propietario = request.user
		obj.save()


admin.site.register(ToDo, ToDoAdmin)