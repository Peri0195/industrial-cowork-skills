# 工业 Cowork 技能目录

本批含30个独立技能包，完整保留上游说明，并增加中文入口与范围明确的离线执行脚本。

## 下载与导入
- [Excel沉淀清单](catalog/batch-01.xlsx)：与第二轮模板对应的列，填写人留空；第二张表含ZIP下载地址、来源、范围和验证状态。
- [独立ZIP目录](downloads)：每个ZIP只有一个技能。MEA Cowork中选择“从ZIP文件安装”。不要把整个仓库ZIP当成批量导入包。
- [技能目录](skills)：可查看SKILL.md、完整来源说明、脚本和样例。

## 状态
OEE已由用户在MEA导入及调用，实际产物已核对。其余29项有既有本地测试记录，但未进行MEA逐项导入与调用验证。按用户后续要求停止进一步验证；不得据此宣称全部平台验证通过。
新增脚本实现范围以各技能中文SKILL.md和输入契约为准，上游完整说明中的扩展能力并非全部实现。第一批侧重生产效率、仓储物流和供应链离线核算，后续批次另行追加。

## 来源与授权
上游来自a5c-ai/babysitter，固定提交与文件哈希保存在每项source.json。上游MIT许可证及版权声明保留。新增适配的许可证见各目录LICENSE；OEE沿用样板授权文件。未上传用户参考清单、公司内部文档、API密钥或本机账户凭据。

## 第一批目录
|序号|中文名称|技能目录|ZIP下载|
|---|---|---|---|
|1|设备综合效率计算与损失核对|[oee-calculator](skills/oee-calculator)|[下载](downloads/oee-calculator.zip?raw=true)|
|2|生产需求节拍核算|[takt-time-calculator](skills/takt-time-calculator)|[下载](downloads/takt-time-calculator.zip?raw=true)|
|3|工时观测与标准时间核算|[time-study-analyzer](skills/time-study-analyzer)|[下载](downloads/time-study-analyzer.zip?raw=true)|
|4|作业抽样利用率估计|[work-sampling-analyzer](skills/work-sampling-analyzer)|[下载](downloads/work-sampling-analyzer.zip?raw=true)|
|5|既定工位分配平衡率核算|[line-balancer](skills/line-balancer)|[下载](downloads/line-balancer.zip?raw=true)|
|6|换型内外作业改善核算|[smed-analyzer](skills/smed-analyzer)|[下载](downloads/smed-analyzer.zip?raw=true)|
|7|缺陷类别帕累托排序|[pareto-analyzer](skills/pareto-analyzer)|[下载](downloads/pareto-analyzer.zip?raw=true)|
|8|5S现场检查得分汇总|[five-s-auditor](skills/five-s-auditor)|[下载](downloads/five-s-auditor.zip?raw=true)|
|9|单服务台排队指标估计|[queuing-analyzer](skills/queuing-analyzer)|[下载](downloads/queuing-analyzer.zip?raw=true)|
|10|风险中性方案期望值比较|[decision-tree-analyzer](skills/decision-tree-analyzer)|[下载](downloads/decision-tree-analyzer.zip?raw=true)|
|11|既定厂内布局搬运负荷比较|[facility-layout-optimizer](skills/facility-layout-optimizer)|[下载](downloads/facility-layout-optimizer.zip?raw=true)|
|12|库存价值与需求波动分类|[abc-xyz-classifier](skills/abc-xyz-classifier)|[下载](downloads/abc-xyz-classifier.zip?raw=true)|
|13|循环盘点到期清单|[cycle-count-scheduler](skills/cycle-count-scheduler)|[下载](downloads/cycle-count-scheduler.zip?raw=true)|
|14|库存久未动用识别|[dead-stock-identifier](skills/dead-stock-identifier)|[下载](downloads/dead-stock-identifier.zip?raw=true)|
|15|批次出库顺序分配|[fifo-lifo-controller](skills/fifo-lifo-controller)|[下载](downloads/fifo-lifo-controller.zip?raw=true)|
|16|运费账单与约定单价核对|[freight-audit-validator](skills/freight-audit-validator)|[下载](downloads/freight-audit-validator.zip?raw=true)|
|17|车辆载重容积利用率核对|[load-optimization-calculator](skills/load-optimization-calculator)|[下载](downloads/load-optimization-calculator.zip?raw=true)|
|18|到货及时足量率核算|[logistics-kpi-tracker](skills/logistics-kpi-tracker)|[下载](downloads/logistics-kpi-tracker.zip?raw=true)|
|19|固定提前期安全库存估计|[safety-stock-calculator](skills/safety-stock-calculator)|[下载](downloads/safety-stock-calculator.zip?raw=true)|
|20|拣选频次与库位优先匹配|[slotting-optimization-engine](skills/slotting-optimization-engine)|[下载](downloads/slotting-optimization-engine.zip?raw=true)|
|21|承运商运输费用汇总|[transportation-spend-analyzer](skills/transportation-spend-analyzer)|[下载](downloads/transportation-spend-analyzer.zip?raw=true)|
|22|需求预测误差核算|[forecast-accuracy-analyzer](skills/forecast-accuracy-analyzer)|[下载](downloads/forecast-accuracy-analyzer.zip?raw=true)|
|23|供应商加权评分核算|[supplier-scorecard-engine](skills/supplier-scorecard-engine)|[下载](downloads/supplier-scorecard-engine.zip?raw=true)|
|24|设备持有期成本现值核算|[tco-calculator](skills/tco-calculator)|[下载](downloads/tco-calculator.zip?raw=true)|
|25|客户服务成本归集|[cost-to-serve-analyzer](skills/cost-to-serve-analyzer)|[下载](downloads/cost-to-serve-analyzer.zip?raw=true)|
|26|串联工序瓶颈能力核算|[capacity-constraint-analyzer](skills/capacity-constraint-analyzer)|[下载](downloads/capacity-constraint-analyzer.zip?raw=true)|
|27|DDMRP缓冲区参数核算|[ddmrp-buffer-manager](skills/ddmrp-buffer-manager)|[下载](downloads/ddmrp-buffer-manager.zip?raw=true)|
|28|物料主数据缺项与重复检查|[master-data-quality-manager](skills/master-data-quality-manager)|[下载](downloads/master-data-quality-manager.zip?raw=true)|
|29|仓库作业人时需求核算|[labor-productivity-optimizer](skills/labor-productivity-optimizer)|[下载](downloads/labor-productivity-optimizer.zip?raw=true)|
|30|运输活动排放因子核算|[carbon-footprint-calculator](skills/carbon-footprint-calculator)|[下载](downloads/carbon-footprint-calculator.zip?raw=true)|

## 第二批：原作者公开技能链接（31—60）

[第二批Excel](catalog/batch-02.xlsx) · [技能目录与说明](catalog/batch-02.md)

第二批保留原作者链接，来源为公网下载，不包含自建ZIP。无需为这些技能新建仓库。
