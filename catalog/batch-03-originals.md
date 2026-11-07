# 第三批完整原始说明

以下保留已采集的原作者 SKILL.md 全文，按原样引用；不是新编技能包。来源版本与原链接列于各条目前。中文摘要见Excel。

## 61 · 地基承载力计算辅助

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/bearing-capacity-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/bearing-capacity-calculator/SKILL.md

``````markdown
---
name: bearing-capacity-calculator
description: Soil bearing capacity calculation skill using multiple methods for various foundation types
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-008
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Bearing Capacity Calculator Skill

## Purpose

The Bearing Capacity Calculator Skill determines ultimate and allowable bearing capacity for foundations using established geotechnical methods including Terzaghi, Meyerhof, Hansen, and Vesic.

## Capabilities

- Ultimate bearing capacity calculation
- Allowable bearing capacity with factor of safety
- Effect of groundwater
- Eccentric and inclined loads
- Layered soil bearing capacity
- Settlement-based bearing capacity
- Shape, depth, and inclination factors
- Bearing capacity for footings on slopes

## Usage Guidelines

### When to Use
- Designing shallow foundations
- Evaluating foundation bearing
- Checking settlement limits
- Analyzing eccentric loading

### Prerequisites
- Soil parameters available
- Foundation dimensions defined
- Groundwater level known
- Load conditions established

### Best Practices
- Use appropriate analysis method
- Consider all failure modes
- Apply suitable safety factors
- Verify with settlement analysis

## Process Integration

This skill integrates with:
- Foundation Design
- Geotechnical Site Investigation

## Configuration

```yaml
bearing-capacity-calculator:
  methods:
    - terzaghi
    - meyerhof
    - hansen
    - vesic
  foundation-types:
    - spread
    - strip
    - mat
  considerations:
    - groundwater
    - eccentricity
    - inclination
```

## Output Artifacts

- Bearing capacity calculations
- Safety factor summaries
- Settlement predictions
- Recommendation reports

``````

## 62 · BIM专业碰撞协调

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/bim-clash-detection

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/bim-clash-detection/SKILL.md

``````markdown
---
name: bim-clash-detection
description: BIM clash detection skill for identifying and managing coordination conflicts between disciplines
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: BIM Coordination
  skill-id: CIV-SK-014
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# BIM Clash Detection Skill

## Purpose

The BIM Clash Detection Skill identifies and manages coordination conflicts between building disciplines including hard clashes, soft clashes, and workflow clashes.

## Capabilities

- Hard clash detection (physical interference)
- Soft clash detection (clearance violations)
- Workflow clash detection (sequencing)
- Clash grouping and prioritization
- Resolution tracking
- Report generation with visualization
- BCF format export
- Multi-model coordination

## Usage Guidelines

### When to Use
- Coordinating multi-discipline models
- Identifying design conflicts
- Managing clash resolution
- Documenting coordination issues

### Prerequisites
- BIM models available
- Coordination matrix defined
- Tolerance settings established
- Resolution workflow defined

### Best Practices
- Run regular detection cycles
- Prioritize clashes by impact
- Track resolution status
- Document resolutions

## Process Integration

This skill integrates with:
- BIM Coordination
- Shop Drawing Review

## Configuration

```yaml
bim-clash-detection:
  clash-types:
    - hard
    - soft
    - clearance
  tolerances:
    hard: 0
    soft: 50  # mm
    clearance: 100  # mm
  output-formats:
    - html
    - bcf
    - json
```

## Output Artifacts

- Clash reports
- BCF issue files
- Resolution logs
- Coordination matrices

``````

## 63 · Civil 3D地形曲面分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/civil3d-surface-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/civil3d-surface-analyzer/SKILL.md

``````markdown
---
name: civil3d-surface-analyzer
description: Civil 3D surface analysis skill for terrain modeling, earthwork, and drainage analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Site Design
  skill-id: CIV-SK-017
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Civil 3D Surface Analyzer Skill

## Purpose

The Civil 3D Surface Analyzer Skill performs terrain surface analysis including slope analysis, cut/fill calculations, drainage analysis, and earthwork quantity computation.

## Capabilities

- Surface analysis (slope, elevation, contours)
- Cut/fill volume calculation
- Drainage analysis
- Corridor modeling
- Cross-section generation
- Earthwork quantities
- Surface comparison
- Watershed delineation

## Usage Guidelines

### When to Use
- Analyzing site topography
- Calculating earthwork volumes
- Evaluating drainage patterns
- Designing corridors

### Prerequisites
- Survey data available
- Surface model created
- Design criteria defined
- Section intervals established

### Best Practices
- Verify surface accuracy
- Use appropriate comparison methods
- Consider shrink/swell factors
- Document calculation methods

## Process Integration

This skill integrates with:
- Highway Geometric Design
- Stormwater Management Design
- Slope Stability Analysis

## Configuration

```yaml
civil3d-surface-analyzer:
  analysis-types:
    - slope
    - elevation
    - drainage
    - volumes
  surface-types:
    - existing
    - proposed
    - corridor
  output-formats:
    - report
    - xml
    - csv
```

## Output Artifacts

- Surface analysis maps
- Volume reports
- Drainage diagrams
- Cross-sections

``````

## 64 · 钢筋混凝土构件设计辅助

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/concrete-design-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/concrete-design-calculator/SKILL.md

``````markdown
---
name: concrete-design-calculator
description: Reinforced concrete design skill for flexure, shear, and serviceability calculations per ACI 318
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Structural Design
  skill-id: CIV-SK-006
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Concrete Design Calculator Skill

## Purpose

The Concrete Design Calculator Skill performs reinforced concrete design calculations for beams, slabs, and columns per ACI 318 including flexure, shear, torsion, and serviceability checks.

## Capabilities

- Flexural design (beams, slabs, columns)
- Shear and torsion design
- Development length calculations
- Crack width calculations
- Deflection calculations (immediate and long-term)
- ACI 318 code compliance checking
- Interaction diagrams for columns
- Slenderness effects analysis

## Usage Guidelines

### When to Use
- Designing reinforced concrete members
- Checking serviceability requirements
- Evaluating existing concrete structures
- Determining reinforcement requirements

### Prerequisites
- Member geometry defined
- Loads and moments established
- Material properties specified
- Exposure conditions identified

### Best Practices
- Check both strength and serviceability
- Consider construction tolerances
- Verify bar spacing and cover
- Document all design assumptions

## Process Integration

This skill integrates with:
- Reinforced Concrete Design
- Foundation Design
- Bridge Design LRFD

## Configuration

```yaml
concrete-design-calculator:
  design-types:
    - flexure
    - shear
    - torsion
    - columns
    - development
  serviceability:
    - deflection
    - crack-width
  design-codes:
    - ACI-318-19
    - ACI-318-14
```

## Output Artifacts

- Design calculations
- Reinforcement schedules
- Interaction diagrams
- Deflection reports

``````

## 65 · 施工关键路径进度编排

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/cpm-schedule-generator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/cpm-schedule-generator/SKILL.md

``````markdown
---
name: cpm-schedule-generator
description: Critical Path Method scheduling skill for construction schedule development and analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Construction Management
  skill-id: CIV-SK-027
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# CPM Schedule Generator Skill

## Purpose

The CPM Schedule Generator Skill develops construction schedules using Critical Path Method including activity sequencing, float analysis, and resource leveling.

## Capabilities

- Critical path calculation
- Float analysis (total, free, independent)
- Resource leveling
- Schedule compression
- Gantt chart generation
- Progress tracking
- Baseline comparison
- What-if analysis

## Usage Guidelines

### When to Use
- Developing project schedules
- Analyzing schedule impacts
- Tracking project progress
- Evaluating alternatives

### Prerequisites
- Activity list defined
- Duration estimates available
- Logic relationships established
- Resource constraints identified

### Best Practices
- Use realistic durations
- Verify logic relationships
- Identify driving paths
- Update regularly

## Process Integration

This skill integrates with:
- Construction Schedule Development

## Configuration

```yaml
cpm-schedule-generator:
  analysis-types:
    - forward-pass
    - backward-pass
    - float-analysis
    - resource-leveling
  outputs:
    - gantt-chart
    - network-diagram
    - reports
```

## Output Artifacts

- Project schedules
- Critical path reports
- Float analyses
- Resource histograms

``````

## 66 · 挡土结构土压力分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/earth-pressure-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/earth-pressure-calculator/SKILL.md

``````markdown
---
name: earth-pressure-calculator
description: Earth pressure calculation skill for retaining structures using classical and seismic methods
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-012
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Earth Pressure Calculator Skill

## Purpose

The Earth Pressure Calculator Skill determines lateral earth pressures on retaining structures using Rankine, Coulomb, and seismic methods for design of retaining walls and basement walls.

## Capabilities

- Active earth pressure (Rankine, Coulomb)
- Passive earth pressure
- At-rest earth pressure
- Surcharge effects
- Layered soil conditions
- Seismic earth pressure (Mononobe-Okabe)
- Sloping backfill effects
- Water pressure considerations

## Usage Guidelines

### When to Use
- Designing retaining walls
- Analyzing basement walls
- Evaluating excavation support
- Assessing seismic pressures

### Prerequisites
- Soil parameters available
- Wall geometry defined
- Surcharge loads identified
- Groundwater level known

### Best Practices
- Select appropriate theory
- Consider wall movement
- Include seismic where required
- Account for drainage

## Process Integration

This skill integrates with:
- Retaining Wall Design
- Foundation Design

## Configuration

```yaml
earth-pressure-calculator:
  theories:
    - rankine
    - coulomb
    - log-spiral
  pressure-states:
    - active
    - passive
    - at-rest
  seismic:
    - mononobe-okabe
    - wood
```

## Output Artifacts

- Pressure diagrams
- Force calculations
- Moment summaries
- Seismic increment values

``````

## 67 · 工程GIS空间分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/gis-spatial-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/gis-spatial-analyzer/SKILL.md

``````markdown
---
name: gis-spatial-analyzer
description: GIS spatial analysis skill for watershed delineation, floodplain mapping, and site analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: GIS
  skill-id: CIV-SK-034
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# GIS Spatial Analyzer Skill

## Purpose

The GIS Spatial Analyzer Skill performs spatial analysis including watershed delineation, floodplain mapping, buffer analysis, and land use classification.

## Capabilities

- Watershed delineation
- Floodplain mapping
- Buffer analysis
- Slope analysis
- Land use classification
- Right-of-way analysis
- Viewshed analysis
- Proximity analysis

## Usage Guidelines

### When to Use
- Analyzing site constraints
- Delineating watersheds
- Mapping flood zones
- Evaluating land use

### Prerequisites
- GIS data available
- DEM for terrain analysis
- Boundary data defined
- Analysis criteria established

### Best Practices
- Use appropriate resolution
- Verify data sources
- Document methodology
- Validate results

## Process Integration

This skill integrates with:
- Flood Analysis and Mitigation
- Stormwater Management Design
- Highway Geometric Design

## Configuration

```yaml
gis-spatial-analyzer:
  analysis-types:
    - watershed
    - flood
    - buffer
    - slope
    - land-use
  data-sources:
    - DEM
    - parcel
    - FEMA
    - NLCD
```

## Output Artifacts

- Watershed maps
- Floodplain delineations
- Buffer zones
- Analysis reports

``````

## 68 · 道路平纵线形设计

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/highway-alignment-designer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/highway-alignment-designer/SKILL.md

``````markdown
---
name: highway-alignment-designer
description: Highway alignment design skill for horizontal and vertical geometry per AASHTO standards
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Transportation Design
  skill-id: CIV-SK-018
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Highway Alignment Designer Skill

## Purpose

The Highway Alignment Designer Skill designs horizontal and vertical highway alignments including curves, superelevation, and sight distance per AASHTO Green Book standards.

## Capabilities

- Horizontal curve design (simple, compound, reverse, spiral)
- Vertical curve design (crest, sag)
- Superelevation calculation
- Sight distance analysis
- Cross-section template generation
- AASHTO Green Book compliance checking
- Design exception documentation
- Corridor modeling support

## Usage Guidelines

### When to Use
- Designing new roadways
- Evaluating existing alignments
- Checking sight distances
- Developing superelevation

### Prerequisites
- Design speed established
- Terrain classification known
- Design criteria selected
- Survey data available

### Best Practices
- Coordinate H and V alignment
- Verify sight distances
- Consider driver expectations
- Document any exceptions

## Process Integration

This skill integrates with:
- Highway Geometric Design
- Bridge Design LRFD

## Configuration

```yaml
highway-alignment-designer:
  curve-types:
    - simple
    - compound
    - reverse
    - spiral
  standards:
    - AASHTO
    - state-DOT
  output-formats:
    - xml
    - landxml
    - csv
```

## Output Artifacts

- Alignment geometry
- Superelevation diagrams
- Sight distance reports
- Design summaries

``````

## 69 · 明渠涵洞与管网水力分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/hydraulic-analysis-engine

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/hydraulic-analysis-engine/SKILL.md

``````markdown
---
name: hydraulic-analysis-engine
description: Hydraulic analysis skill for open channel flow, culverts, and pipe networks
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Water Resources
  skill-id: CIV-SK-023
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Hydraulic Analysis Engine Skill

## Purpose

The Hydraulic Analysis Engine Skill performs hydraulic analysis for open channels, culverts, and pipe networks using Manning's equation and energy-momentum principles.

## Capabilities

- Open channel flow (Manning's equation)
- Culvert hydraulics (inlet/outlet control)
- Pipe network analysis
- Energy and momentum calculations
- Backwater analysis
- Spillway design calculations
- Critical and normal depth
- Gradually varied flow

## Usage Guidelines

### When to Use
- Sizing drainage structures
- Analyzing channel capacity
- Evaluating flood elevations
- Designing spillways

### Prerequisites
- Channel geometry defined
- Flow rates established
- Boundary conditions known
- Roughness values selected

### Best Practices
- Verify Manning's n values
- Check flow regime
- Consider tailwater effects
- Validate with observations

## Process Integration

This skill integrates with:
- Hydraulic Structure Design
- Stormwater Management Design
- Flood Analysis and Mitigation

## Configuration

```yaml
hydraulic-analysis-engine:
  analysis-types:
    - open-channel
    - culvert
    - pipe-network
    - spillway
  flow-types:
    - steady
    - unsteady
    - uniform
    - varied
```

## Output Artifacts

- Water surface profiles
- Culvert analysis
- Network solutions
- Energy grade lines

``````

## 70 · 降雨径流与洪水分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/hydrologic-modeling-engine

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/hydrologic-modeling-engine/SKILL.md

``````markdown
---
name: hydrologic-modeling-engine
description: Hydrologic modeling skill for rainfall-runoff analysis, flood frequency, and watershed analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Water Resources
  skill-id: CIV-SK-022
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Hydrologic Modeling Engine Skill

## Purpose

The Hydrologic Modeling Engine Skill performs hydrologic analysis including rainfall-runoff modeling, flood frequency analysis, and watershed characterization using established methods.

## Capabilities

- Rational method calculations
- SCS/NRCS curve number method
- Unit hydrograph generation
- Reservoir routing
- Time of concentration calculation
- IDF curve analysis
- Flood frequency analysis
- Watershed delineation

## Usage Guidelines

### When to Use
- Estimating design flows
- Analyzing watersheds
- Designing stormwater facilities
- Evaluating flood risk

### Prerequisites
- Watershed characteristics known
- Rainfall data available
- Land use identified
- Soil types classified

### Best Practices
- Select appropriate method
- Validate with observed data
- Consider climate effects
- Document assumptions

## Process Integration

This skill integrates with:
- Stormwater Management Design
- Flood Analysis and Mitigation
- Hydraulic Structure Design

## Configuration

```yaml
hydrologic-modeling-engine:
  methods:
    - rational
    - scs-curve-number
    - unit-hydrograph
    - reservoir-routing
  outputs:
    - peak-flow
    - hydrograph
    - report
```

## Output Artifacts

- Peak flow calculations
- Hydrographs
- Watershed reports
- Routing analyses

``````

## 71 · IFC工程模型信息分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/ifc-model-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/ifc-model-analyzer/SKILL.md

``````markdown
---
name: ifc-model-analyzer
description: IFC model analysis skill for validation, property extraction, and model comparison
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: BIM Coordination
  skill-id: CIV-SK-015
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# IFC Model Analyzer Skill

## Purpose

The IFC Model Analyzer Skill analyzes IFC format BIM models for schema validation, property extraction, quantity takeoff, and model comparison.

## Capabilities

- IFC schema validation
- Property set extraction
- Quantity takeoff
- Model comparison (diff)
- Element classification
- Coordinate system analysis
- LOD assessment
- Data quality checking

## Usage Guidelines

### When to Use
- Validating IFC exports
- Extracting model data
- Comparing model versions
- Checking data quality

### Prerequisites
- IFC file available
- Schema version identified
- Extraction requirements defined
- Comparison baseline established

### Best Practices
- Validate schema compliance
- Check coordinate systems
- Verify property mapping
- Document model assumptions

## Process Integration

This skill integrates with:
- BIM Coordination
- Structural Peer Review

## Configuration

```yaml
ifc-model-analyzer:
  analysis-types:
    - validation
    - extraction
    - comparison
    - quality-check
  ifc-versions:
    - IFC2x3
    - IFC4
    - IFC4.3
  outputs:
    - report
    - json
    - csv
```

## Output Artifacts

- Validation reports
- Property extractions
- Model comparisons
- Quality assessments

``````

## 72 · 道路路面结构设计辅助

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/pavement-design-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/pavement-design-calculator/SKILL.md

``````markdown
---
name: pavement-design-calculator
description: Pavement design skill for flexible and rigid pavements using AASHTO and MEPDG methods
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Transportation Design
  skill-id: CIV-SK-020
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Pavement Design Calculator Skill

## Purpose

The Pavement Design Calculator Skill designs flexible and rigid pavements using AASHTO 93, MEPDG, and other established methods including overlay design and life-cycle cost analysis.

## Capabilities

- Flexible pavement design (AASHTO 93, MEPDG)
- Rigid pavement design
- Overlay design
- Traffic loading analysis (ESALs)
- Material characterization
- Life-cycle cost analysis
- Structural number calculation
- Thickness determination

## Usage Guidelines

### When to Use
- Designing new pavements
- Evaluating rehabilitation options
- Analyzing pavement life
- Comparing alternatives

### Prerequisites
- Traffic data available
- Subgrade characterization complete
- Material properties known
- Design period established

### Best Practices
- Use appropriate design method
- Verify traffic projections
- Consider drainage effects
- Evaluate life-cycle costs

## Process Integration

This skill integrates with:
- Pavement Design
- Highway Geometric Design

## Configuration

```yaml
pavement-design-calculator:
  design-methods:
    - AASHTO-93
    - MEPDG
    - PCA
  pavement-types:
    - flexible
    - rigid
    - composite
  analysis:
    - new-construction
    - overlay
    - rehabilitation
```

## Output Artifacts

- Pavement thickness designs
- Life-cycle cost analyses
- Material specifications
- Design summaries

``````

## 73 · 桩基础承载力分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/pile-capacity-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/pile-capacity-analyzer/SKILL.md

``````markdown
---
name: pile-capacity-analyzer
description: Deep foundation capacity analysis skill for driven piles and drilled shafts
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-011
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Pile Capacity Analyzer Skill

## Purpose

The Pile Capacity Analyzer Skill determines axial and lateral capacity of deep foundations including driven piles and drilled shafts using FHWA and other established methods.

## Capabilities

- Driven pile capacity (alpha, beta methods)
- Drilled shaft capacity (FHWA methods)
- Pile group efficiency
- Lateral pile analysis (p-y curves)
- Pile driving analysis (wave equation)
- LRFD resistance factors
- Uplift capacity
- Settlement of pile groups

## Usage Guidelines

### When to Use
- Designing deep foundations
- Analyzing pile group behavior
- Evaluating lateral capacity
- Predicting pile driving

### Prerequisites
- Soil borings available
- Pile type and size selected
- Load requirements defined
- Installation method determined

### Best Practices
- Use appropriate method for soil type
- Consider setup and relaxation
- Apply LRFD resistance factors
- Plan for verification testing

## Process Integration

This skill integrates with:
- Foundation Design
- Bridge Design LRFD

## Configuration

```yaml
pile-capacity-analyzer:
  pile-types:
    - driven-steel
    - driven-concrete
    - drilled-shaft
    - micropile
  capacity-methods:
    - alpha
    - beta
    - nordlund
    - FHWA-drilled
  lateral-methods:
    - p-y-curves
    - Broms
```

## Output Artifacts

- Capacity calculations
- Load-settlement curves
- p-y analysis results
- Group efficiency factors

``````

## 74 · 结构截面几何特性计算

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/section-property-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/section-property-calculator/SKILL.md

``````markdown
---
name: section-property-calculator
description: Cross-sectional property calculation skill for structural sections including standard and custom shapes
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Structural Analysis
  skill-id: CIV-SK-002
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Section Property Calculator Skill

## Purpose

The Section Property Calculator Skill calculates cross-sectional properties for structural sections including area, moment of inertia, section modulus, and plastic modulus for both standard and custom shapes.

## Capabilities

- Calculate cross-sectional properties (A, I, S, Z, r)
- Support for standard shapes (W, HSS, C, L, pipe)
- Custom section analysis
- Composite section properties
- Cracked section analysis for concrete
- Plastic section modulus calculation
- Effective section properties
- Built-up section analysis

## Usage Guidelines

### When to Use
- Determining section properties for design
- Analyzing composite sections
- Evaluating cracked concrete sections
- Designing built-up members

### Prerequisites
- Section geometry defined
- Material properties specified
- Cracking criteria established (for concrete)
- Effective width defined (for composites)

### Best Practices
- Use correct axis orientation
- Account for holes and penetrations
- Consider effective sections per code
- Verify against published values

## Process Integration

This skill integrates with:
- Reinforced Concrete Design
- Structural Steel Design
- Bridge Design LRFD

## Configuration

```yaml
section-property-calculator:
  standard-shapes:
    - W-shapes
    - HSS-rectangular
    - HSS-round
    - channels
    - angles
    - pipes
  analysis-types:
    - gross
    - net
    - effective
    - cracked
```

## Output Artifacts

- Section property tables
- Cross-section drawings
- Calculation summaries
- Composite section analysis

``````

## 75 · 基础沉降分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/settlement-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/settlement-calculator/SKILL.md

``````markdown
---
name: settlement-calculator
description: Foundation settlement calculation skill for immediate, consolidation, and secondary compression
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-010
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Settlement Calculator Skill

## Purpose

The Settlement Calculator Skill calculates foundation settlements including immediate (elastic) settlement, primary consolidation, and secondary compression using established geotechnical methods.

## Capabilities

- Immediate (elastic) settlement
- Consolidation settlement (1D theory)
- Secondary compression
- Time-rate of consolidation
- Differential settlement analysis
- Tolerable settlement checks
- Settlement beneath rigid foundations
- Stress distribution calculations

## Usage Guidelines

### When to Use
- Estimating foundation settlement
- Evaluating differential settlement
- Time-rate predictions
- Tolerable settlement verification

### Prerequisites
- Soil compressibility data available
- Foundation loads defined
- Groundwater conditions known
- Soil stratigraphy established

### Best Practices
- Use appropriate stress distribution
- Consider soil variability
- Account for adjacent structures
- Verify with field monitoring

## Process Integration

This skill integrates with:
- Foundation Design
- Geotechnical Site Investigation

## Configuration

```yaml
settlement-calculator:
  settlement-types:
    - immediate
    - consolidation
    - secondary
  methods:
    - elastic
    - terzaghi-1d
    - stress-history
  output:
    - magnitude
    - time-rate
    - differential
```

## Output Artifacts

- Settlement calculations
- Time-settlement curves
- Differential settlement maps
- Tolerable settlement checks

``````

## 76 · 边坡稳定性分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/slope-stability-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/slope-stability-analyzer/SKILL.md

``````markdown
---
name: slope-stability-analyzer
description: Slope stability analysis skill using limit equilibrium methods for static and seismic conditions
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-009
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Slope Stability Analyzer Skill

## Purpose

The Slope Stability Analyzer Skill performs slope stability analysis using limit equilibrium methods for circular and non-circular failure surfaces under static and seismic loading conditions.

## Capabilities

- Limit equilibrium analysis (Bishop, Spencer, Morgenstern-Price)
- Circular and non-circular failure surfaces
- Factor of safety calculation
- Seismic slope stability (pseudo-static)
- Probabilistic slope stability
- Sensitivity analysis
- Back-analysis for failed slopes
- Reinforced slope analysis

## Usage Guidelines

### When to Use
- Analyzing natural slopes
- Designing cut and fill slopes
- Evaluating landslide potential
- Designing slope reinforcement

### Prerequisites
- Slope geometry defined
- Soil stratigraphy established
- Shear strength parameters available
- Groundwater conditions known

### Best Practices
- Search for critical failure surface
- Use appropriate analysis method
- Consider pore pressure effects
- Verify with multiple methods

## Process Integration

This skill integrates with:
- Slope Stability Analysis
- Retaining Wall Design

## Configuration

```yaml
slope-stability-analyzer:
  methods:
    - bishop-simplified
    - spencer
    - morgenstern-price
    - janbu
  failure-surfaces:
    - circular
    - non-circular
    - block
  conditions:
    - static
    - pseudo-static
    - dynamic
```

## Output Artifacts

- Factor of safety results
- Critical slip surfaces
- Sensitivity analyses
- Stability charts

``````

## 77 · 工程土分类与参数关联

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/soil-classification-tool

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/soil-classification-tool/SKILL.md

``````markdown
---
name: soil-classification-tool
description: Soil classification skill using USCS and AASHTO systems with SPT correlations
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Geotechnical Analysis
  skill-id: CIV-SK-013
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Soil Classification Tool Skill

## Purpose

The Soil Classification Tool Skill classifies soils using USCS and AASHTO systems, interprets Atterberg limits, and provides SPT correlation calculations for engineering properties.

## Capabilities

- USCS classification
- AASHTO soil classification
- Atterberg limits interpretation
- Grain size distribution analysis
- Soil description generator
- SPT correlation calculations
- Relative density estimation
- Consistency determination

## Usage Guidelines

### When to Use
- Classifying soil samples
- Interpreting laboratory data
- Estimating engineering properties
- Preparing geotechnical reports

### Prerequisites
- Laboratory test data available
- Grain size distribution known
- Atterberg limits tested
- SPT values recorded

### Best Practices
- Follow standard procedures
- Consider local correlations
- Document sample quality
- Verify visual description

## Process Integration

This skill integrates with:
- Geotechnical Site Investigation

## Configuration

```yaml
soil-classification-tool:
  systems:
    - USCS
    - AASHTO
  correlations:
    - SPT-friction-angle
    - SPT-undrained-strength
    - SPT-relative-density
  outputs:
    - classification
    - description
    - properties
```

## Output Artifacts

- Soil classifications
- Property correlations
- Boring logs
- Soil descriptions

``````

## 78 · 施工报审资料跟踪

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/submittal-tracker

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/submittal-tracker/SKILL.md

``````markdown
---
name: submittal-tracker
description: Construction submittal tracking skill for document management and review workflow
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Construction Management
  skill-id: CIV-SK-029
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Submittal Tracker Skill

## Purpose

The Submittal Tracker Skill manages construction submittals including log management, review workflow automation, and approval tracking.

## Capabilities

- Submittal log management
- Review workflow automation
- Specification section linking
- Response time tracking
- Revision management
- Approval stamp generation
- Distribution tracking
- Status reporting

## Usage Guidelines

### When to Use
- Managing project submittals
- Tracking review status
- Monitoring response times
- Generating status reports

### Prerequisites
- Submittal register established
- Review workflow defined
- Spec sections identified
- Response times specified

### Best Practices
- Track all submittals
- Monitor response times
- Document review comments
- Maintain revision history

## Process Integration

This skill integrates with:
- Shop Drawing Review
- Construction Quality Control

## Configuration

```yaml
submittal-tracker:
  status-types:
    - pending
    - under-review
    - approved
    - rejected
    - resubmit
  tracking:
    - dates
    - reviewers
    - comments
    - revisions
```

## Output Artifacts

- Submittal logs
- Status reports
- Response time analysis
- Approval stamps

``````

## 79 · 测量点云与地形数据处理

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/survey-data-processor

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/survey-data-processor/SKILL.md

``````markdown
---
name: survey-data-processor
description: Survey data processing skill for point clouds, DTM generation, and coordinate transformation
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Surveying
  skill-id: CIV-SK-033
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Survey Data Processor Skill

## Purpose

The Survey Data Processor Skill processes survey data including point cloud processing, DTM/TIN generation, coordinate transformation, and traverse adjustment.

## Capabilities

- Point cloud processing
- DTM/TIN generation
- Coordinate transformation
- Traverse adjustment
- Level loop adjustment
- GNSS data processing
- Contour generation
- Feature extraction

## Usage Guidelines

### When to Use
- Processing survey data
- Creating terrain models
- Transforming coordinates
- Adjusting measurements

### Prerequisites
- Survey data collected
- Control points established
- Coordinate system defined
- Quality requirements known

### Best Practices
- Check data quality
- Verify transformations
- Document adjustments
- Archive raw data

## Process Integration

This skill integrates with:
- Geotechnical Site Investigation
- Highway Geometric Design

## Configuration

```yaml
survey-data-processor:
  data-types:
    - point-cloud
    - total-station
    - GNSS
    - level
  processing:
    - DTM-generation
    - adjustment
    - transformation
    - feature-extraction
```

## Output Artifacts

- DTM surfaces
- Adjusted coordinates
- Transformation reports
- Survey maps

``````

## 80 · 供水管网与泵组建模

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/civil-engineering/skills/water-distribution-modeler

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/civil-engineering/skills/water-distribution-modeler/SKILL.md

``````markdown
---
name: water-distribution-modeler
description: Water distribution system modeling skill for pipe networks, pump analysis, and fire flow
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: civil-engineering
  domain: science
  category: Water Resources
  skill-id: CIV-SK-025
graph:
  domains: [domain:civil-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:computational-geometry, skill-area:data-analysis]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Water Distribution Modeler Skill

## Purpose

The Water Distribution Modeler Skill analyzes water distribution systems including pipe network analysis, fire flow evaluation, and pump performance assessment.

## Capabilities

- Pipe network analysis (Hardy-Cross, Newton-Raphson)
- Fire flow analysis
- Pump curve analysis
- Storage tank sizing
- Pressure zone analysis
- Water quality modeling
- Extended period simulation
- System optimization

## Usage Guidelines

### When to Use
- Designing water systems
- Evaluating system capacity
- Analyzing fire flow
- Optimizing operations

### Prerequisites
- Network topology defined
- Demand patterns established
- Pump curves available
- Tank data complete

### Best Practices
- Calibrate with field data
- Model multiple scenarios
- Verify pressure limits
- Consider emergency conditions

## Process Integration

This skill integrates with:
- Water Distribution Design

## Configuration

```yaml
water-distribution-modeler:
  analysis-types:
    - steady-state
    - extended-period
    - fire-flow
    - water-quality
  solvers:
    - gradient
    - linear-theory
  components:
    - pipes
    - pumps
    - tanks
    - valves
```

## Output Artifacts

- Network solutions
- Pressure maps
- Fire flow reports
- Water age analysis

``````

## 81 · 材料晶体结构分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/materials-science/skills/crystallography-analysis

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/materials-science/skills/crystallography-analysis/SKILL.md

``````markdown
---
name: crystallography-analysis
description: Advanced skill for crystallographic structure analysis and determination including space group identification, atomic position refinement, and PDF analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
metadata:
  specialization: materials-science
  domain: science
  category: materials-characterization
  priority: high
  phase: 6
  tools-libraries:
    - GSAS-II
    - VESTA
    - CrystalMaker
    - Mercury
    - PDFgui
graph:
  domains: [domain:materials-science]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Crystallography Analysis Skill

## Purpose

The Crystallography Analysis skill provides advanced capabilities for determining and analyzing crystal structures from diffraction data, enabling detailed structural characterization of crystalline materials including phase identification, symmetry analysis, and local structure determination through pair distribution function methods.

## Capabilities

- Space group determination and symmetry analysis
- Atomic position refinement
- Disorder and defect modeling
- Structure factor calculation
- Pair distribution function (PDF) analysis
- Neutron diffraction data analysis
- Single-crystal structure solution
- Reciprocal space mapping interpretation

## Usage Guidelines

### Space Group Determination

1. **Systematic Absence Analysis**
   - Identify extinct reflections from diffraction pattern
   - Determine Bravais lattice type
   - Assign possible space groups from extinction conditions

2. **Symmetry Verification**
   - Check intensity statistics for centrosymmetry
   - Verify Laue class assignment
   - Consider twinning if symmetry ambiguous

3. **Structure Validation**
   - Use checkCIF for validation
   - Verify bond distances and angles
   - Check displacement parameters for physical reasonableness

### Rietveld Refinement

1. **Starting Model**
   - Use published structure or ab initio solution
   - Verify unit cell parameters from indexing
   - Set appropriate peak shape function

2. **Refinement Strategy**
   - Refine background first, then scale
   - Add profile parameters gradually
   - Refine atomic positions with appropriate constraints

3. **Quality Metrics**
   - Monitor Rwp, Rp, chi-squared
   - Check difference curve for systematic errors
   - Validate with independent techniques

### Pair Distribution Function (PDF)

1. **Data Collection**
   - Use high Q-range data (synchrotron or Mo source)
   - Measure to Q > 20 A^-1 for adequate resolution
   - Collect background and container separately

2. **Data Reduction**
   - Apply corrections (absorption, polarization, Compton)
   - Normalize to obtain S(Q)
   - Fourier transform to obtain G(r)

3. **PDF Modeling**
   - Use small-box modeling for average structure
   - Apply reverse Monte Carlo for complex disorder
   - Consider multiple phases and nanoparticle effects

## Process Integration

- MS-001: XRD Analysis & Phase Identification
- MS-002: Electron Microscopy Characterization

## Input Schema

```json
{
  "sample_id": "string",
  "data_type": "powder_xrd|single_crystal|neutron|electron|pdf",
  "data_file": "string (path)",
  "wavelength": "number (Angstrom)",
  "analysis_type": "phase_id|refinement|structure_solution|pdf_fit",
  "starting_model": "string (CIF file, optional)"
}
```

## Output Schema

```json
{
  "sample_id": "string",
  "space_group": "string",
  "unit_cell": {
    "a": "number (Angstrom)",
    "b": "number (Angstrom)",
    "c": "number (Angstrom)",
    "alpha": "number (degrees)",
    "beta": "number (degrees)",
    "gamma": "number (degrees)"
  },
  "atomic_positions": [
    {
      "atom": "string",
      "site": "string",
      "x": "number",
      "y": "number",
      "z": "number",
      "occupancy": "number",
      "Uiso": "number (Angstrom^2)"
    }
  ],
  "r_factors": {
    "Rwp": "number",
    "Rp": "number",
    "chi_squared": "number"
  }
}
```

## Best Practices

1. Always index pattern before attempting structure solution
2. Use multiple space group possibilities if extinction conditions ambiguous
3. Apply soft constraints for chemically reasonable structures
4. Validate refined structures against bond valence sums
5. Report estimated standard deviations from refinement
6. Use combined refinement for multi-technique data when available

## Integration Points

- Connects with XRD Analysis for powder data processing
- Feeds into DFT Calculation for structure verification
- Supports Electron Microscopy for SAED indexing
- Integrates with Materials Database for structure archival

``````

## 82 · 金属材料金相分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/materials-science/skills/metallurgical-analysis

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/materials-science/skills/metallurgical-analysis/SKILL.md

``````markdown
---
name: metallurgical-analysis
description: Specialized skill for metallic materials analysis and metallography including grain size measurement, phase quantification, and inclusion rating
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
metadata:
  specialization: materials-science
  domain: science
  category: materials-characterization
  priority: high
  phase: 6
  tools-libraries:
    - ImageJ
    - Clemex
    - ASTM E112
    - ASTM E45
graph:
  domains: [domain:materials-science]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Metallurgical Analysis Skill

## Purpose

The Metallurgical Analysis skill provides specialized capabilities for characterizing metallic materials through metallographic techniques, enabling systematic evaluation of microstructure, grain size, phase distribution, and inclusion content per industry standards.

## Capabilities

- Metallographic preparation protocol selection
- Etching reagent selection for different alloys
- Grain size measurement (ASTM E112, intercept method)
- Phase fraction quantification (point count, image analysis)
- Inclusion rating (ASTM E45)
- Banding and segregation assessment
- Prior austenite grain boundary revelation
- Weld microstructure evaluation (HAZ mapping)

## Usage Guidelines

### Sample Preparation

1. **Sectioning**
   - Select appropriate cutting method (abrasive, EDM, precision saw)
   - Minimize heat input to prevent microstructural changes
   - Identify orientation relative to processing direction

2. **Mounting**
   - Choose mount type (hot compression, cold setting)
   - Add conductive filler for SEM/EBSD samples
   - Consider edge retention requirements

3. **Grinding and Polishing**
   - Follow systematic grit progression (120 to 1200 to diamond)
   - Use appropriate lubricant and rotation direction
   - Verify scratch-free surface before etching

### Etching Selection

| Alloy System | Etchant | Purpose |
|--------------|---------|---------|
| Carbon steels | 2% Nital | General microstructure |
| Stainless steel | Vilella's | Martensitic structures |
| Aluminum | Keller's | Grain boundaries, precipitates |
| Titanium | Kroll's | Alpha-beta microstructure |
| Copper | FeCl3/HCl | Grain boundaries |
| Nickel superalloys | Glyceregia | Gamma prime, carbides |

### Grain Size Measurement

1. **ASTM E112 Methods**
   - Comparison method: Match to standard charts
   - Planimetric method: Count grains in known area
   - Intercept method: Count grain boundary intersections

2. **Calculation**
   - Apply magnification correction
   - Use minimum 5 fields for statistical validity
   - Report ASTM grain size number with standard deviation

3. **Special Cases**
   - Duplex structures: Report both phases separately
   - Elongated grains: Measure aspect ratio
   - Prior austenite: Use specific etchants (picric acid based)

### Inclusion Rating (ASTM E45)

1. **Method Selection**
   - Method A: Worst field rating
   - Method D: Quantitative measurement
   - Specify inclusion type (A, B, C, D sulfides, oxides)

2. **Reporting**
   - Include severity (thin, heavy) and length
   - Note distribution (random, stringer, cluster)
   - Compare to specification limits

## Process Integration

- MS-002: Electron Microscopy Characterization
- MS-017: Root Cause Failure Analysis

## Input Schema

```json
{
  "sample_id": "string",
  "alloy_system": "steel|aluminum|titanium|copper|nickel",
  "alloy_grade": "string",
  "analysis_type": "grain_size|phase_fraction|inclusion|weld_eval",
  "magnification": "number",
  "etchant_used": "string"
}
```

## Output Schema

```json
{
  "sample_id": "string",
  "grain_size": {
    "astm_number": "number",
    "average_diameter": "number (microns)",
    "standard_deviation": "number",
    "method": "string"
  },
  "phase_fractions": [
    {
      "phase": "string",
      "fraction": "number (percent)",
      "morphology": "string"
    }
  ],
  "inclusion_rating": {
    "method": "string",
    "type_a": "number",
    "type_b": "number",
    "type_c": "number",
    "type_d": "number"
  },
  "observations": "string"
}
```

## Best Practices

1. Document complete preparation procedure for reproducibility
2. Use consistent magnification within a comparative study
3. Apply appropriate etching time - under-etched is better than over-etched
4. Verify grain boundaries are fully revealed before measurement
5. Use image analysis software for quantitative phase measurements
6. Include representative micrographs in reports

## Integration Points

- Connects with Electron Microscopy for high-resolution analysis
- Feeds into Failure Analysis for metallographic investigation
- Supports Mechanical Testing for structure-property correlation
- Integrates with Heat Treatment Optimization for process development

``````

## 83 · 高分子材料性能表征

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/materials-science/skills/polymer-characterization

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/materials-science/skills/polymer-characterization/SKILL.md

``````markdown
---
name: polymer-characterization
description: Specialized skill for polymer materials analysis including molecular weight distribution, thermal transitions, crystallinity, and rheological properties
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
metadata:
  specialization: materials-science
  domain: science
  category: materials-characterization
  priority: high
  phase: 6
  tools-libraries:
    - GPC/SEC software
    - Rheometer software
    - FTIR libraries
    - DSC analysis
graph:
  domains: [domain:materials-science]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Polymer Characterization Skill

## Purpose

The Polymer Characterization skill provides comprehensive analysis capabilities for polymeric materials, enabling systematic evaluation of molecular weight, thermal behavior, crystallinity, mechanical properties, and chemical structure essential for polymer science and engineering applications.

## Capabilities

- Molecular weight distribution analysis (GPC/SEC)
- Thermal transition identification (Tg, Tm, Tc)
- Crystallinity determination (DSC, XRD)
- Rheological property analysis (viscosity, viscoelasticity)
- Chemical structure verification (FTIR, NMR)
- Degradation pathway analysis
- Additive and filler content determination
- Polymer blend compatibility assessment

## Usage Guidelines

### Molecular Weight Analysis (GPC/SEC)

1. **Sample Preparation**
   - Dissolve in appropriate solvent (THF, DMF, chloroform)
   - Filter through 0.45 um membrane
   - Prepare at 1-5 mg/mL concentration

2. **Calibration**
   - Use narrow molecular weight standards (PS, PMMA, PEO)
   - Apply universal calibration with Mark-Houwink parameters
   - Consider absolute methods (light scattering, viscometry)

3. **Data Analysis**
   - Calculate Mn, Mw, Mz averages
   - Determine polydispersity index (PDI = Mw/Mn)
   - Identify multimodal distributions

### Thermal Analysis for Polymers

1. **Glass Transition (Tg)**
   - Use DSC at 10-20 K/min heating rate
   - Report midpoint, onset, or inflection consistently
   - Note thermal history effects

2. **Melting Behavior**
   - Identify peak melting temperature (Tm)
   - Calculate heat of fusion for crystallinity
   - Watch for multiple melting peaks (reorganization)

3. **Crystallinity Calculation**
   ```
   Crystallinity (%) = (ΔHm / ΔHm°) × 100
   ```
   Where ΔHm° is the enthalpy of 100% crystalline polymer

### Rheological Characterization

1. **Viscosity Measurements**
   - Shear viscosity vs. shear rate curves
   - Zero-shear viscosity determination
   - Shear thinning/thickening behavior

2. **Viscoelastic Properties**
   - Storage modulus (G') and loss modulus (G'')
   - Complex viscosity (η*)
   - Crossover frequency and modulus

3. **Temperature Dependence**
   - Apply WLF equation above Tg
   - Use Arrhenius below Tg
   - Generate master curves via time-temperature superposition

### Chemical Structure Analysis

1. **FTIR Spectroscopy**
   - Identify functional groups
   - Verify polymer backbone structure
   - Detect oxidation and degradation

2. **NMR Spectroscopy**
   - Determine tacticity and stereoregularity
   - Identify end groups and branching
   - Quantify copolymer composition

## Process Integration

- MS-003: Spectroscopic Analysis Suite
- MS-004: Thermal Analysis Protocol

## Input Schema

```json
{
  "sample_id": "string",
  "polymer_type": "string",
  "analysis_methods": ["GPC", "DSC", "rheology", "FTIR", "NMR"],
  "solvent": "string (for GPC)",
  "temperature_range": {
    "start": "number (C)",
    "end": "number (C)"
  }
}
```

## Output Schema

```json
{
  "sample_id": "string",
  "molecular_weight": {
    "Mn": "number (g/mol)",
    "Mw": "number (g/mol)",
    "PDI": "number"
  },
  "thermal_properties": {
    "Tg": "number (C)",
    "Tm": "number (C)",
    "Tc": "number (C)",
    "crystallinity": "number (percent)"
  },
  "rheological_properties": {
    "zero_shear_viscosity": "number (Pa.s)",
    "crossover_frequency": "number (rad/s)",
    "flow_activation_energy": "number (kJ/mol)"
  },
  "chemical_structure": {
    "functional_groups": ["string"],
    "degradation_indicators": "string"
  }
}
```

## Best Practices

1. Erase thermal history with heat-cool-heat DSC cycle
2. Use appropriate molecular weight standards for calibration
3. Ensure complete dissolution for GPC samples
4. Apply Cox-Merz rule to relate steady shear and dynamic data
5. Verify polymer identification with multiple techniques
6. Document processing and storage conditions

## Integration Points

- Connects with Thermal Analysis for comprehensive thermal characterization
- Feeds into Mechanical Testing for structure-property relationships
- Supports Spectroscopy Analysis for chemical identification
- Integrates with Composite Design for matrix characterization

``````

## 84 · 材料表面成分与形貌分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/materials-science/skills/surface-analysis

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/materials-science/skills/surface-analysis/SKILL.md

``````markdown
---
name: surface-analysis
description: Skill for surface composition, chemical state, and topography analysis including XPS depth profiling, AFM imaging, and contact angle measurements
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
metadata:
  specialization: materials-science
  domain: science
  category: materials-characterization
  priority: high
  phase: 6
  tools-libraries:
    - CasaXPS
    - Gwyddion
    - AFM analysis software
    - ImageJ
graph:
  domains: [domain:materials-science]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Surface Analysis Skill

## Purpose

The Surface Analysis skill provides comprehensive capabilities for characterizing material surfaces, enabling detailed analysis of surface composition, chemical bonding states, topography, and interfacial properties critical for understanding surface-sensitive phenomena.

## Capabilities

- XPS depth profiling and chemical state analysis
- AFM imaging and roughness quantification
- Contact angle measurement and surface energy calculation
- Profilometry data analysis
- Surface contamination identification
- Tribological surface analysis
- Coating thickness measurement
- Adhesion mechanism analysis

## Usage Guidelines

### X-ray Photoelectron Spectroscopy (XPS)

1. **Survey Spectra**
   - Acquire wide scan (0-1200 eV) for elemental identification
   - Identify all elements present above detection limit (~0.1 at%)
   - Note adventitious carbon for charge referencing

2. **High-Resolution Spectra**
   - Acquire narrow scans for elements of interest
   - Use appropriate pass energy (20-50 eV typical)
   - Ensure sufficient signal-to-noise for peak fitting

3. **Peak Fitting**
   - Apply Shirley or linear background
   - Constrain FWHM and peak shape within physical limits
   - Assign chemical states from binding energy shifts

4. **Depth Profiling**
   - Use Ar+ sputtering for inorganic materials
   - Consider cluster ions (Ar-cluster, C60) for organics
   - Monitor for preferential sputtering and mixing

### Atomic Force Microscopy (AFM)

1. **Imaging Mode Selection**
   - Contact mode: Hard surfaces, atomic resolution
   - Tapping mode: Soft samples, reduced tip wear
   - Non-contact: Minimal surface interaction

2. **Image Analysis**
   - Calculate roughness parameters (Ra, RMS, Rmax)
   - Identify surface features and defects
   - Measure step heights and feature dimensions

3. **Force Spectroscopy**
   - Acquire force-distance curves
   - Extract adhesion forces
   - Map mechanical properties (modulus, stiffness)

### Contact Angle Analysis

1. **Measurement Methods**
   - Sessile drop for static contact angle
   - Advancing/receding for dynamic behavior
   - Wilhelmy plate for surface tension

2. **Surface Energy Calculation**
   - Owens-Wendt method (dispersive + polar)
   - Van Oss-Chaudhury-Good (acid-base)
   - Use multiple probe liquids (water, diiodomethane, formamide)

3. **Interpretation**
   - Hydrophilic: Contact angle < 90 degrees
   - Hydrophobic: Contact angle > 90 degrees
   - Superhydrophobic: Contact angle > 150 degrees

## Process Integration

- MS-003: Spectroscopic Analysis Suite
- MS-015: Thin Film Deposition Protocol

## Input Schema

```json
{
  "sample_id": "string",
  "technique": "XPS|AFM|contact_angle|profilometry",
  "analysis_type": "survey|depth_profile|imaging|force_spectroscopy|wettability",
  "parameters": {
    "scan_area": "number (um x um for AFM)",
    "sputter_depth": "number (nm for XPS)",
    "probe_liquids": ["string (for contact angle)"]
  }
}
```

## Output Schema

```json
{
  "sample_id": "string",
  "xps_results": {
    "elemental_composition": [
      {
        "element": "string",
        "concentration": "number (at%)",
        "chemical_states": [
          {
            "state": "string",
            "binding_energy": "number (eV)",
            "fraction": "number (percent)"
          }
        ]
      }
    ],
    "depth_profile": {
      "depth": ["number (nm)"],
      "composition": {}
    }
  },
  "afm_results": {
    "roughness": {
      "Ra": "number (nm)",
      "RMS": "number (nm)",
      "Rmax": "number (nm)"
    },
    "features": ["string"]
  },
  "surface_energy": {
    "total": "number (mJ/m2)",
    "dispersive": "number (mJ/m2)",
    "polar": "number (mJ/m2)"
  }
}
```

## Best Practices

1. Clean samples appropriately before analysis (solvent, plasma)
2. Use charge neutralization for insulating samples in XPS
3. Reference XPS binding energies to C 1s at 284.8 eV
4. Calibrate AFM z-scale with step height standards
5. Use fresh probe liquids for contact angle measurements
6. Report measurement conditions and uncertainties

## Integration Points

- Connects with Spectroscopy Analysis for complementary chemical information
- Feeds into Thin Film Deposition for process monitoring
- Supports Failure Analysis for surface contamination identification
- Integrates with Corrosion Assessment for passive layer analysis

``````

## 85 · 工业废气治理设备选型

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/environmental-engineering/skills/air-pollution-control

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/environmental-engineering/skills/air-pollution-control/SKILL.md

``````markdown
---
name: air-pollution-control
description: Specialized skill for air pollution control equipment selection and design including scrubbers, baghouses, ESPs, oxidizers, and BACT/LAER determination.
allowed-tools: Read, Grep, Write, Bash, Edit, Glob
category: Air Quality Management
backlog-id: SK-007
metadata:
  author: babysitter-sdk
  version: "1.0.0"
graph:
  domains: [domain:environmental-engineering]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:geospatial-data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Air Pollution Control Design Skill

Air pollution control equipment selection and design for industrial emission reduction.

## Purpose

This skill provides comprehensive capabilities for designing air pollution control systems, including technology selection, equipment sizing, efficiency calculations, and regulatory compliance demonstration (BACT/LAER/MACT).

## Capabilities

### Scrubber Design
- Wet scrubber technology selection
- Packed tower design and sizing
- Spray tower configuration
- Venturi scrubber design
- Pressure drop calculations
- Liquid-to-gas ratio optimization
- Chemical dosing requirements

### Baghouse and Fabric Filter Sizing
- Filter media selection
- Air-to-cloth ratio determination
- Compartmentalization design
- Pulse-jet vs reverse-air cleaning
- Pressure drop estimation
- Bag life prediction
- Hopper sizing

### Electrostatic Precipitator Design
- Collection efficiency calculation
- Specific Collection Area (SCA) determination
- Plate spacing and configuration
- Electrical field strength
- Rapping system design
- Resistivity considerations
- Power supply sizing

### Thermal and Catalytic Oxidizer Specification
- Destruction efficiency requirements
- Temperature and residence time
- Heat recovery options (regenerative, recuperative)
- Catalyst selection for catalytic oxidizers
- Auxiliary fuel requirements
- Turndown capabilities

### Carbon Adsorption System Design
- Activated carbon selection
- Adsorption capacity calculations
- Breakthrough time estimation
- Bed sizing
- Regeneration system design
- Carbon replacement frequency

### Control Efficiency Calculations
- Outlet emission rate determination
- Removal efficiency verification
- Stack testing correlation
- Continuous monitoring requirements

### Pressure Drop and Energy Analysis
- System pressure drop calculation
- Fan power requirements
- Operating cost estimation
- Energy optimization opportunities

### BACT/LAER/MACT Determination
- Control technology identification
- Cost-effectiveness analysis
- Technical feasibility evaluation
- Regulatory database research
- Top-down BACT analysis

## Prerequisites

### Installation
```bash
pip install numpy scipy pandas matplotlib
```

### Optional Dependencies
```bash
# For chemical property lookup
pip install chemicals thermo

# For visualization
pip install plotly
```

## Usage Patterns

### Baghouse Design
```python
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class GasStreamData:
    """Gas stream characteristics"""
    flow_rate_acfm: float
    temperature_f: float
    moisture_pct: float
    particulate_loading_gr_acf: float
    particle_size_micron: float
    gas_composition: Dict[str, float] = None

@dataclass
class BaghouseDesign:
    """Baghouse design parameters"""
    filter_media: str
    bag_diameter_in: float
    bag_length_ft: float
    air_to_cloth_ratio: float
    cleaning_type: str  # 'pulse_jet', 'reverse_air', 'shaker'

class BaghouseCalculator:
    """Pulse-jet baghouse sizing calculations"""

    # Recommended air-to-cloth ratios (acfm/ft2) by application
    AC_RATIOS = {
        'cement': {'gross': 4.0, 'net': 3.5},
        'coal': {'gross': 6.0, 'net': 5.0},
        'foundry': {'gross': 4.5, 'net': 3.5},
        'steel': {'gross': 5.0, 'net': 4.0},
        'chemical': {'gross': 5.5, 'net': 4.5},
        'pharmaceutical': {'gross': 3.5, 'net': 3.0},
        'general': {'gross': 5.0, 'net': 4.0}
    }

    # Filter media properties
    MEDIA_PROPERTIES = {
        'polyester': {'max_temp_f': 275, 'cost_factor': 1.0, 'acid_resist': 'good'},
        'polypropylene': {'max_temp_f': 200, 'cost_factor': 0.9, 'acid_resist': 'excellent'},
        'nomex': {'max_temp_f': 400, 'cost_factor': 3.0, 'acid_resist': 'good'},
        'fiberglass': {'max_temp_f': 500, 'cost_factor': 2.5, 'acid_resist': 'excellent'},
        'ptfe': {'max_temp_f': 500, 'cost_factor': 8.0, 'acid_resist': 'excellent'},
        'p84': {'max_temp_f': 500, 'cost_factor': 5.0, 'acid_resist': 'good'}
    }

    def select_filter_media(self, gas: GasStreamData) -> str:
        """Select appropriate filter media based on gas conditions"""
        temp = gas.temperature_f

        suitable = []
        for media, props in self.MEDIA_PROPERTIES.items():
            if props['max_temp_f'] >= temp:
                suitable.append((media, props))

        # Return lowest cost suitable media
        suitable.sort(key=lambda x: x[1]['cost_factor'])
        return suitable[0][0] if suitable else 'ptfe'

    def calculate_filter_area(self, gas: GasStreamData,
                              application: str = 'general',
                              use_net_ratio: bool = True) -> Dict:
        """Calculate required filter area"""
        ratios = self.AC_RATIOS.get(application, self.AC_RATIOS['general'])
        ac_ratio = ratios['net'] if use_net_ratio else ratios['gross']

        filter_area = gas.flow_rate_acfm / ac_ratio

        return {
            'gas_flow_acfm': gas.flow_rate_acfm,
            'air_to_cloth_ratio': ac_ratio,
            'filter_area_sqft': filter_area
        }

    def size_baghouse(self, gas: GasStreamData,
                      bag_diameter_in: float = 6.0,
                      bag_length_ft: float = 10.0,
                      application: str = 'general') -> Dict:
        """Size complete baghouse system"""

        # Filter media selection
        media = self.select_filter_media(gas)

        # Calculate filter area
        area_calc = self.calculate_filter_area(gas, application)
        required_area = area_calc['filter_area_sqft']

        # Bag area calculation
        bag_area = np.pi * (bag_diameter_in / 12) * bag_length_ft  # sq ft per bag

        # Number of bags
        num_bags = np.ceil(required_area / bag_area)

        # Compartments (typically 8-16 bags per row, 2-4 rows per compartment)
        bags_per_compartment = 32  # typical
        num_compartments = np.ceil(num_bags / bags_per_compartment)

        # Pressure drop estimate (typical for pulse-jet)
        dp_filter = 2.5  # inches w.c. for clean filter
        dp_tubesheet = 0.5
        dp_inlet_outlet = 1.0
        total_dp = dp_filter + dp_tubesheet + dp_inlet_outlet

        # Hopper sizing (4:1 turndown, 8-hour storage)
        dust_rate_lb_hr = gas.particulate_loading_gr_acf * gas.flow_rate_acfm * 60 / 7000
        hopper_volume = dust_rate_lb_hr * 8 / 50  # 50 lb/cf bulk density

        return {
            'filter_media': media,
            'required_filter_area_sqft': required_area,
            'bag_diameter_in': bag_diameter_in,
            'bag_length_ft': bag_length_ft,
            'area_per_bag_sqft': bag_area,
            'total_bags': int(num_bags),
            'num_compartments': int(num_compartments),
            'air_to_cloth_gross': gas.flow_rate_acfm / (num_bags * bag_area),
            'pressure_drop_in_wc': total_dp,
            'dust_rate_lb_hr': dust_rate_lb_hr,
            'hopper_volume_cf': hopper_volume,
            'max_temp_f': self.MEDIA_PROPERTIES[media]['max_temp_f']
        }

# Example usage
gas = GasStreamData(
    flow_rate_acfm=50000,
    temperature_f=350,
    moisture_pct=8,
    particulate_loading_gr_acf=2.0,
    particle_size_micron=5
)

calculator = BaghouseCalculator()
design = calculator.size_baghouse(gas, application='cement')

print(f"Filter media: {design['filter_media']}")
print(f"Total bags: {design['total_bags']}")
print(f"Compartments: {design['num_compartments']}")
print(f"A/C ratio: {design['air_to_cloth_gross']:.2f} acfm/sqft")
print(f"Pressure drop: {design['pressure_drop_in_wc']:.1f} in w.c.")
```

### Wet Scrubber Design
```python
class WetScrubberDesign:
    """Wet scrubber design calculations"""

    def packed_tower_sizing(self, gas_flow_acfm: float,
                           pollutant: str,
                           inlet_conc_ppm: float,
                           outlet_conc_ppm: float,
                           scrubbing_liquid: str = 'water') -> Dict:
        """Size packed tower for gas absorption"""

        # Removal efficiency
        efficiency = (inlet_conc_ppm - outlet_conc_ppm) / inlet_conc_ppm

        # Gas velocity (typical range 3-6 ft/s for packed towers)
        gas_velocity_fps = 4.5

        # Cross-sectional area
        area_sqft = (gas_flow_acfm / 60) / gas_velocity_fps

        # Diameter
        diameter_ft = np.sqrt(4 * area_sqft / np.pi)

        # Height based on NTU (simplified)
        ntu = -np.log(1 - efficiency)  # Number of transfer units
        htu = 2.5  # Height of transfer unit (ft) - typical for 2" packing
        packing_height = ntu * htu

        # L/G ratio (liquid to gas)
        lg_ratio = 10  # gpm per 1000 acfm typical

        # Liquid flow rate
        liquid_flow_gpm = gas_flow_acfm * lg_ratio / 1000

        # Pressure drop (1-2 in w.c. per ft of packing typical)
        pressure_drop = packing_height * 1.5

        return {
            'diameter_ft': diameter_ft,
            'packing_height_ft': packing_height,
            'total_height_ft': packing_height * 1.5,  # Add for internals
            'cross_section_sqft': area_sqft,
            'gas_velocity_fps': gas_velocity_fps,
            'liquid_flow_gpm': liquid_flow_gpm,
            'lg_ratio_gpm_per_kacfm': lg_ratio,
            'pressure_drop_in_wc': pressure_drop,
            'removal_efficiency_pct': efficiency * 100,
            'ntu': ntu
        }

    def venturi_scrubber_sizing(self, gas_flow_acfm: float,
                                particulate_loading_gr_acf: float,
                                target_efficiency_pct: float) -> Dict:
        """Size venturi scrubber for particulate removal"""

        # Pressure drop vs efficiency correlation (Johnstone equation)
        # Efficiency increases with pressure drop
        # For 99% efficiency, typically need 30-50 in w.c.

        if target_efficiency_pct >= 99:
            pressure_drop = 50
        elif target_efficiency_pct >= 95:
            pressure_drop = 30
        elif target_efficiency_pct >= 90:
            pressure_drop = 20
        else:
            pressure_drop = 10

        # L/G ratio (higher for higher efficiency)
        lg_ratio = 8 + (target_efficiency_pct - 90) * 0.2

        # Throat velocity (typically 12,000-24,000 fpm)
        throat_velocity = 15000  # fpm

        # Throat area
        throat_area = gas_flow_acfm / throat_velocity

        # Liquid flow
        liquid_flow = gas_flow_acfm * lg_ratio / 1000

        return {
            'throat_area_sqft': throat_area,
            'throat_velocity_fpm': throat_velocity,
            'pressure_drop_in_wc': pressure_drop,
            'liquid_flow_gpm': liquid_flow,
            'lg_ratio': lg_ratio,
            'expected_efficiency_pct': target_efficiency_pct
        }

# Example usage
scrubber = WetScrubberDesign()

# Packed tower for SO2 removal
packed = scrubber.packed_tower_sizing(
    gas_flow_acfm=30000,
    pollutant='SO2',
    inlet_conc_ppm=1000,
    outlet_conc_ppm=50
)
print(f"Packed tower diameter: {packed['diameter_ft']:.1f} ft")
print(f"Packing height: {packed['packing_height_ft']:.1f} ft")
print(f"Removal efficiency: {packed['removal_efficiency_pct']:.1f}%")

# Venturi for particulates
venturi = scrubber.venturi_scrubber_sizing(
    gas_flow_acfm=30000,
    particulate_loading_gr_acf=5.0,
    target_efficiency_pct=95
)
print(f"\nVenturi pressure drop: {venturi['pressure_drop_in_wc']} in w.c.")
print(f"Liquid flow: {venturi['liquid_flow_gpm']:.0f} gpm")
```

### BACT Analysis
```python
class BACTAnalysis:
    """Best Available Control Technology analysis"""

    # Control technology database (simplified)
    CONTROL_TECHNOLOGIES = {
        'PM': [
            {'name': 'Baghouse', 'efficiency': 99.9, 'cost_per_ton': 500},
            {'name': 'ESP', 'efficiency': 99.5, 'cost_per_ton': 400},
            {'name': 'Cyclone', 'efficiency': 90, 'cost_per_ton': 100},
            {'name': 'Wet Scrubber', 'efficiency': 95, 'cost_per_ton': 600}
        ],
        'SO2': [
            {'name': 'Wet FGD', 'efficiency': 98, 'cost_per_ton': 800},
            {'name': 'Dry FGD', 'efficiency': 95, 'cost_per_ton': 600},
            {'name': 'SDA', 'efficiency': 92, 'cost_per_ton': 500}
        ],
        'NOx': [
            {'name': 'SCR', 'efficiency': 90, 'cost_per_ton': 2000},
            {'name': 'SNCR', 'efficiency': 60, 'cost_per_ton': 500},
            {'name': 'Low-NOx Burner', 'efficiency': 50, 'cost_per_ton': 200}
        ],
        'VOC': [
            {'name': 'RTO', 'efficiency': 99, 'cost_per_ton': 3000},
            {'name': 'Catalytic Oxidizer', 'efficiency': 98, 'cost_per_ton': 2500},
            {'name': 'Carbon Adsorption', 'efficiency': 95, 'cost_per_ton': 1500},
            {'name': 'Condenser', 'efficiency': 85, 'cost_per_ton': 800}
        ]
    }

    def top_down_bact(self, pollutant: str, uncontrolled_tpy: float,
                      cost_threshold: float = 15000) -> List[Dict]:
        """Perform top-down BACT analysis

        Args:
            pollutant: Pollutant type (PM, SO2, NOx, VOC)
            uncontrolled_tpy: Uncontrolled emissions (tons per year)
            cost_threshold: Maximum acceptable cost ($/ton removed)
        """
        technologies = self.CONTROL_TECHNOLOGIES.get(pollutant, [])

        # Sort by efficiency (highest first) - top-down approach
        technologies = sorted(technologies, key=lambda x: x['efficiency'], reverse=True)

        results = []
        for tech in technologies:
            tons_removed = uncontrolled_tpy * tech['efficiency'] / 100
            controlled_emissions = uncontrolled_tpy - tons_removed
            annual_cost = tech['cost_per_ton'] * tons_removed
            cost_effectiveness = tech['cost_per_ton']

            is_feasible = cost_effectiveness <= cost_threshold

            results.append({
                'technology': tech['name'],
                'efficiency_pct': tech['efficiency'],
                'controlled_emissions_tpy': controlled_emissions,
                'tons_removed_tpy': tons_removed,
                'annual_cost': annual_cost,
                'cost_effectiveness': cost_effectiveness,
                'is_cost_effective': is_feasible,
                'bact_candidate': is_feasible
            })

            if is_feasible:
                break  # First cost-effective option is BACT

        return results

    def generate_bact_report(self, pollutant: str,
                             uncontrolled_tpy: float) -> str:
        """Generate BACT determination report"""
        analysis = self.top_down_bact(pollutant, uncontrolled_tpy)

        report = f"""
BACT DETERMINATION - {pollutant}
================================
Uncontrolled Emissions: {uncontrolled_tpy:.1f} tpy

TOP-DOWN ANALYSIS:

"""
        for i, tech in enumerate(analysis, 1):
            status = "BACT SELECTED" if tech['bact_candidate'] else \
                     "Eliminated - Cost" if not tech['is_cost_effective'] else "Evaluated"

            report += f"""
Step {i}: {tech['technology']}
  Control Efficiency: {tech['efficiency_pct']}%
  Controlled Emissions: {tech['controlled_emissions_tpy']:.2f} tpy
  Cost Effectiveness: ${tech['cost_effectiveness']:,.0f}/ton
  Status: {status}
"""

        # Find BACT
        bact = next((t for t in analysis if t['bact_candidate']), None)
        if bact:
            report += f"""
BACT DETERMINATION:
  Selected Technology: {bact['technology']}
  Emission Limit: {bact['controlled_emissions_tpy']:.2f} tpy
  Control Efficiency: {bact['efficiency_pct']}%
"""

        return report

# Example usage
bact = BACTAnalysis()

report = bact.generate_bact_report('NOx', uncontrolled_tpy=100)
print(report)

# VOC BACT
voc_analysis = bact.top_down_bact('VOC', uncontrolled_tpy=50)
for tech in voc_analysis:
    print(f"{tech['technology']}: {tech['efficiency_pct']}% - "
          f"${tech['cost_effectiveness']}/ton - "
          f"{'BACT' if tech['bact_candidate'] else 'Eliminated'}")
```

## Usage Guidelines

### When to Use This Skill
- Air pollution control system design
- Permit application preparation
- BACT/LAER/MACT determinations
- Control equipment optimization
- Emission reduction projects

### Best Practices
1. **Characterize emissions thoroughly** before design
2. **Consider multiple control options** for BACT
3. **Account for variable operating conditions** in sizing
4. **Include maintenance access** in design
5. **Design for turndown** when loads vary
6. **Plan for monitoring** to verify performance

### Process Integration
- AQ-002: Air Pollution Control System Design (all phases)
- AQ-001: Air Permit Application Development (BACT determination)

## Dependencies

- numpy: Numerical calculations
- scipy: Engineering correlations

## References

- EPA Air Pollution Control Technology Fact Sheets
- OAQPS Control Cost Manual
- EPA RACT/BACT/LAER Clearinghouse

``````

## 86 · 园区雨洪与绿色排水管理

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/environmental-engineering/skills/stormwater-management

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/environmental-engineering/skills/stormwater-management/SKILL.md

``````markdown
---
name: stormwater-management
description: Skill for integrated stormwater management and green infrastructure design with SWMM modeling, hydrologic analysis, BMP sizing, and MS4 permit compliance.
allowed-tools: Read, Grep, Write, Bash, Edit, Glob
category: Water and Wastewater Treatment
backlog-id: SK-004
metadata:
  author: babysitter-sdk
  version: "1.0.0"
graph:
  domains: [domain:environmental-engineering]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:geospatial-data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Stormwater Management Skill

Integrated stormwater management and green infrastructure design for sustainable urban drainage.

## Purpose

This skill provides comprehensive capabilities for stormwater management planning, including hydrologic analysis, green infrastructure design, BMP selection and sizing, SWMM modeling, and MS4 permit compliance analysis.

## Capabilities

### SWMM Modeling and Simulation
- EPA SWMM model setup and configuration
- Subcatchment delineation and parameterization
- Drainage network modeling
- Long-term continuous simulation
- Design storm analysis
- LID representation and modeling

### Hydrologic Analysis
- TR-55 methodology implementation
- Rational method calculations
- SCS Curve Number determination
- Time of concentration estimation
- Unit hydrograph development
- Rainfall-runoff modeling

### Green Infrastructure Sizing
- Bioretention facility design
- Permeable pavement sizing
- Rain garden design
- Green roof specifications
- Tree box filters
- Vegetated swales

### Detention/Retention Pond Design
- Storage volume calculations
- Stage-storage-discharge relationships
- Outlet structure design
- Emergency spillway sizing
- Sediment forebay design
- Maintenance access planning

### Water Quality BMP Selection
- Pollutant removal efficiency analysis
- BMP selection matrix
- Treatment train design
- Sizing for TSS removal
- Nutrient removal considerations
- Cost-effectiveness analysis

### Pollutant Load Modeling
- Event Mean Concentration (EMC) analysis
- Annual pollutant load estimation
- Source area contribution analysis
- Loading rate calculations
- Reduction target setting

### Low Impact Development Integration
- Site-level LID planning
- Watershed-scale LID analysis
- LID retrofit opportunities
- Performance monitoring design
- Adaptive management frameworks

### MS4 Permit Compliance Analysis
- NPDES requirements interpretation
- MCM implementation tracking
- TMDL compliance assessment
- Monitoring program design
- Annual report preparation

## Prerequisites

### Installation
```bash
pip install numpy scipy pandas matplotlib
```

### Optional Dependencies
```bash
# For SWMM integration
pip install swmm-api pyswmm

# For GIS analysis
pip install geopandas shapely

# For visualization
pip install plotly folium
```

## Usage Patterns

### Rational Method Calculations
```python
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class CatchmentData:
    """Catchment characteristics"""
    area_acres: float
    runoff_coefficient: float
    time_of_concentration_min: float
    description: str = ""

class RationalMethod:
    """Rational method for peak runoff calculation"""

    def __init__(self):
        # IDF curve coefficients (example for generic location)
        # Q = C * I * A, where I from IDF: I = a / (Tc + b)^c
        self.idf_coefficients = {
            2: {'a': 100, 'b': 10, 'c': 0.8},
            5: {'a': 120, 'b': 10, 'c': 0.8},
            10: {'a': 140, 'b': 10, 'c': 0.8},
            25: {'a': 160, 'b': 10, 'c': 0.8},
            50: {'a': 180, 'b': 10, 'c': 0.8},
            100: {'a': 200, 'b': 10, 'c': 0.8}
        }

    def rainfall_intensity(self, tc_min: float, return_period: int) -> float:
        """Calculate rainfall intensity from IDF curve (in/hr)"""
        coef = self.idf_coefficients.get(return_period, self.idf_coefficients[10])
        intensity = coef['a'] / (tc_min + coef['b']) ** coef['c']
        return intensity

    def peak_runoff(self, catchment: CatchmentData, return_period: int) -> float:
        """Calculate peak runoff using Rational Method (cfs)"""
        C = catchment.runoff_coefficient
        I = self.rainfall_intensity(catchment.time_of_concentration_min, return_period)
        A = catchment.area_acres

        Q = C * I * A  # cfs
        return Q

    def composite_runoff_coefficient(self, subareas: List[Tuple[float, float]]) -> float:
        """Calculate composite C for mixed land uses
        subareas: list of (area, C) tuples
        """
        total_area = sum(a for a, c in subareas)
        weighted_c = sum(a * c for a, c in subareas) / total_area
        return weighted_c

    @staticmethod
    def time_of_concentration_kirpich(length_ft: float, slope_pct: float) -> float:
        """Kirpich equation for Tc (minutes)"""
        tc = 0.0078 * (length_ft ** 0.77) * (slope_pct ** -0.385)
        return tc

# Example runoff coefficients
RUNOFF_COEFFICIENTS = {
    'commercial': 0.85,
    'industrial': 0.75,
    'residential_high_density': 0.65,
    'residential_medium_density': 0.45,
    'residential_low_density': 0.35,
    'parks': 0.20,
    'forest': 0.15,
    'impervious': 0.95,
    'lawn_steep': 0.30,
    'lawn_flat': 0.20
}

# Example usage
rational = RationalMethod()

# Calculate composite C for mixed use area
subareas = [
    (5.0, RUNOFF_COEFFICIENTS['commercial']),
    (10.0, RUNOFF_COEFFICIENTS['residential_medium_density']),
    (3.0, RUNOFF_COEFFICIENTS['parks'])
]
composite_c = rational.composite_runoff_coefficient(subareas)

catchment = CatchmentData(
    area_acres=18.0,
    runoff_coefficient=composite_c,
    time_of_concentration_min=15.0,
    description="Mixed use development"
)

for rp in [2, 10, 25, 100]:
    Q = rational.peak_runoff(catchment, rp)
    print(f"{rp}-year storm: Q = {Q:.1f} cfs")
```

### SCS Curve Number Method
```python
class SCSMethod:
    """SCS Curve Number method for runoff calculation"""

    def __init__(self, curve_number: float):
        self.cn = curve_number
        self.S = (1000 / curve_number) - 10  # Potential retention (inches)
        self.Ia = 0.2 * self.S  # Initial abstraction

    def runoff_depth(self, rainfall_inches: float) -> float:
        """Calculate runoff depth (inches)"""
        P = rainfall_inches
        if P <= self.Ia:
            return 0.0

        Q = (P - self.Ia) ** 2 / (P - self.Ia + self.S)
        return Q

    def runoff_volume(self, rainfall_inches: float, area_acres: float) -> float:
        """Calculate runoff volume (acre-feet)"""
        Q_inches = self.runoff_depth(rainfall_inches)
        volume_ac_ft = Q_inches / 12 * area_acres
        return volume_ac_ft

    @staticmethod
    def composite_cn(subareas: List[Tuple[float, float]]) -> float:
        """Calculate area-weighted composite CN
        subareas: list of (area, CN) tuples
        """
        total_area = sum(a for a, cn in subareas)
        weighted_cn = sum(a * cn for a, cn in subareas) / total_area
        return weighted_cn

    @staticmethod
    def adjust_cn_for_amc(cn_ii: float, condition: str) -> float:
        """Adjust CN for antecedent moisture condition
        condition: 'dry' (AMC-I), 'normal' (AMC-II), or 'wet' (AMC-III)
        """
        if condition == 'dry':
            cn = cn_ii / (2.281 - 0.01281 * cn_ii)
        elif condition == 'wet':
            cn = cn_ii / (0.427 + 0.00573 * cn_ii)
        else:
            cn = cn_ii
        return cn

# Standard curve numbers (AMC-II, Hydrologic Soil Group B)
CURVE_NUMBERS = {
    'impervious': 98,
    'commercial': 92,
    'industrial': 88,
    'residential_1_8_acre': 85,
    'residential_1_4_acre': 80,
    'residential_1_2_acre': 75,
    'residential_1_acre': 68,
    'open_space_good': 61,
    'open_space_fair': 69,
    'forest_good': 55,
    'pasture_good': 61
}

# Example usage
# Pre-development condition
pre_cn = SCSMethod.composite_cn([
    (20, CURVE_NUMBERS['forest_good']),
    (80, CURVE_NUMBERS['pasture_good'])
])
pre_scs = SCSMethod(pre_cn)

# Post-development condition
post_cn = SCSMethod.composite_cn([
    (30, CURVE_NUMBERS['impervious']),
    (40, CURVE_NUMBERS['residential_1_4_acre']),
    (30, CURVE_NUMBERS['open_space_good'])
])
post_scs = SCSMethod(post_cn)

rainfall = 3.5  # inches (design storm)
pre_runoff = pre_scs.runoff_volume(rainfall, area_acres=100)
post_runoff = post_scs.runoff_volume(rainfall, area_acres=100)

print(f"Pre-development CN: {pre_cn:.0f}")
print(f"Post-development CN: {post_cn:.0f}")
print(f"Pre-development runoff: {pre_runoff:.2f} acre-feet")
print(f"Post-development runoff: {post_runoff:.2f} acre-feet")
print(f"Required detention: {post_runoff - pre_runoff:.2f} acre-feet")
```

### Bioretention Sizing
```python
class BioretentionDesign:
    """Bioretention facility design"""

    def __init__(self, infiltration_rate_in_hr: float = 1.0):
        self.infiltration_rate = infiltration_rate_in_hr

    def size_for_water_quality(self, drainage_area_sf: float,
                                impervious_fraction: float,
                                design_rainfall_in: float = 1.0) -> Dict:
        """Size bioretention for water quality treatment"""
        # Calculate water quality volume (WQv)
        # Using simplified volumetric approach
        Rv = 0.05 + 0.009 * (impervious_fraction * 100)  # Runoff coefficient
        wqv_cf = Rv * design_rainfall_in / 12 * drainage_area_sf

        # Bioretention area sizing
        # Based on 6" ponding depth and filter media depth
        ponding_depth_ft = 0.5  # 6 inches
        drain_time_hr = 24  # Maximum drain time

        # Area based on infiltration during storm
        storm_duration_hr = 2  # Assume 2-hour storm
        infiltrated_depth = self.infiltration_rate * storm_duration_hr / 12  # feet

        # Minimum surface area
        min_area_sf = wqv_cf / (ponding_depth_ft + infiltrated_depth)

        # Typical sizing: 5-10% of impervious area
        recommended_area_sf = drainage_area_sf * impervious_fraction * 0.05

        return {
            'water_quality_volume_cf': wqv_cf,
            'minimum_surface_area_sf': min_area_sf,
            'recommended_area_sf': max(min_area_sf, recommended_area_sf),
            'ponding_depth_in': 6,
            'filter_media_depth_in': 24,
            'drain_time_hr': ponding_depth_ft * 12 / self.infiltration_rate
        }

    def design_details(self, surface_area_sf: float) -> Dict:
        """Generate design details for bioretention"""
        return {
            'surface_area_sf': surface_area_sf,
            'filter_media': {
                'depth_in': 24,
                'composition': '50% sand, 30% comite, 20% mulch (top)',
                'permeability_in_hr': self.infiltration_rate
            },
            'underdrain': {
                'diameter_in': 4,
                'material': 'Perforated PVC',
                'slope_pct': 0.5,
                'gravel_depth_in': 12
            },
            'overflow': {
                'type': 'Standpipe or weir',
                'elevation': '6 inches above media surface'
            },
            'plants': {
                'density': '1 per 3 sq ft',
                'recommended': ['Switchgrass', 'Black-eyed Susan', 'Sedges']
            },
            'maintenance': {
                'mulch_replacement': 'Annual',
                'vegetation_maintenance': 'Biannual',
                'sediment_removal': 'As needed, typically 5-year'
            }
        }

# Example usage
bio = BioretentionDesign(infiltration_rate_in_hr=1.5)

sizing = bio.size_for_water_quality(
    drainage_area_sf=43560,  # 1 acre
    impervious_fraction=0.6,
    design_rainfall_in=1.0
)

print(f"Water quality volume: {sizing['water_quality_volume_cf']:.0f} cf")
print(f"Recommended area: {sizing['recommended_area_sf']:.0f} sf")
print(f"Drain time: {sizing['drain_time_hr']:.1f} hours")

details = bio.design_details(sizing['recommended_area_sf'])
print(f"\nFilter media depth: {details['filter_media']['depth_in']} inches")
```

### Pollutant Load Analysis
```python
class PollutantLoading:
    """Stormwater pollutant load estimation"""

    # Event Mean Concentrations (mg/L) by land use
    EMC = {
        'residential': {'TSS': 101, 'TP': 0.38, 'TN': 2.5, 'Zn': 0.14},
        'commercial': {'TSS': 69, 'TP': 0.22, 'TN': 2.2, 'Zn': 0.22},
        'industrial': {'TSS': 85, 'TP': 0.26, 'TN': 2.0, 'Zn': 0.32},
        'highway': {'TSS': 142, 'TP': 0.34, 'TN': 3.2, 'Zn': 0.35},
        'open_space': {'TSS': 40, 'TP': 0.10, 'TN': 1.0, 'Zn': 0.05}
    }

    # BMP removal efficiencies (%)
    BMP_REMOVAL = {
        'bioretention': {'TSS': 85, 'TP': 60, 'TN': 50, 'Zn': 80},
        'wet_pond': {'TSS': 80, 'TP': 50, 'TN': 30, 'Zn': 60},
        'dry_pond': {'TSS': 60, 'TP': 20, 'TN': 15, 'Zn': 30},
        'grass_swale': {'TSS': 70, 'TP': 25, 'TN': 20, 'Zn': 40},
        'perm_pavement': {'TSS': 85, 'TP': 60, 'TN': 50, 'Zn': 70},
        'sand_filter': {'TSS': 85, 'TP': 50, 'TN': 35, 'Zn': 80}
    }

    def annual_load(self, area_acres: float, land_use: str,
                    annual_runoff_in: float, pollutant: str) -> float:
        """Calculate annual pollutant load (lbs/year)"""
        emc = self.EMC.get(land_use, self.EMC['residential']).get(pollutant, 0)

        # Load = EMC * Volume
        # Volume (L) = runoff (in) * area (acres) * 43560 sf/ac * 0.0254 m/in * 1000 L/m3
        volume_l = annual_runoff_in * 0.0254 * area_acres * 43560 * 0.0929 * 1000

        # Load in mg, convert to lbs
        load_mg = emc * volume_l
        load_lbs = load_mg / 453592

        return load_lbs

    def load_reduction(self, load_lbs: float, bmp_type: str,
                       pollutant: str) -> Dict:
        """Calculate load reduction from BMP"""
        efficiency = self.BMP_REMOVAL.get(bmp_type, {}).get(pollutant, 0) / 100
        removed = load_lbs * efficiency
        remaining = load_lbs - removed

        return {
            'initial_load_lbs': load_lbs,
            'removal_efficiency_pct': efficiency * 100,
            'load_removed_lbs': removed,
            'remaining_load_lbs': remaining
        }

# Example usage
loading = PollutantLoading()

# Calculate loads for a 50-acre commercial development
area = 50  # acres
annual_runoff = 30  # inches
land_use = 'commercial'

for pollutant in ['TSS', 'TP', 'TN']:
    load = loading.annual_load(area, land_use, annual_runoff, pollutant)
    reduction = loading.load_reduction(load, 'bioretention', pollutant)
    print(f"{pollutant}: {load:.1f} lbs/yr -> {reduction['remaining_load_lbs']:.1f} lbs/yr "
          f"({reduction['removal_efficiency_pct']:.0f}% removal)")
```

## Usage Guidelines

### When to Use This Skill
- Stormwater management plan development
- Green infrastructure design
- BMP selection and sizing
- MS4 permit compliance analysis
- Watershed planning and TMDL implementation

### Best Practices
1. **Match design storm** to local requirements
2. **Consider treatment train approaches** for multiple benefits
3. **Plan for maintenance access** in design
4. **Verify infiltration rates** with field testing
5. **Include pre-treatment** for high pollutant areas
6. **Monitor performance** for adaptive management

### Process Integration
- WW-004: Stormwater Management Planning (all phases)

## Dependencies

- numpy, scipy: Numerical calculations
- pandas: Data analysis
- pyswmm: SWMM model interaction (optional)

## References

- EPA SWMM Reference Manual
- ASCE Manual of Practice No. 77
- State-specific stormwater design manuals
- NCHRP Report 565 BMP Selection

``````

## 87 · 污水处理工艺运行优化

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/environmental-engineering/skills/wastewater-optimization

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/environmental-engineering/skills/wastewater-optimization/SKILL.md

``````markdown
---
name: wastewater-optimization
description: Specialized skill for biological and physical-chemical wastewater treatment process optimization with activated sludge modeling, nutrient removal, aeration efficiency, and energy minimization.
allowed-tools: Read, Grep, Write, Bash, Edit, Glob
category: Water and Wastewater Treatment
backlog-id: SK-002
metadata:
  author: babysitter-sdk
  version: "1.0.0"
graph:
  domains: [domain:environmental-engineering]
  skillAreas: [skill-area:data-analysis, skill-area:statistical-analysis, skill-area:geospatial-data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer]
---

# Wastewater Treatment Optimization Skill

Biological and physical-chemical wastewater treatment process optimization for municipal and industrial applications.

## Purpose

This skill provides comprehensive capabilities for optimizing wastewater treatment processes, including activated sludge modeling, nutrient removal optimization, aeration efficiency analysis, and energy consumption minimization.

## Capabilities

### Activated Sludge Process Modeling
- ASM1, ASM2d, ASM3 model implementation
- Stoichiometric and kinetic parameter estimation
- Model calibration with plant data
- Steady-state and dynamic simulation
- Sensitivity analysis for key parameters

### BioWin and GPS-X Integration
- Model input file generation
- Simulation scenario configuration
- Results parsing and analysis
- Automated optimization runs
- Comparative scenario analysis

### Nutrient Removal Optimization
- Biological Nutrient Removal (BNR) process design
- Enhanced Biological Phosphorus Removal (EBPR) optimization
- Nitrification/denitrification kinetics
- Carbon source requirements
- Recycle ratio optimization

### Aeration Efficiency Analysis
- Oxygen transfer efficiency (OTE) calculation
- Alpha and beta factor determination
- Diffuser performance assessment
- Blower energy optimization
- DO control strategy evaluation

### Sludge Age and F/M Ratio Optimization
- Solids Retention Time (SRT) optimization
- Food-to-Microorganism (F/M) ratio analysis
- MLSS concentration control
- Sludge yield prediction
- WAS flow optimization

### Energy Consumption Minimization
- Energy audit methodology
- Aeration energy optimization
- Pumping efficiency analysis
- Process control optimization
- Energy benchmarking

### Chemical Dosing Optimization
- Coagulant dose optimization
- Polymer selection and dosing
- pH adjustment requirements
- Phosphorus precipitation
- Chemical cost minimization

### Secondary Clarifier Modeling
- Settling velocity analysis
- Solids flux theory application
- State point analysis
- Clarifier capacity evaluation
- Return sludge optimization

## Prerequisites

### Installation
```bash
pip install numpy scipy pandas matplotlib
```

### Optional Dependencies
```bash
# For process simulation
pip install python-control

# For optimization
pip install scipy pymoo

# For data visualization
pip install plotly seaborn
```

## Usage Patterns

### Activated Sludge Mass Balance
```python
import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class WastewaterCharacteristics:
    """Influent wastewater characteristics"""
    flow_mgd: float  # Million gallons per day
    bod5_mg_l: float  # 5-day BOD
    tss_mg_l: float  # Total suspended solids
    tkn_mg_l: float  # Total Kjeldahl Nitrogen
    tp_mg_l: float  # Total phosphorus
    temperature_c: float = 20.0

@dataclass
class ActivatedSludgeParameters:
    """Kinetic and stoichiometric parameters"""
    Y: float = 0.6  # Yield coefficient (g VSS/g BOD)
    kd: float = 0.06  # Endogenous decay rate (1/day)
    mu_max: float = 6.0  # Maximum specific growth rate (1/day)
    Ks: float = 60.0  # Half-saturation constant (mg/L BOD)
    theta_Y: float = 1.0  # Temperature coefficient for Y
    theta_kd: float = 1.04  # Temperature coefficient for kd

class ActivatedSludgeModel:
    """Simplified activated sludge process model"""

    def __init__(self, influent: WastewaterCharacteristics,
                 params: ActivatedSludgeParameters):
        self.influent = influent
        self.params = params

    def calculate_srt_for_effluent(self, target_bod_eff: float) -> float:
        """Calculate required SRT for target effluent BOD"""
        S = target_bod_eff
        S0 = self.influent.bod5_mg_l
        Y = self.params.Y
        kd = self.params.kd
        mu_max = self.params.mu_max
        Ks = self.params.Ks

        # Specific growth rate at effluent concentration
        mu = mu_max * S / (Ks + S)

        # Minimum SRT (washout)
        srt_min = 1 / (mu - kd)

        return srt_min * 1.5  # Safety factor

    def calculate_oxygen_requirement(self, srt_days: float, target_bod_eff: float) -> Dict:
        """Calculate oxygen requirements"""
        Q = self.influent.flow_mgd * 3.785  # Convert to m3/day * 1000 L/m3
        S0 = self.influent.bod5_mg_l
        S = target_bod_eff
        Y = self.params.Y
        kd = self.params.kd

        # BOD removal
        bod_removed = (S0 - S) * Q / 1000  # kg/day

        # Biomass production
        Px = Y * bod_removed / (1 + kd * srt_days)

        # Oxygen for BOD oxidation
        O2_bod = bod_removed - 1.42 * Px

        # Oxygen for endogenous respiration
        O2_endo = 1.42 * kd * Px * srt_days

        return {
            'bod_removed_kg_day': bod_removed,
            'biomass_produced_kg_day': Px,
            'O2_for_bod_kg_day': O2_bod,
            'O2_for_endogenous_kg_day': O2_endo,
            'total_O2_kg_day': O2_bod + O2_endo
        }

    def calculate_aeration_basin_volume(self, srt_days: float,
                                        mlss_mg_l: float) -> float:
        """Calculate required aeration basin volume"""
        Q = self.influent.flow_mgd * 3785.41  # m3/day
        S0 = self.influent.bod5_mg_l
        S = 10  # Target effluent BOD
        Y = self.params.Y
        kd = self.params.kd

        # Calculate biomass
        Px = Y * (S0 - S) / (1 + kd * srt_days)  # mg VSS/L influent

        # Assume VSS/TSS ratio
        vss_tss_ratio = 0.8
        mlvss = mlss_mg_l * vss_tss_ratio

        # Volume calculation
        volume_m3 = (Q * Px * srt_days) / mlvss

        return volume_m3

# Example usage
influent = WastewaterCharacteristics(
    flow_mgd=10.0,
    bod5_mg_l=200,
    tss_mg_l=220,
    tkn_mg_l=40,
    tp_mg_l=8,
    temperature_c=18
)

params = ActivatedSludgeParameters()
model = ActivatedSludgeModel(influent, params)

srt = model.calculate_srt_for_effluent(target_bod_eff=10)
print(f"Required SRT: {srt:.1f} days")

o2_req = model.calculate_oxygen_requirement(srt, target_bod_eff=10)
print(f"Oxygen requirement: {o2_req['total_O2_kg_day']:.0f} kg/day")

volume = model.calculate_aeration_basin_volume(srt, mlss_mg_l=3000)
print(f"Aeration basin volume: {volume:.0f} m3")
```

### Aeration Efficiency Optimization
```python
import numpy as np

class AerationAnalysis:
    """Aeration system efficiency analysis"""

    def __init__(self, basin_depth_m: float, diffuser_type: str = 'fine_bubble'):
        self.basin_depth = basin_depth_m
        self.diffuser_type = diffuser_type

        # Standard oxygen transfer efficiencies
        self.sote_per_m = {
            'fine_bubble': 0.06,  # 6% per meter depth
            'coarse_bubble': 0.02,  # 2% per meter depth
            'surface_aerator': 0.015  # per meter equivalent
        }

    def calculate_sote(self) -> float:
        """Calculate Standard Oxygen Transfer Efficiency"""
        base_sote = self.sote_per_m.get(self.diffuser_type, 0.04)
        return base_sote * self.basin_depth

    def calculate_aote(self, temperature_c: float, do_mg_l: float,
                       alpha: float = 0.5, beta: float = 0.95,
                       altitude_m: float = 0) -> float:
        """Calculate Actual Oxygen Transfer Efficiency"""
        # Saturation DO at standard conditions
        Cs_20 = 9.09  # mg/L at 20C, sea level

        # Temperature correction for DO saturation
        Cs_T = 14.62 - 0.3898 * temperature_c + 0.006969 * temperature_c**2

        # Altitude correction
        P_ratio = np.exp(-altitude_m / 8500)

        # Theta factor for temperature
        theta = 1.024

        # Calculate AOTE
        sote = self.calculate_sote()
        aote = sote * alpha * ((beta * Cs_T * P_ratio - do_mg_l) / Cs_20) * \
               theta ** (temperature_c - 20)

        return aote

    def calculate_air_flow(self, o2_required_kg_hr: float,
                           aote: float) -> float:
        """Calculate required air flow rate"""
        # Air is ~23% oxygen by mass
        # Standard air density ~1.2 kg/m3
        o2_fraction = 0.23
        air_density = 1.2  # kg/m3

        # O2 in air = 1.2 * 0.23 = 0.276 kg O2/m3 air
        o2_per_m3_air = air_density * o2_fraction

        # Air flow required
        air_flow_m3_hr = o2_required_kg_hr / (o2_per_m3_air * aote)

        return air_flow_m3_hr

    def calculate_blower_power(self, air_flow_m3_hr: float,
                               inlet_pressure_kpa: float = 101.325,
                               discharge_pressure_kpa: float = 150,
                               efficiency: float = 0.70) -> float:
        """Calculate blower power requirement"""
        # Adiabatic compression
        gamma = 1.4  # Air specific heat ratio

        # Pressure ratio
        p_ratio = discharge_pressure_kpa / inlet_pressure_kpa

        # Convert to m3/s
        Q = air_flow_m3_hr / 3600

        # Adiabatic head calculation
        head_kj_kg = (gamma / (gamma - 1)) * (inlet_pressure_kpa / 1.2) * \
                     ((p_ratio ** ((gamma - 1) / gamma)) - 1)

        # Power in kW
        power_kw = (Q * 1.2 * head_kj_kg) / efficiency

        return power_kw

# Example usage
aeration = AerationAnalysis(basin_depth_m=5.0, diffuser_type='fine_bubble')

sote = aeration.calculate_sote()
print(f"SOTE: {sote*100:.1f}%")

aote = aeration.calculate_aote(temperature_c=18, do_mg_l=2.0, alpha=0.5)
print(f"AOTE: {aote*100:.1f}%")

air_flow = aeration.calculate_air_flow(o2_required_kg_hr=500, aote=aote)
print(f"Air flow required: {air_flow:.0f} m3/hr")

power = aeration.calculate_blower_power(air_flow_m3_hr=air_flow)
print(f"Blower power: {power:.0f} kW")
```

### Nutrient Removal Analysis
```python
class NutrientRemoval:
    """Nutrient removal process analysis"""

    def __init__(self):
        self.nitrification_rate_20c = 0.08  # g N/(g VSS*day) at 20C
        self.denitrification_rate_20c = 0.1  # g N/(g VSS*day) at 20C

    def calculate_nitrification_srt(self, temperature_c: float,
                                    safety_factor: float = 2.0) -> float:
        """Calculate minimum SRT for nitrification"""
        # Nitrifier parameters
        mu_max_20 = 0.8  # 1/day at 20C
        kd_n = 0.04  # 1/day
        theta = 1.07

        # Temperature correction
        mu_max = mu_max_20 * theta ** (temperature_c - 20)

        # Minimum SRT
        srt_min = 1 / (mu_max - kd_n)

        return srt_min * safety_factor

    def calculate_carbon_for_denitrification(self, no3_to_remove_mg_l: float,
                                             flow_mgd: float,
                                             carbon_source: str = 'methanol') -> Dict:
        """Calculate external carbon requirement for denitrification"""
        # Carbon requirements (g COD/g N removed)
        carbon_ratios = {
            'methanol': 3.0,
            'ethanol': 4.0,
            'acetic_acid': 3.5,
            'raw_wastewater': 4.5
        }

        ratio = carbon_ratios.get(carbon_source, 4.0)

        # Convert flow
        flow_m3_day = flow_mgd * 3785.41

        # N mass to remove
        n_mass_kg_day = no3_to_remove_mg_l * flow_m3_day / 1000

        # COD required
        cod_kg_day = n_mass_kg_day * ratio

        return {
            'nitrate_removed_kg_day': n_mass_kg_day,
            'cod_required_kg_day': cod_kg_day,
            'carbon_source': carbon_source,
            'ratio_used': ratio
        }

    def calculate_ebpr_capacity(self, vfa_mg_l: float, flow_mgd: float) -> Dict:
        """Estimate EBPR phosphorus removal capacity"""
        # VFA uptake ratio: ~10-15 mg VFA-COD per mg P removed
        vfa_p_ratio = 12  # mg VFA-COD / mg P

        # Convert flow
        flow_m3_day = flow_mgd * 3785.41

        # VFA mass available
        vfa_mass_kg_day = vfa_mg_l * flow_m3_day / 1000

        # P removal potential
        p_removal_kg_day = vfa_mass_kg_day / (vfa_p_ratio / 1000)

        return {
            'vfa_available_kg_day': vfa_mass_kg_day,
            'p_removal_potential_kg_day': p_removal_kg_day,
            'p_removal_concentration_mg_l': (p_removal_kg_day * 1000) / flow_m3_day
        }

# Example usage
nutrient = NutrientRemoval()

srt = nutrient.calculate_nitrification_srt(temperature_c=15)
print(f"Minimum SRT for nitrification at 15C: {srt:.1f} days")

carbon = nutrient.calculate_carbon_for_denitrification(
    no3_to_remove_mg_l=20,
    flow_mgd=10,
    carbon_source='methanol'
)
print(f"Methanol COD required: {carbon['cod_required_kg_day']:.0f} kg/day")

ebpr = nutrient.calculate_ebpr_capacity(vfa_mg_l=50, flow_mgd=10)
print(f"EBPR P removal potential: {ebpr['p_removal_concentration_mg_l']:.1f} mg/L")
```

## Usage Guidelines

### When to Use This Skill
- Wastewater treatment process design and optimization
- Energy efficiency improvement projects
- Nutrient removal system upgrades
- Process troubleshooting and capacity analysis
- Chemical dosing optimization

### Best Practices
1. **Calibrate models** with plant-specific data
2. **Consider seasonal variations** in temperature and loading
3. **Account for diurnal variations** in flow and load
4. **Verify model predictions** with plant performance data
5. **Include safety factors** for critical processes like nitrification
6. **Optimize holistically** considering interactions between processes

### Process Integration
- WW-002: Wastewater Process Optimization (all phases)
- WW-001: Water Treatment Plant Design (optimization phases)

## Dependencies

- numpy: Numerical calculations
- scipy: Optimization routines
- pandas: Data analysis

## References

- Metcalf & Eddy, "Wastewater Engineering: Treatment and Resource Recovery"
- Water Environment Federation, "Nutrient Removal" (MOP 34)
- Henze et al., "Activated Sludge Models ASM1, ASM2, ASM2d and ASM3"

``````

## 88 · CAN与CAN-FD总线分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/embedded-systems/skills/can-bus

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/embedded-systems/skills/can-bus/SKILL.md

``````markdown
---
name: can-bus
description: CAN/CAN-FD bus analysis and development expertise
category: Communication Protocols
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
graph:
  domains: [domain:embedded-systems]
  specializations: [specialization:embedded-systems]
  skillAreas: [skill-area:rtos-programming, skill-area:firmware-development]
  roles: [role:embedded-engineer]
---

# CAN Bus Skill

## Overview

This skill provides comprehensive CAN and CAN-FD bus analysis, development, and debugging capabilities for automotive and industrial embedded systems.

## Capabilities

### Message Frame Operations
- CAN message frame generation
- Frame analysis and decoding
- Identifier filtering and masking
- Standard (11-bit) and extended (29-bit) IDs
- Remote frame handling

### DBC File Support
- DBC file parsing and generation
- Signal decoding and encoding
- Message definition management
- Physical value scaling
- Multiplexed signal support

### Protocol Support
- CAN 2.0A/B compliance
- CAN-FD configuration and validation
- J1939 transport protocol
- CANopen communication
- UDS (ISO 14229) diagnostics
- ISO-TP (ISO 15765-2)

### Bus Analysis
- Bus arbitration analysis
- Error frame detection and analysis
- Bus-off recovery monitoring
- Bus load calculation
- Bit timing verification
- Network topology analysis

### Gateway Operations
- Message routing configuration
- Gateway bridge setup
- Protocol translation
- Filtering and forwarding rules

## Target Processes

- `device-driver-development.js` - CAN driver implementation
- `signal-integrity-testing.js` - CAN bus signal validation
- `hw-sw-interface-specification.js` - CAN interface definition
- `functional-safety-certification.js` - CAN safety requirements

## Dependencies

- CAN interface tools (PEAK, Vector, Kvaser)
- DBC files for signal decoding
- CAN analyzer hardware
- SocketCAN (Linux)

## Usage Context

This skill is invoked when tasks require:
- CAN driver development
- Bus communication debugging
- DBC-based signal analysis
- Protocol stack implementation
- Automotive networking

## Configuration Examples

### CAN Bit Timing
```yaml
can:
  bitrate: 500000  # 500 kbps
  sample_point: 87.5
  sjw: 1
  seg1: 13
  seg2: 2
  prescaler: 4
```

### CAN-FD Configuration
```yaml
can_fd:
  nominal_bitrate: 500000
  data_bitrate: 2000000
  brs: enabled  # Bit Rate Switch
  esi: enabled  # Error State Indicator
```

### DBC Signal Definition
```dbc
BO_ 0x123 EngineData: 8 ECU
 SG_ EngineRPM : 0|16@1+ (0.25,0) [0|16383.75] "rpm" Vector__XXX
 SG_ EngineTemp : 16|8@1+ (1,-40) [-40|215] "C" Vector__XXX
```

``````

## 89 · 嵌入式硬件环境应力试验

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/embedded-systems/skills/environmental-stress-testing

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/embedded-systems/skills/environmental-stress-testing/SKILL.md

``````markdown
---
name: environmental-stress-testing
description: Design and execute environmental stress tests for embedded hardware — temperature cycling, vibration, humidity, and EMC validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
graph:
  domains: [domain:embedded-systems]
  specializations: [specialization:embedded-systems]
  skillAreas: [skill-area:environmental-stress-testing]
  roles: [role:embedded-engineer]
---

# Environmental Stress Testing Skill

> Stub — implementation pending.

``````

## 90 · 嵌入式实时响应分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/embedded-systems/skills/real-time-behavior-testing

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/embedded-systems/skills/real-time-behavior-testing/SKILL.md

``````markdown
---
name: real-time-behavior-testing
description: Validate real-time behavior in embedded systems — timing constraints, interrupt latency, and RTOS task scheduling verification.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
graph:
  domains: [domain:embedded-systems]
  specializations: [specialization:embedded-systems]
  skillAreas: [skill-area:real-time-behavior-testing]
  roles: [role:embedded-engineer]
---

# Real-time Behavior Testing Skill

> Stub — implementation pending.

``````
