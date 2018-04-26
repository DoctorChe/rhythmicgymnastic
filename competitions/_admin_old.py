from django.contrib import admin
from .models import Competition, Gymnast, Result
# from .models import Date, Flow, Subflow
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import TextInput, NumberInput
from django.db import models


# class DateInline(admin.StackedInline):
#     model = Date
#     # exclude = ('flow_start', 'flow_end', )
#
#
# class FlowInline(admin.StackedInline):
#     model = Flow
#     exclude = ('flow_start', 'flow_end',)
#
#
# class SubflowInline(admin.TabularInline):
#     model = Subflow


class GymnastInline(admin.StackedInline):
    model = Gymnast
    extra = 1


class ResultInline(admin.StackedInline):
    model = Result
    extra = 1


# @receiver(pre_save, sender=Competition)
# def calc_fullname(sender, instance, **kwargs):
#     instance.event_fullname = instance.make_fullname()


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,                      {'fields': ['title', 'event_place']}),
    #     ('Competition information', {'fields': ['event_organizer', 'event_judge', 'event_sec'],
    #                                  'classes': ['collapse']}),
    # ]
    list_display = ['title', 'full_name', 'place']
    list_filter = ['place', ]
    search_fields = ['title', 'place']
    fieldsets = [
        (None, {'fields': [('title', 'slug'), 'full_name']}),
        (None, {'fields': [('place', ),
                           ('start', 'end', ),
                           # ('event_age_from', 'event_age_to',),
                           ('organizer', 'sec', ),
                           # 'event_judge',
                           ]}),
        # ('Дополнительная информация', {'fields': ['event_logo',
        #                                           ('event_logo_print',
        #                                            'event_logo_dim',
        #                                            'event_team_type', ),
        #                                           'event_team_n'
        #                                           ],
        #                                'classes': ['collapse']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    # fields = (('title', 'slug'),)
    # exclude = ('event_key', 'event_parent', 'event_age_from', 'event_age_to', 'event_logo_dim', 'event_team_type',
    #            'event_team_n',)  # Исключить поля из панели администрирования
    save_as = True  # Включить возможность “сохранять как” на странице редактирования объекта (сохранит с новым ID)
    # inlines = [DateInline, ]
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size': '10'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    # }
    readonly_fields = ('full_name', )


# @receiver(pre_save, sender=Competition)
# def calc_fullname(sender, instance, **kwargs):
#     instance.event_fullname = instance.make_fullname()


# @admin.register(Date)
# class DateAdmin(admin.ModelAdmin):
#     list_display = ['date_parent', 'date_shortname', 'date_value']
#     list_display_links = ('date_shortname', 'date_value')
#     list_filter = ['date_parent', 'date_shortname']
#     search_fields = ['date_shortname', 'date_start']
#     date_hierarchy = 'date_value'  # Отображение дат
#     exclude = ('date_start', 'date_end',)
#     # prepopulated_fields = {'date_fullname': ('date_number', 'date_parent')}
#     inlines = [FlowInline, ]
#
#
# @receiver(pre_save, sender=Date)
# def calc_fullname(sender, instance, **kwargs):
#     instance.date_shortname = instance.make_shortname()
#     instance.date_fullname = instance.make_fullname()
#     instance.flow_fullname = instance.make_fullname()
#
#
# @admin.register(Flow)
# class FlowAdmin(admin.ModelAdmin):
#     list_display = ['flow_parent', 'flow_fullname', 'flow_category', 'make_flow_event']
#     list_display_links = ('flow_fullname', 'flow_category')
#     list_filter = ['flow_parent', 'flow_fullname']
#     search_fields = ['flow_fullname', 'flow_category']
#     exclude = ('flow_start', 'flow_end',)
#     inlines = [SubflowInline, ]
#
#
# @receiver(pre_save, sender=Flow)
# def calc_fullname(sender, instance, **kwargs):
#     instance.flow_ex = instance.make_flow_ex()
#     instance.flow_fullname = instance.make_fullname()
#
#
# @admin.register(Subflow)
# class SubflowAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['subflow_parent', ('subflow_name', 'subflow_fulname'),
#                            ('subflow_start', 'subflow_end')]}),
#         ('Subflow information', {'fields': ['sub_brake_name', 'sub_brake_type'],
#                                  'classes': ['collapse']}),
#     ]
#     list_display = ['subflow_parent', 'subflow_name', 'subflow_start', 'subflow_end']
#     list_display_links = ('subflow_name', 'subflow_start')
#     list_filter = ['subflow_parent', 'subflow_name']
#     search_fields = ['subflow_name', 'subflow_start']
#     # exclude = ('flow_start', 'flow_end', )
#     inlines = [GymnastInline, ]
#
#
# @receiver(pre_save, sender=Subflow)
# def calc_fullname(sender, instance, **kwargs):
#     instance.subflow_name = instance.make_name()
#     instance.subflow_fulname = instance.make_fullname()


@receiver(pre_save, sender=Gymnast)
def calc_fullname(sender, instance, **kwargs):
    instance.result_v1 = instance.calc_result_v1()
    instance.result_v2 = instance.calc_result_v2()
    instance.result_v3 = instance.calc_result_v3()
    instance.result_v4 = instance.calc_result_v4()
    instance.result = instance.calc_result(instance.result_v1,
                                           instance.result_v2,
                                           instance.result_v3,
                                           instance.result_v4)


@admin.register(Gymnast)
class GymnastAdmin(admin.ModelAdmin):
    list_display = ['competition_parent',
                    'name', 'year_of_birth', 'category', 'city', 'coach',
                    'number']
    list_display_links = ('name',)
    list_filter = ['competition_parent', 'number', 'category', 'city']
    search_fields = ['name', ]
    # exclude = ('flow_start', 'flow_end', )
    fieldsets = [
        (None, {'fields': ['competition_parent', ]}),
        (None, {'fields': [('name', 'category', 'year_of_birth',),
                           ('city', 'coach',),
                           ]}),
        ('Дополнительная информация', {'fields': ['position',
                                                  ('position_v1',
                                                   'position_v2',
                                                   'position_v3',
                                                   'position_v4', ),
                                                  ],
                                       'classes': ['collapse']}),
    ]
    readonly_fields = ('position', 'position_v1', 'position_v2',
                       'position_v3', 'position_v4')
    # inlines = [ResultInline, ]


@receiver(pre_save, sender=Result)
def calc_results(sender, instance, **kwargs):
    instance.tv1d = instance.make_tv_d(instance.v1d1,
                                       instance.v1d2)
    instance.tv1e = instance.make_tv_e(instance.v1e1,
                                       instance.v1e2,
                                       instance.v1e3,
                                       instance.v1e4,
                                       instance.v1e5)
    instance.tv2d = instance.make_tv_d(instance.v2d1,
                                       instance.v2d2)
    instance.tv2e = instance.make_tv_e(instance.v2e1,
                                       instance.v2e2,
                                       instance.v2e3,
                                       instance.v2e4,
                                       instance.v2e5)
    instance.tv3d = instance.make_tv_d(instance.v3d1,
                                       instance.v3d2)
    instance.tv3e = instance.make_tv_e(instance.v3e1,
                                       instance.v3e2,
                                       instance.v3e3,
                                       instance.v3e4,
                                       instance.v3e5)
    instance.tv4d = instance.make_tv_d(instance.v4d1,
                                       instance.v4d2)
    instance.tv4e = instance.make_tv_e(instance.v4e1,
                                       instance.v4e2,
                                       instance.v4e3,
                                       instance.v4e4,
                                       instance.v4e5)
    instance.score1 = instance.calc_total_score(instance.tv1d,
                                                instance.tv1e)
    instance.score2 = instance.calc_total_score(instance.tv2d,
                                                instance.tv2e)
    instance.score3 = instance.calc_total_score(instance.tv3d,
                                                instance.tv3e)
    instance.score4 = instance.calc_total_score(instance.tv4d,
                                                instance.tv4e)
    instance.result1 = instance.calc_total_result(instance.score1,
                                                  instance.pv1k)
    instance.result2 = instance.calc_total_result(instance.score2,
                                                  instance.pv2k)
    instance.result3 = instance.calc_total_result(instance.score3,
                                                  instance.pv3k)
    instance.result4 = instance.calc_total_result(instance.score4,
                                                  instance.pv4k)
    # instance.result_parent.gymnast_result_v1 = instance.total_score1


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    # def view_total_score1(self, obj):
    #     # return obj.result_tv1d + obj.result_tv1e
    #     return "%s" % obj.result_tv1d
    #
    # view_total_score1.short_description = 'сумма'
    # view_total_score1.empty_value_display = '???'

    # list_display = ['parent', 'competition_parent', 'score1', ]
    list_display = ['parent', 'full_name', 'score1', ]
    # list_display = ['parent', 'get_competition_parent', 'score1', ]
    fieldsets = [
        # (None, {'fields': ['competition_parent', 'parent', ]}),
        (None, {'fields': ['full_name', 'parent', ]}),
        ('Обруч',  {'fields': [('v1d1', 'v1d2',),
                               ('v1e1', 'v1e2', 'v1e3', 'v1e4', 'v1e5',),
                               ('tv1d', 'tv1e', 'score1',),
                               ('pv1k', 'result1',),
                               # ('total_score1', ),
                               ]}),
        ('Мяч',    {'fields': [('v2d1', 'v2d2',),
                               ('v2e1', 'v2e2', 'v2e3', 'v2e4', 'v2e5',),
                               ('tv2d', 'tv2e', 'score2',),
                               ('pv2k', 'result2',),
                               ]}),
        ('Булава', {'fields': [('v3d1', 'v3d2',),
                               ('v3e1', 'v3e2', 'v3e3', 'v3e4', 'v3e5',),
                               ('tv3d', 'tv3e', 'score3',),
                               ('pv3k', 'result3',),
                               ]}),
        ('Лента',  {'fields': [('v4d1', 'v4d2',),
                               ('v4e1', 'v4e2', 'v4e3', 'v4e4', 'v4e5',),
                               ('tv4d', 'tv4e', 'score4',),
                               ('pv4k', 'result4',),
                               ]}),
        ('Сумма всего', {'fields': ['calc_total']}),
        # ('Subflow information', {'fields': ['sub_brake_name', 'sub_brake_type'],
        #                          'classes': ['collapse']}),
    ]
    formfield_overrides = {
        models.FloatField: {'widget': NumberInput(attrs={'size': '5', 'min': '0', 'max': '10', 'step': '0.1'})},
        models.CharField: {'widget': TextInput(attrs={'size': '5'})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    readonly_fields = ('tv1d', 'tv1e',
                       'tv2d', 'tv2e',
                       'tv3d', 'tv3e',
                       'tv4d', 'tv4e',
                       'score1', 'score2', 'score3', 'score4',
                       'result1', 'result2', 'result3', 'result4',
                       'calc_total',
                       'get_competition_parent',
                       'full_name',
                       )
    list_display_links = ('parent',)
    # list_filter = ['competition_parent']
    # list_filter = ['get_competition_parent']
    # exclude = ('flow_start', 'flow_end', )
    search_fields = ['gymnast_parent', ]

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
