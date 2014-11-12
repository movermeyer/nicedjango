from django.db import models


class Abstract(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        app_label = 'a2'
        abstract = True


class Real(Abstract):
    pass

# TODO:
# class ProxyManager(models.Manager):
#    def get_queryset(self):
#        return QuerySet(self.model).filter(name__startswith='proxy')


class Proxy(Real):
    #    objects = ProxyManager()

    class Meta:
        app_label = 'a2'
        proxy = True


class Sub(Real):
    pass


class SubSub(Sub):
    pass


class Foreign(Abstract):
    f = models.ForeignKey(Real, null=True)


class OneToOne(Abstract):
    r = models.OneToOneField(Real, null=True)
    s = models.OneToOneField('self', null=True)


class ManyToMany(Abstract):
    m = models.ManyToManyField(Real)
    s = models.ManyToManyField('self')
