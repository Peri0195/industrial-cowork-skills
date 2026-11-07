# 输入输出契约

任务：客户服务成本归集。

## 字段结构
以下字段均需提供，嵌套数组可增加同结构记录。数组需非空，ID不可重复；数值不接收字符串、布尔值、NaN或无穷大。非负和正值限制由脚本逐字段检查；允许负收益的payoff等字段另有处理。
```json
{
  "handling_rate": 5,
  "orders": [
    {
      "customer": "A",
      "units": 10,
      "direct_cost": 20,
      "handling_events": 2
    },
    {
      "customer": "A",
      "units": 10,
      "direct_cost": 30,
      "handling_events": 1
    }
  ]
}
```
字段名单位：minutes为分钟，hours为小时，days为天，kg为千克，m3为立方米，ton_km为吨公里，fraction及rate为小数比例（具体范围见方法）。amount、cost、payoff须使用同一种币种。日期为YYYY-MM-DD。

## 方法和边界
客户成本=sum(direct_cost+handling_events×handling_rate)；单位成本=客户成本/总件数。

只归集输入的成本项目；未提供的间接费用不自动分摊。

## 样例输出校验点
```json
{
  "customers": {
    "A": {
      "total_cost": 65,
      "units": 20,
      "cost_per_unit": 3.25
    }
  }
}
```
这里列出必验字段，完整结果可能包含额外明细。浮点数绝对/相对容差1e-8，字符串、布尔值、列表必须精确匹配。
脚本返回0表示计算成功并生成两份报告；返回2表示输入不合规并输出JSON错误，不生成新成功报告。请为每次调用使用新的输出目录，以免误读之前的结果。
