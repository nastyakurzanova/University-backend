# Create your models here.
from django.db import models
#--------

class Users(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField()
    phone = models.FloatField()
    # who_moderator = models.ForeignKey('Moderators', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        app_label = 'rip_lab1'
        managed = False
        db_table = 'users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    

class Audiences(models.Model):
    number = models.CharField(max_length=50)
    price = models.FloatField()
    img = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    corpus = models.CharField(max_length=50)
    deleted = models.BooleanField()
    def __str__(self):
        return self.number
    class Meta:
        app_label = 'rip_lab1'
        managed = False
        db_table = 'audiences' 
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class Booking_requests(models.Model):
    status = models.CharField(max_length=10)
    moderator = models.IntegerField()
    date_confirmed = models.DateTimeField()
    date_in_progress = models.DateTimeField()
    creater = models.IntegerField()
    date_booling = models.DateTimeField()
    date_added = models.DateTimeField()
    def __str__(self):
        return self.number, self.status
    class Meta:
        app_label = 'rip_lab1'
        managed = False
        db_table = 'booking_requests' 
        verbose_name = "Бронивание"
        verbose_name_plural = "Бронирования"
#--------
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'books'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'