from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site


class SocialProvider(models.Model):
    SENTINEL = 'sentinel'
    GOOGLE = 'google'
    GITHUB = 'github'
    Social_List = [
        (None, 'Select Provider'),
        (GOOGLE, 'Google'),
        (GITHUB, 'Github'),

        # for deleted provider of SocialAccount instances
        (SENTINEL, 'sentinel'),
    ]
    social = models.CharField(
        unique=True,
        max_length=10,
        choices=Social_List,
        null=False,
        blank=False, )

    client_id = models.CharField(blank=False, null=False, max_length=1000)

    def __str__(self):
        return self.social

    class Meta:
        verbose_name = 'Social Provider'
        verbose_name_plural = 'Social Providers'


def get_sentinel_social_provider():
    """:return sentinel of SocialProvider Model"""
    return SocialProvider.objects.get_or_create(social=SocialProvider.SENTINEL, defaults={'client_id': ''})[0]


class SocialAccount(models.Model):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=False, blank=False,
                             related_name="socialaccount_site", default=Site.objects.get_current)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,
                             related_name="socialaccount_user")

    # on_delete: do Not delete social accounts on deleting a provider
    provider = models.ForeignKey(
        to=SocialProvider, on_delete=models.SET(get_sentinel_social_provider),
        blank=False, null=False)

    social_provider_identifier = models.CharField(blank=False, null=False, max_length=1000, )
    is_connected = models.BooleanField(null=False, blank=False, default=False, )

    email = models.EmailField(blank=False, null=True, max_length=1000, unique=True, )

    def __str__(self):
        return self.email + "::" + self.provider.social + "::" + self.user.email

    class Meta:
        verbose_name = 'Social Account'
        verbose_name_plural = 'Social Accounts'
        # ensures for a user there is only one account per provider and per site at most
        constraints = [
            models.UniqueConstraint(fields=['user', 'provider', 'site'],
                                    name='user have one account per provider and site'),
            models.UniqueConstraint(fields=['social_provider_identifier', 'provider', 'site'],
                                    name='every social_provider_identifier per provider is unique for every site'),
        ]
