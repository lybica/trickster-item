トリックスター アイテムデータ 初版

- `loaddata items.yaml` が通るハズですが、メモリ消費量がかなり多くなるのでおすすめしません。他の方法を考え中です…
- `class` と `type` は予約語なので、それぞれ `iclass` `itype` になっています。
- `DataType='Enum'` には `"1/2/4/8/16/32"` のようなデータが、オリジナルのまま `CharField(max_length=128)` に入っています。
