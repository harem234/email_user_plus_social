from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

"""related_name protocol for foreignKey
<from table name>_<to table name> """


class EmailUser(AbstractUser):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=False, blank=False, related_name="user_site",
                             default=Site.objects.get_current().pk, db_column='site')
    # new USERNAME_FIELD (email) must be overwrite and be required so: manage.py createsuperuser runs
    email = models.EmailField(
        _('email address'), unique=True, null=False, blank=False,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True, null=True,
        help_text=_('Optional. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
    )

    isEmailVerified = models.BooleanField(blank=False, null=False, default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email.lower()
