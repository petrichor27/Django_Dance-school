from django.contrib import admin
from django.db import models


class Course(models.Model):
    id_cor = models.IntegerField(verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.IntegerField(default=0, verbose_name="Цена")

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return str(str(self.id_cor) + " " + self.name + " " + str(self.price))


class Client(models.Model):
    id_cl = models.IntegerField(verbose_name="ID")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиент"

    def __str__(self):
        return str( str(self.id_cl)+ " "  + self.lastname + " " + self.firstname + " " +self.middlename)


class Teacher(models.Model):
    id_t = models.IntegerField(verbose_name="ID")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватель"

    def __str__(self):
        return str( str(self.id_t)+ " "  + self.lastname + " " + self.firstname + " " +self.middlename)


class Dgroup(models.Model):
    id_g = models.IntegerField(verbose_name="ID")
    id_cl = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    id_cor = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    id_t = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группа"

    def __str__(self):
        return str( str(self.id_g)+ " " + str(self.id_cl)+ " " + str(self.id_cor) + " " + str(self.id_t))


#class Select(admin.SimpleListFilter):
#    title = "Выборка"
#    parameter_name = "select"

#    def lookups(self, request, model_admin):
#        return (('Вальс', 'Вальс'), ('Танго', 'Танго'), ('Народные танцы', 'Народные танцы'), ('Самбо', 'Самбо'))

#    def queryset(self, request, queryset):
#        if self.value() == 'Вальс':
#            return queryset.filter(cor='Вальс')
#        if self.value() == 'Танго':
#            return queryset.filter(cor='Танго')
#        if self.value() == 'Народные танцы':
#            return queryset.filter(cor='Народные танцы')
#        if self.value() == 'Самбо':
#            return queryset.filter(cor='Самбо')