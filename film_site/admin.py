from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import admin

from django.contrib.admin.models import LogEntry

from .models import VideoType, MyWorks, AboutMe, Order, Hashtags

AdminSite.site_header = "Только для видеооператора сайта"

# LogEntry.objects.all().delete()

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


@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
    model = Hashtags

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    model = AboutMe
    search_fields = ['firstName', 'lastName']


class TotalPrice(ChangeList):

    def get_results(self, request):
        super(TotalPrice, self).get_results(request)
        q = self.result_list.aggregate(total=Sum('price'))
        self.total_count = q['total']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    change_list_template = "admin/model_change_list.html"

    model = Order
    list_display = ('create_at', 'full_name', 'email', 'event_date', 'event_time', 'typeVideo', 'timeWork', 'price')
    search_fields = ['firstName', 'lastName', 'eventDate', 'typeVideo__name', 'price']
    list_filter = ['typeVideo__name']
    date_hierarchy = 'eventDate'

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'ЗАКАЗЧИК'

    def event_date(self, obj):
        return obj.eventDate.strftime("%d.%m.%Y")
    event_date.short_description = 'ДАТА СЪЕМОК'

    def create_at(self, obj):
        return obj.created_at.strftime("%d.%m.%Y")
    create_at.short_description = 'ДАТА ЗАКАЗА'

    def event_time(self, obj):
        return obj.eventTime.strftime("%H:%M")
    event_time.short_description = 'ВРЕМЯ НАЧАЛА СЪЕМОК'

    def get_changelist(self, request):
        return TotalPrice


admin.site.unregister(User)
admin.site.unregister(Group)
