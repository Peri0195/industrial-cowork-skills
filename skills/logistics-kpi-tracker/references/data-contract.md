# 输入输出契约

任务：到货及时足量率核算。

## 字段结构
以下字段均需提供，嵌套数组可增加同结构记录。数组需非空，ID不可重复；数值不接收字符串、布尔值、NaN或无穷大。非负和正值限制由脚本逐字段检查；允许负收益的payoff等字段另有处理。
```json
{
  "orders": [
    {
      "id": "1",
      "on_time": true,
      "in_full": true
    },
    {
      "id": "2",
      "on_time": true,
      "in_full": false
    },
    {
      "id": "3",
      "on_time": false,
      "in_full": true
    },
    {
      "id": "4",
      "on_time": true,
      "in_full": true
    }
  ]
}
```
字段名单位：minutes为分钟，hours为小时，days为天，kg为千克，m3为立方米，ton_km为吨公里，fraction及rate为小数比例（具体范围见方法）。amount、cost、payoff须使用同一种币种。日期为YYYY-MM-DD。

## 方法和边界
OTIF以同一订单同时满足on_time和in_full为分子；不能把两个比例直接相乘。

准时窗口和足量口径由业务方先确认；不连接物流平台。

## 样例输出校验点
```json
{
  "on_time_pct": 75,
  "in_full_pct": 75,
  "otif_pct": 50
}
```
这里列出必验字段，完整结果可能包含额外明细。浮点数绝对/相对容差1e-8，字符串、布尔值、列表必须精确匹配。
脚本返回0表示计算成功并生成两份报告；返回2表示输入不合规并输出JSON错误，不生成新成功报告。请为每次调用使用新的输出目录，以免误读之前的结果。
