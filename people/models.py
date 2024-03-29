from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from base.models import Slugified


class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        if is_superuser:
            user_type = User.UT_ADMIN
        else:
            user_type = User.UT_PARENT

        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, user_type=user_type,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    UT_ADMIN = 0
    UT_HLV = 1
    UT_DOCTOR = 2
    UT_TUTOR = 3
    UT_PARENT = 4

    USER_TYPES = (
        (UT_ADMIN, _('Admin')),
        (UT_HLV, _('Main instructor')),
        (UT_DOCTOR, _('Doctor')),
        (UT_TUTOR, _('Tutor')),
        (UT_PARENT, _('Parent')),
    )

    USER_TYPES_DICT = dict(USER_TYPES)

    user_type = models.SmallIntegerField(_('User type'), choices=USER_TYPES,
                                         db_index=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('email', )

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    @property
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        full_name = self.get_full_name
        if full_name:
            return u'%s' % full_name
        else:
            return super(User, self).__unicode__()


class KidGroup(Slugified):

    class Meta:
        verbose_name = _('Kid group')
        verbose_name_plural = _('Kid groups')


class Kid(models.Model):
    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('Last name'), max_length=100)

    date_of_birth = models.DateField(_('Date of birth'), null=True, blank=True)

    non_swimmer = models.BooleanField(_('Non swimmer'), default=False)

    description = models.TextField(_('Description'), blank=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.date_of_birth)

    class Meta:
        verbose_name = _('Kid')
        verbose_name_plural = _('Kids')


class EntryMedicalCheck(models.Model):
    kid = models.ForeignKey(Kid)
    medicine = models.CharField(_('Medicine'), max_length=100, null=True, blank=True)
    dosage = models.CharField(_('Dosage'), max_length=50, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Entry medical check')
        verbose_name_plural = _('Entry medical checks')
