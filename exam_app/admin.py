from django.contrib import admin
from .models import *


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'group')
    search_fields = ('first_name', 'last_name', 'email', 'group_name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    search_fields = ('name', 'subject_name')


@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'student')
    search_fields = ('exam_name', 'student_first_name', 'student_last_name')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'exam')
    search_fields = ('name', 'exam_name')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_correct', 'question')
    search_fields = ('name', 'question_name')