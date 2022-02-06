from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import VideoType, MyWorks, AboutMe, Order

AdminSite.site_header = "Только для администратора сайта"

@admin.register(VideoType)
class VideoTypeAdmin(admin.ModelAdmin):
    model = VideoType
    list_display = ('name', 'price')
    search_fields = ['name', 'price']


@admin.register(MyWorks)
class MyWorksAdmin(admin.ModelAdmin):
    model = MyWorks
    list_display = ('name', 'videoType')
    search_fields = ['name', 'videoType__name']
    list_filter = ['videoType__name']


# @admin.register(AboutMe)
# class AboutMeAdmin(admin.ModelAdmin):
#     model = AboutMe
#     search_fields = ['firstName', 'lastName']


class TotalPrice(ChangeList):

    def get_results(self, request):
        super(TotalPrice, self).get_results(request)
        q = self.result_list.aggregate(total=Sum('price'))
        self.total_count = q['total']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    change_list_template = "admin/model_change_list.html"
    
    model = Order
    list_display = ('created_at', 'lastName', 'firstName', 'price', 'eventDate', 'typeVideo', 'timeWork', 'email')
    search_fields = ['lastName', 'firstName', 'price', 'eventDate', 'typeVideo__name', 'timeWork']
    list_filter = ['typeVideo__name']
    date_hierarchy = 'eventDate'

    def get_changelist(self, request):
        return TotalPrice


admin.site.unregister(User)
admin.site.unregister(Group)
