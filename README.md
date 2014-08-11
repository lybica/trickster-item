# トリックスター アイテムデータ 初版

- `loaddata items.yaml` が通るハズですが、メモリ消費量がかなり多くなるのでおすすめしません。他の方法を考え中です…
- `class` と `type` は予約語なので、それぞれ `iclass` `itype` になっています。
- `DataType='Enum'` には `"1/2/4/8/16/32"` のようなデータが、オリジナルのまま `CharField(max_length=128)` に入っています。
 
- 属性・耐性(固定値)情報を追加

#### 使用例

```
>>> Item.objects.get(pk=40020)
<Item: 蒼剣フィルドザクス>
>>> _.itemattribute_set.all()
[<ItemAttribute: 蒼剣フィルドザクス Water 40>]

```
