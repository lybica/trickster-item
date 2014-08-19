from django.db import models

from django.utils.translation import ugettext as _

import random

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
        (FIRE, 'Fire'),
        (WATER, 'Water'),
        (WIND, 'Wind'),
        (EARTH, 'Earth'),
        (ELEC, 'Elec'),
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
        (NOPROP, 'NoProp'),
        (PHYSICAL, 'Physical'),
        (GUN, 'Gun'),
        (SHADOW, 'Shadow'),
    )
    element = models.IntegerField(choices=ELEMENT_CHOICES)
    resist = models.BooleanField(default=False)

    @property
    def field(self):
        return '%s%s' % \
            (self.get_element_display(), 'R' if self.resist else '')

    def __unicode__(self):
        return _(self.field)


class ItemAttribute(models.Model):
    item = models.ForeignKey(Item)
    attr = models.ForeignKey(Attribute, default=None)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s %d' % \
            (unicode(self.item), unicode(self.attr), self.value)


class PresentItem(models.Model):
    item = models.OneToOneField(Item)
    ptype = models.IntegerField()
    count = models.IntegerField()

    def __unicode__(self):
        return unicode(self.item)

    def open(self):
        stat = self.dropitem_set.all()
        raffle = []
        received = []
        for s in stat:
            raffle += [s] * s.rate
        def pick(raffle, count):
            for n in xrange(count):
                picked = random.choice(raffle)
                yield [picked.drop] * picked.count
        return list(pick(raffle, self.count))

    def open_verbose(self):
        def verbose(itemsets):
            for itemset in itemsets:
                yield _('%(item)s %(count)d') % \
                    {'item': itemset[0], 'count': len(itemset)}
        return list(verbose(self.open()))


class DropItem(models.Model):
    item = models.ForeignKey(PresentItem)
    drop = models.ForeignKey(Item)
    rate = models.SmallIntegerField()
    count = models.IntegerField()

    def __unicode__(self):
        return '%s > %s(%d) %d' % \
            (unicode(self.item), unicode(self.drop), self.count, self.rate)
