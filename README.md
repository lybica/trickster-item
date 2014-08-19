# トリックスター アイテムデータ 初版

- Django 1.7 + Python 2.7

- `loaddata items.yaml` が通るハズですが、メモリ消費量がかなり多くなるのでおすすめしません。他の方法を考え中です…
- `class` と `type` は予約語なので、それぞれ `iclass` `itype` になっています。
- `DataType='Enum'` には `"1/2/4/8/16/32"` のようなデータが、オリジナルのまま `CharField(max_length=128)` に入っています。
 
- 属性・耐性(固定値)情報を追加
- 鬱箱の中身を追加
- 鬱箱「開封」テスト

#### 使用例

```
>>> Item.objects.get(pk=40020)
<Item: 蒼剣フィルドザクス>
>>> _.itemattribute_set.all()
[<ItemAttribute: 蒼剣フィルドザクス Water 40>]
```
```
>>> box = Item.objects.get(pk=431055)
>>> box
<Item: ラブチョコレートボックス>
>>> box.presentitem
<PresentItem: ラブチョコレートボックス>
>>> [d.drop for d in box.presentitem.dropitem_set.all()]
[<Item: ラブハンター>, <Item: ソレイユ>, <Item: ハッピーバレンタイン>,
<Item: 口溶けチョコレートドリンク>, <Item: 本命チョコ>, <Item: 義理チョコ>,
<Item: ブラックチョコレート>]
```
```
>>> fron django.utils import translation as l10n
>>> l10n.activate('ja')
>>> box = PresentItem.objects.get(item__name='専用パラベンスボックスダブル')
>>> print '\n'.join(box.open_verbose())
(倉庫拡張チケット : 1個) を手に入れた！
(ライトピンクポーション : 20個) を手に入れた！
```
