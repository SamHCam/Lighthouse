from django.contrib import admin
from .models import Request, Expense

class ExpenseInline(admin.TabularInline):
    model = Expense
    extra = 3


class RequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['request_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ExpenseInline]
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('request_text', 'pub_date', 'was_published_recently')

admin.site.register(Request, RequestAdmin)


