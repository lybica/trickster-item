from django.db import models

from django.utils.translation import ugettext as _

# Create your models here.

class Item(models.Model):
    iclass = models.IntegerField()
    itype = models.IntegerField()
    subtype = models.IntegerField()
    itemftype = models.IntegerField()
    name = models.CharField(max_length=64)
    comment = models.CharField(max_length=256)
    use = models.CharField(max_length=256)
    name_eng = models.CharField(max_length=64)
    comment_eng = models.CharField(max_length=64)
    filename = models.CharField(max_length=64)
    bundlenum = models.IntegerField()
    invfilename = models.CharField(max_length=64)
    invbundlenum = models.IntegerField()
    cmtfilename = models.CharField(max_length=64)
    cmtbundlenum = models.IntegerField()
    equipfilename = models.CharField(max_length=64)
    pivotid = models.IntegerField()
    paletteid = models.IntegerField()
    options = models.CharField(max_length=128)
    hidehat = models.CharField(max_length=128)
    chrtypeflags = models.CharField(max_length=128)
    groundflags = models.IntegerField()
    systemflags = models.IntegerField()
    optionsex = models.CharField(max_length=128)
    weight = models.IntegerField()
    value = models.IntegerField()
    minlevel = models.IntegerField()
    effect = models.CharField(max_length=128)
    effectflags2 = models.IntegerField()
    selrange = models.IntegerField()
    life = models.IntegerField()
    depth = models.IntegerField()
    delay = models.FloatField()
    ap = models.IntegerField()
    hp = models.IntegerField()
    hpcon = models.IntegerField()
    mp = models.IntegerField()
    mpcon = models.IntegerField()
    money = models.IntegerField()
    applus = models.IntegerField()
    acplus = models.IntegerField()
    dxplus = models.IntegerField()
    maxmpplus = models.IntegerField()
    maplus = models.IntegerField()
    mdplus = models.IntegerField()
    maxwtplus = models.IntegerField()
    daplus = models.IntegerField()
    lkplus = models.IntegerField()
    maxhpplus = models.IntegerField()
    dpplus = models.IntegerField()
    hvplus = models.IntegerField()
    hprecoveryrate = models.FloatField()
    mprecoveryrate = models.FloatField()
    cardnum = models.IntegerField()
    cardgengrade = models.IntegerField()
    cardgenparam = models.FloatField()
    dailygencnt = models.IntegerField()
    partfilename = models.CharField(max_length=64)
    chrftypeflag = models.CharField(max_length=128)
    chrgender = models.IntegerField()
    existtype = models.IntegerField()
    ncash = models.IntegerField()
    newcm = models.IntegerField()
    famcm = models.IntegerField()
    summary = models.CharField(max_length=64)
    shopfilename = models.CharField(max_length=64)
    shopbundlenum = models.IntegerField()
    minstattype = models.IntegerField()
    minstatlv = models.IntegerField()
    refineindex = models.IntegerField()
    refinetype = models.IntegerField()
    compoundslot = models.IntegerField()
    setitemid = models.IntegerField()
    reformcount = models.IntegerField()
    groupid = models.IntegerField()

    def __unicode__(self):
        return self.name


class Attribute(models.Model):
    FIRE = 1
    WATER = 2
    WIND = 3
    EARTH = 4
    ELEC = 5
    LIGHT = 6
    DARK = 7
    NOPROP = 8
    PHYSICAL = 9
    GUN = 10
    SHADOW = 11
    ELEMENT_CHOICES = (
        (FIRE, _('Fire')),
        (WATER, _('Water')),
        (WIND, _('Wind')),
        (EARTH, _('Earth')),
        (ELEC, _('Elec')),
        (LIGHT, _('Light')),
        (DARK, _('Dark')),
        (NOPROP, _('NoProp')),
        (PHYSICAL, _('Physical')),
        (GUN, _('Gun')),
        (SHADOW, _('Shadow')),
    )
    element = models.IntegerField(choices=ELEMENT_CHOICES)
    resist = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s%s' % \
            (self.get_element_display(), _('R') if self.resist else '')


class ItemAttribute(models.Model):
    item = models.ForeignKey(Item)
    attr = models.ForeignKey(Attribute, default=None)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s %d' % \
            (unicode(self.item), unicode(self.attr), self.value)
