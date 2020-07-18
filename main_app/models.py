from django.db import models


class StudentDetails(models.Model):
    student_name = models.CharField(max_length=70)
    age = models.IntegerField()
    class_name = models.CharField(db_column='class', max_length=30)
    section = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=50)
    parent_phone_number = models.CharField(max_length=15)
    class_teacher = models.CharField(max_length=50)
    favourite_sport = models.CharField(max_length=50)
    favourite_subject = models.CharField(max_length=30)

    class Meta:
        db_table = 'student_details'


class ParentsDetails(models.Model):
    parent_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    educational_qualification = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = 'parents_details'


class TeacherDetails(models.Model):
    teacher_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    head_of_class = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    years_of_experience = models.IntegerField()
    educational_qualification = models.CharField(max_length=50)
    complaints = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher_details'


class DriverDetails(models.Model):
    driver_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    lic_no = models.CharField(max_length=20)
    experience = models.IntegerField()
    complaints = models.CharField(max_length=100)
    route = models.CharField(max_length=50)

    class Meta:
        db_table = 'driver_details'
