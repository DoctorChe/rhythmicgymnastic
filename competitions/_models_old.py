from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import TextInput, Textarea, NumberInput
from django.urls import reverse

from .choices import CATEGORY


class Competition(models.Model):
    title = models.CharField(verbose_name='наименование', max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    place = models.CharField(verbose_name='место проведения соревнований', max_length=256)
    start = models.DateField(verbose_name='дата начала соревнований', auto_now_add=False)
    end = models.DateField(verbose_name='дата окончания соревнований', auto_now_add=False)
    # parent = models.CharField(max_length=256, blank=True)

    # fullname = models.CharField(max_length=256, blank=True)

    age_from = models.CharField(max_length=4, blank=True)
    age_to = models.CharField(max_length=4, blank=True)
    organizer = models.CharField(verbose_name='организатор соревнований', max_length=256, blank=True)
    judge = models.CharField(verbose_name='судьи', max_length=256, blank=True)
    sec = models.CharField(verbose_name='секретарь', max_length=256, blank=True)
    # logo = models.ImageField(verbose_name='логотип', upload_to=None, height_field=None, width_field=None,
    #                                max_length=100, blank=True)
    # logo_print = models.BooleanField(verbose_name='печатать логотип')
    # logo_dim = models.CharField(max_length=4, verbose_name='размер логотипа', blank=True)
    # team_type = models.CharField(max_length=4, blank=True)
    # team_n = models.CharField(max_length=4, blank=True)

    class Meta:
        ordering = ('start',)
        verbose_name = 'соревнование'
        verbose_name_plural = 'соревнования'

    def __str__(self):
        return self.title

    def make_fullname(self):
        return "%s %s" % (self.start, self.title)

    make_fullname.short_description = "Полное название соревнования"
    full_name = property(make_fullname)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def get_absolute_url(self):
    #     return reverse('competitions:competition_detail',
    #                    args=[self.start.year,
    #                          self.start.strftime('%m'),
    #                          # self.start.strftime('%d'),
    #                          self.slug])


# class Date(models.Model):
#     date_parent = models.ForeignKey(Competition, verbose_name='соревнование', related_name='dates',
#                                     on_delete=models.CASCADE)
#     date_value = models.DateField(verbose_name='дата', auto_now_add=False)
#
#     date_number = models.PositiveIntegerField(verbose_name='порядковый номер', )
#     date_shortname = models.CharField(verbose_name='короткое имя', max_length=16, blank=True)
#     date_fullname = models.CharField(verbose_name='полное имя', max_length=256, blank=True)
#     # slug = models.SlugField(max_length=256, unique=True)
#
#     date_start = models.CharField(verbose_name='начало мероприятий в этот день', max_length=32, blank=True)
#     date_end = models.CharField(verbose_name='конец мероприятий в этот день', max_length=32, blank=True)
#
#     date_age_from = models.CharField(max_length=4, blank=True)
#     date_age_to = models.CharField(max_length=4, blank=True)
#
#     date_n = models.CharField(max_length=4, blank=True)
#
#     class Meta:
#         ordering = ('date_value',)
#         verbose_name = 'дата'
#         verbose_name_plural = 'даты'
#
#     def __str__(self):
#         return self.date_fullname
#
#     def make_shortname(self):
#         return f"{self.date_number}-й день"
#
#     def make_fullname(self):
#         return f"{self.date_parent.title} ({self.date_number}-й день)"
#
#
# class Flow(models.Model):
#     ROPE = 'RO'
#     HOOP = 'HO'
#     BALL = 'BA'
#     CLUBS = 'CL'
#     RIBBON = 'RI'
#     THREE_PLUS_TWO = 'TH'
#     ON_THE_CHOICE = 'ON'
#     NO_APPARATUS = 'NO'
#     APPARATUS = (
#         (NO_APPARATUS, 'Без предметов'),
#         (ROPE, 'Скакалка'),
#         (HOOP, 'Обруч'),
#         (BALL, 'Мяч'),
#         (CLUBS, 'Булавы'),
#         (RIBBON, 'Лента'),
#         (THREE_PLUS_TWO, '3+2'),
#         (ON_THE_CHOICE, 'На выбор'),
#     )
#     SUBGROUP = (
#         ('A', 'A'),
#         ('B', 'B'),
#         ('C', 'C'),
#         ('D', 'D'),
#         ('E', 'E'),
#         ('F', 'F'),
#     )
#
#     flow_parent = models.ForeignKey(Date, verbose_name='дата', related_name='flows', on_delete=models.CASCADE)
#     flow_fullname = models.CharField(verbose_name='полное название группы', max_length=256, blank=True)
#
#     flow_year_from = models.PositiveIntegerField(verbose_name='год рождения (от)', null=True)
#     flow_year_to = models.PositiveIntegerField(verbose_name='год рождения (до)', null=True)
#
#     flow_category = models.CharField(max_length=5,
#                                      verbose_name='разряд',
#                                      choices=CATEGORY)
#     flow_vid = models.CharField(max_length=64, blank=True)
#
#     flow_start = models.CharField(max_length=64, blank=True, null=True)
#     flow_end = models.CharField(max_length=64, blank=True, null=True)
#
#     flow_group = models.BooleanField(verbose_name='групповое выступление')
#     flow_wa = models.CharField(max_length=1, blank=True)
#     flow_prog = models.CharField(max_length=1, blank=True)
#     brake_type = models.CharField(verbose_name='тип перерыва', max_length=1, blank=True)
#     brake_name = models.CharField(verbose_name='название перерыва', max_length=128, blank=True)
#     flow_ex = models.PositiveIntegerField(verbose_name='количество видов выступлений', default=0,)
#     flow_sec = models.PositiveIntegerField(verbose_name='длительность одного выступления', default=120,)
#     flow_letter = models.CharField(max_length=1,
#                                    choices=SUBGROUP,
#                                    verbose_name='подгруппа',
#                                    blank=True)
#     flow_v1 = models.CharField(max_length=2,
#                                choices=APPARATUS,
#                                # default=NO_APPARATUS,
#                                blank=True)
#     flow_v2 = models.CharField(max_length=2,
#                                choices=APPARATUS,
#                                blank=True)
#     flow_v3 = models.CharField(max_length=2,
#                                choices=APPARATUS,
#                                blank=True)
#     flow_v4 = models.CharField(max_length=2,
#                                choices=APPARATUS,
#                                blank=True)
#     flow_vert = models.BooleanField(verbose_name='"Вертушка"')
#     flow_num_sf = models.CharField(max_length=32, blank=True)
#     flow_min_sf = models.CharField(max_length=32, blank=True)
#     flow_team_k = models.CharField(max_length=4, blank=True)
#
#     # def is_upperclass(self):
#     #     return self.year_in_school in (self.JUNIOR, self.SENIOR)
#
#     class Meta:
#         # ordering = ('date_value',)
#         verbose_name = 'группа'
#         verbose_name_plural = 'группы'
#
#     def make_fullname(self):
#         # cat = self.CATEGORY[next((i for i, v in enumerate(self.CATEGORY) if v[0] == self.flow_category), None)][1]
#         cat = dict(CATEGORY)[self.flow_category]
#         return f"Группа {self.flow_year_from}-{self.flow_year_to} г.р.,{cat}, {self.flow_ex} вида ()"
#
#     def make_flow_ex(self):
#         x = 0
#         for item in [self.flow_v1, self.flow_v2, self.flow_v3, self.flow_v4]:
#             if item:
#                 x = x + 1
#         return x
#
#     def make_flow_event(self):
#         return self.flow_parent.date_value
#
#     make_flow_event.short_description = "День потока"
#     flow_event = property(make_flow_event)
#
#
# class Subflow(models.Model):
#     subflow_parent = models.ForeignKey(Flow, related_name='subflows', on_delete=models.CASCADE)
#     subflow_start = models.TimeField(verbose_name='время старта выступлений потока', auto_now_add=False)
#     subflow_end = models.TimeField(verbose_name='время завершения выступлений потока', auto_now_add=False)
#     subflow_name = models.CharField(verbose_name='имя потока', max_length=64, blank=True)
#     subflow_fulname = models.CharField(verbose_name='полное имя потока', max_length=256, blank=True)
#     sub_brake_name = models.CharField(verbose_name='имя перерыва', max_length=256, blank=True)
#     sub_brake_type = models.CharField(verbose_name='тип перерыва', max_length=1, blank=True)
#
#     class Meta:
#         # ordering = ('date_value',)
#         verbose_name = 'поток'
#         verbose_name_plural = 'потоки'
#
#     def make_name(self):
#         # cat = dict(self.CATEGORY)[self.flow_category]
#         number = ''
#         return f"Поток {number}"
#
#     def make_fullname(self):
#         return f"{self.subflow_name} ()"


class Gymnast(models.Model):
    # gymnast_parent = models.ForeignKey(Subflow, related_name='gymnasts', on_delete=models.DO_NOTHING)
    competition_parent = models.ForeignKey(Competition, verbose_name='соревнование',
                                           related_name='gymnasts_comp', on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='имя гимнастки', max_length=256)
    year_of_birth = models.PositiveIntegerField(verbose_name='год рождения',
                                                validators=[MinValueValidator(2000), MaxValueValidator(2018)])
    category = models.CharField(max_length=5,
                                verbose_name='разряд',
                                choices=CATEGORY,
                                blank=True)
    city = models.CharField(verbose_name='город', max_length=32, blank=True)
    team = models.CharField(verbose_name='клуб', max_length=32, blank=True)
    coach = models.CharField(verbose_name='тренер', max_length=128, blank=True)
    is_group = models.NullBooleanField(verbose_name='это группа', null=True)
    start = models.PositiveIntegerField(default=0, blank=True, null=True)
    position = models.PositiveIntegerField(default=0, blank=True, null=True)
    position_v1 = models.PositiveIntegerField(blank=True, null=True)
    position_v2 = models.PositiveIntegerField(blank=True, null=True)
    position_v3 = models.PositiveIntegerField(blank=True, null=True)
    position_v4 = models.PositiveIntegerField(blank=True, null=True)
    position_v5 = models.PositiveIntegerField(blank=True, null=True)
    position_v6 = models.PositiveIntegerField(blank=True, null=True)
    position_v7 = models.PositiveIntegerField(blank=True, null=True)
    result = models.FloatField(blank=True, null=True)
    result_v1 = models.FloatField(blank=True, null=True)
    result_v2 = models.FloatField(blank=True, null=True)
    result_v3 = models.FloatField(blank=True, null=True)
    result_v4 = models.FloatField(blank=True, null=True)
    result_v5 = models.FloatField(blank=True, null=True)
    result_v6 = models.FloatField(blank=True, null=True)
    result_v7 = models.FloatField(blank=True, null=True)
    subresult = models.FloatField(blank=True, null=True)
    penalty = models.FloatField(blank=True, null=True)
    post = models.CharField(max_length=128, blank=True)
    v1 = models.IntegerField(verbose_name='упражнение №1', default=-1, blank=True, null=True)
    v2 = models.IntegerField(verbose_name='упражнение №2', default=-1, blank=True, null=True)
    v3 = models.IntegerField(verbose_name='упражнение №3', default=-1, blank=True, null=True)
    v4 = models.IntegerField(verbose_name='упражнение №4', default=-1, blank=True, null=True)
    checked = models.BooleanField(default=0)
    number = models.PositiveIntegerField(verbose_name='порядковый номер выступления', blank=True, null=True)

    class Meta:
        # ordering = ('date_value',)
        verbose_name = 'гимнастка'
        verbose_name_plural = 'гимнастки'

    def __str__(self):
        return self.name

    def calc_result_v1(self):
        # lst = [item.result_result1 for item in self.results.all() if item.result_result1]
        lst = [item.result1 for item in self.results.all() if item.result1]
        return max(lst) if lst else None

    def calc_result_v2(self):
        lst = [item.result2 for item in self.results.all() if item.result2]
        return max(lst) if lst else None

    def calc_result_v3(self):
        lst = [item.result3 for item in self.results.all() if item.result3]
        return max(lst) if lst else None

    def calc_result_v4(self):
        lst = [item.result4 for item in self.results.all() if item.result4]
        return max(lst) if lst else None

    def calc_result(self, *args):
        lst = [item for item in args if item]
        return sum(lst) if lst else None

    def get_category_display(self):
        for cat in CATEGORY:
            if cat[0] == self.category:
                return cat[1]

    # def get_absolute_url(self):
    #     return reverse('gymnasts:cgymnast_detail',
    #                    args=[self.start.year,
    #                          self.start.strftime('%m'),
    #                          # self.start.strftime('%d'),
    #                          self.slug])


class Result(models.Model):
    parent = models.ForeignKey(Gymnast, verbose_name='гимнастка', related_name='results',
                               on_delete=models.CASCADE)
    # competition_parent = models.ForeignKey(Competition, verbose_name='соревнование', related_name='results_comp',
    #                                        on_delete=models.CASCADE)

    # Оценка D
    tv1d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv2d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv3d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv4d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv5d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv6d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)
    tv7d = models.FloatField(verbose_name='окончательная оценка D', blank=True, null=True)

    # Оценка E
    tv1e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv2e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv3e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv4e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv5e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv6e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)
    tv7e = models.FloatField(verbose_name='окончательная оценка E', blank=True, null=True)

    score1 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score2 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score3 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score4 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score5 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score6 = models.FloatField(verbose_name='оценка', blank=True, null=True)
    score7 = models.FloatField(verbose_name='оценка', blank=True, null=True)

    result1 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result2 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result3 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result4 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result5 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result6 = models.FloatField(verbose_name='сумма', blank=True, null=True)
    result7 = models.FloatField(verbose_name='сумма', blank=True, null=True)

    pv1k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv2k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv3k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv4k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv5k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv6k = models.FloatField(verbose_name='сбавка', blank=True, null=True)
    pv7k = models.FloatField(verbose_name='сбавка', blank=True, null=True)

    # Обруч
    v1d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v1d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v1d3 = models.FloatField(blank=True, null=True)
    v1d4 = models.FloatField(blank=True, null=True)

    v1e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v1e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v1e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v1e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v1e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    # Мяч
    v2d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v2d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v2d3 = models.FloatField(blank=True, null=True)
    v2d4 = models.FloatField(blank=True, null=True)

    v2e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v2e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v2e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v2e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v2e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    # Булава
    v3d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v3d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v3d3 = models.FloatField(blank=True, null=True)
    v3d4 = models.FloatField(blank=True, null=True)

    v3e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v3e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v3e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v3e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v3e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    # Лента
    v4d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v4d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v4d3 = models.FloatField(blank=True, null=True)
    v4d4 = models.FloatField(blank=True, null=True)

    v4e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v4e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v4e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v4e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v4e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    v5d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v5d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v5d3 = models.FloatField(blank=True, null=True)
    v5d4 = models.FloatField(blank=True, null=True)

    v5e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v5e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v5e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v5e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v5e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    v6d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v6d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v6d3 = models.FloatField(blank=True, null=True)
    v6d4 = models.FloatField(blank=True, null=True)

    v6e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v6e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v6e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v6e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v6e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    v7d1 = models.FloatField(verbose_name='D1/D2', blank=True, null=True)
    v7d2 = models.FloatField(verbose_name='D3/D4', blank=True, null=True)
    v7d3 = models.FloatField(blank=True, null=True)
    v7d4 = models.FloatField(blank=True, null=True)

    v7e1 = models.FloatField(verbose_name='E1/E2', blank=True, null=True)
    v7e2 = models.FloatField(verbose_name='E3', blank=True, null=True)
    v7e3 = models.FloatField(verbose_name='E4', blank=True, null=True)
    v7e4 = models.FloatField(verbose_name='E5', blank=True, null=True)
    v7e5 = models.FloatField(verbose_name='E6', blank=True, null=True)

    class Meta:
        # ordering = ('date_value',)
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'

    def __str__(self):
        return f'Результаты выступления ({self.parent})'

    def make_tv_d(self, *args):
        lst = [item for item in args if item]
        return sum(lst) if lst else None

    result_e = {
        0: lambda x: None,
        1: lambda x: sum(x),
        2: lambda x: sum(x) / 2,
        3: lambda x: sum(x) - (min(x) + max(x)),
        4: lambda x: (sum(x) - (min(x) + max(x))) / 2,
        5: lambda x: (sum(x) - (min(x) + max(x))) / 3
    }

    def make_tv_e(self, *args):
        lst1 = []
        i = 0
        for item in args:
            if item:
                i = i + 1
                lst1.append(item)
        return self.result_e[i](lst1)

    def calc_total_score(self, *args):
        lst = [item for item in args if item]
        return sum(lst) if lst else None

    def calc_total_result(self, score, penalty):
        if score and penalty:
            res = score - penalty
        elif score and not penalty:
            res = score
        else:
            res = None
        return res

    def calc_total(self):
        lst = [self.result1, self.result2, self.result3, self.result4]
        res = 0
        for item in lst:
            if item:
                res += item
        return res

        # self.result_parent.gymnast_result_v1 = self.result_tv1d + self.result_tv1e if self.result_tv1d and self.result_tv1e else 0
        # return self.result_parent.gymnast_result_v1
    calc_total.short_description = 'сумма всего'
    # calc_total.empty_value_display = '-'
    # total_score1 = property(calc_total_score)

    def get_competition_parent(self):
        return self.parent.competition_parent.full_name

    get_competition_parent.short_description = 'соревнование'

    def make_fullname(self):
        return "%s %s" % (self.parent.competition_parent.full_name, self.parent)
        # return "%s" % (self.parent)

    make_fullname.short_description = "Полное название гимнастки"
    full_name = property(make_fullname)



# class Apparatus(models.Model):
#     owner = models.ForeignKey(User, related_name='apparatus_created', on_delete=models.DO_NOTHING)
#     competition = models.ForeignKey(Competition, related_name='apparatuses', on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True)
#     overview = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('-created',)
#
#     def __str__(self):
#         return self.title
#
#
# class Group(models.Model):
#     apparatus = models.ForeignKey(Apparatus, related_name='groups', on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Gymnast(models.Model):
#     group = models.ForeignKey(Group, related_name='gymnasts', on_delete=models.DO_NOTHING)
#     gymnast_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('gymnast_type', 'object_id')

from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('competitions:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
