# 第三批完整原始说明（分类修订版）

## 61 航空气动数据库整理

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/aero-database/SKILL.md

``````markdown
---
name: aero-database
description: Systematic generation and management of aerodynamic coefficient databases
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - aerodynamics
    - database
    - coefficients
    - simulation
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:data-analysis]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Aerodynamic Database Generation Skill

## Purpose
Systematically generate, manage, and maintain aerodynamic coefficient databases for flight simulation, stability analysis, and performance prediction.

## Capabilities
- Multi-dimensional parameter sweep configuration
- Automated CFD job submission and monitoring
- Force and moment coefficient extraction
- Database interpolation and extrapolation
- Format conversion for flight simulation
- Database validation and consistency checks
- Version control and change tracking
- Documentation and metadata management

## Usage Guidelines
- Define comprehensive parameter ranges covering the flight envelope
- Ensure adequate resolution in critical regions (transonic, high angle of attack)
- Validate database consistency across parameter boundaries
- Implement robust interpolation schemes for smooth coefficient variations
- Maintain version control for database updates and modifications
- Document data sources, assumptions, and limitations

## Dependencies
- Database tools
- HPC job schedulers
- MATLAB
- Python data processing libraries

## Process Integration
- AE-003: Aerodynamic Database Generation
- AE-013: Flight Simulation Model Development

``````

## 62 航空气动弹性分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/aeroelastic-analysis/SKILL.md

``````markdown
---
name: aeroelastic-analysis
description: Skill for flutter, divergence, and aeroelastic response analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - structural-analysis
    - aeroelasticity
    - flutter
    - dynamics
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:sensor-fusion]
  roles: [role:research-engineer, role:computational-scientist]
---

# Aeroelastic Analysis Skill

## Purpose
Provide comprehensive aeroelastic analysis capabilities for flutter prevention, divergence assessment, and dynamic response prediction.

## Capabilities
- Flutter analysis (p-k, PKNL methods)
- Divergence speed determination
- Control reversal analysis
- Gust response analysis
- Ground vibration test correlation
- Aeroelastic tailoring assessment
- Structural coupling analysis
- Flight envelope clearance documentation

## Usage Guidelines
- Validate structural modes against GVT data before flutter analysis
- Use appropriate aerodynamic theories for the flight regime
- Include control system effects in flutter predictions
- Apply required flutter margins per certification requirements
- Consider fuel state and payload variations in analysis matrix
- Document all modeling assumptions and uncertainties

## Dependencies
- MSC NASTRAN (SOL 144/145/146)
- ZAERO
- FlightLoads

## Process Integration
- AE-010: Aeroelastic Analysis

``````

## 63 航空电子系统集成

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/avionics-integration/SKILL.md

``````markdown
---
name: avionics-integration
description: Skill for avionics architecture design and system integration
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - avionics
    - integration
    - architecture
    - systems
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:physics-simulation, skill-area:mathematical-reasoning]
  roles: [role:systems-integration-engineer, role:research-engineer]
---

# Avionics System Integration Skill

## Purpose
Enable avionics architecture design and system integration including bus protocols, redundancy management, and human-machine interface design.

## Capabilities
- Avionics architecture definition
- ARINC 429/664 bus specification
- Federated vs IMA architecture
- Redundancy management design
- Data loading requirements
- Built-in test (BIT) requirements
- Human-machine interface specification
- Crew alerting system design

## Usage Guidelines
- Define avionics architecture based on safety and performance requirements
- Select appropriate bus protocols for data rate and criticality
- Design redundancy to meet system safety requirements
- Implement comprehensive built-in test capabilities
- Design crew interfaces following human factors principles
- Coordinate with certification for novel avionics features

## Dependencies
- Avionics specification tools
- Bus analysis tools
- Human factors guidelines

## Process Integration
- Systems integration processes
- Avionics certification planning

``````

## 64 航空复合材料结构设计

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/composite-structures/SKILL.md

``````markdown
---
name: composite-structures
description: Expert skill for composite aerospace structure design and analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - structural-analysis
    - composites
    - laminate-design
    - materials
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:statistical-analysis]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Composite Structures Skill

## Purpose
Enable expert composite aerospace structure design and analysis including laminate optimization, failure prediction, and manufacturing considerations.

## Capabilities
- Laminate analysis and optimization
- Classical laminate theory (CLT) calculations
- Ply failure criteria (Tsai-Wu, Hashin, LaRC)
- Stacking sequence optimization
- Manufacturing constraint consideration
- Repair analysis and substantiation
- Allowables database management
- Impact damage assessment

## Usage Guidelines
- Apply appropriate failure criteria based on loading and material system
- Consider manufacturing constraints in laminate design (ply drops, tool access)
- Use building block approach for allowables development
- Account for environmental effects (temperature, moisture)
- Design for inspectability and repairability
- Document material and process specifications completely

## Dependencies
- HyperSizer
- ESACOMP
- Laminate tools
- NASTRAN

## Process Integration
- AE-009: Composite Structure Design

``````

## 65 航空疲劳与损伤容限分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/fatigue-dt/SKILL.md

``````markdown
---
name: fatigue-dt
description: Specialized skill for fatigue life prediction and damage tolerance assessment
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - structural-analysis
    - fatigue
    - damage-tolerance
    - certification
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  roles: [role:research-engineer, role:computational-scientist]
---

# Fatigue and Damage Tolerance Skill

## Purpose
Provide specialized fatigue life prediction and damage tolerance assessment capabilities for airworthiness certification and structural integrity management.

## Capabilities
- S-N and strain-life analysis
- Crack growth analysis (NASGRO, AFGROW)
- Inspection interval determination
- Damage tolerance substantiation
- Spectrum loading analysis
- Mean stress correction methods
- Multi-site damage assessment
- Certification evidence generation

## Usage Guidelines
- Use appropriate fatigue methodology based on structural criticality
- Select material data from qualified sources (MMPDS, ESDU)
- Apply appropriate scatter factors per regulatory requirements
- Consider environmental effects on fatigue and crack growth
- Define inspection intervals with adequate safety margins
- Document all assumptions and conservatisms in certification reports

## Dependencies
- NASGRO
- AFGROW
- Fe-Safe
- nCode DesignLife

## Process Integration
- AE-008: Fatigue and Damage Tolerance
- AE-021: Certification Planning

``````

## 66 飞行仿真模型构建

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/flight-sim-model/SKILL.md

``````markdown
---
name: flight-sim-model
description: Skill for creating and validating flight dynamics models
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - flight-dynamics
    - simulation
    - modeling
    - validation
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:sensor-fusion]
  roles: [role:research-engineer, role:computational-scientist]
---

# Flight Simulation Model Skill

## Purpose
Create and validate high-fidelity flight dynamics models for training simulators, engineering analysis, and flight test support.

## Capabilities
- Six-DOF equation of motion implementation
- Aerodynamic database integration
- Propulsion model integration
- Landing gear and ground dynamics
- Atmospheric modeling (ISA, GRAM)
- Sensor and actuator modeling
- Model validation against flight data
- Real-time simulation interface

## Usage Guidelines
- Use validated aerodynamic databases from CFD and wind tunnel data
- Implement accurate propulsion models for all operating conditions
- Include realistic actuator dynamics and limitations
- Validate model against flight test data where available
- Document model fidelity and limitations
- Ensure real-time performance for pilot-in-the-loop applications

## Dependencies
- MATLAB/Simulink
- JSBSim
- FlightGear
- X-Plane

## Process Integration
- AE-013: Flight Simulation Model Development
- AE-024: Flight Test Planning

``````

## 67 飞行试验策划

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/flight-test-planning/SKILL.md

``````markdown
---
name: flight-test-planning
description: Skill for comprehensive flight test planning and execution support
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - testing
    - flight-test
    - validation
    - certification
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:statistical-analysis, skill-area:physics-simulation]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Flight Test Planning Skill

## Purpose
Provide comprehensive flight test planning capabilities including test point definition, instrumentation specification, and safety analysis.

## Capabilities
- Test point definition and prioritization
- Test card generation
- Instrumentation requirements specification
- Safety of flight analysis
- Flight test technique selection
- Data analysis planning
- Risk assessment and mitigation
- Test schedule optimization

## Usage Guidelines
- Define clear test objectives aligned with certification requirements
- Prioritize test points based on risk and criticality
- Specify instrumentation to capture required data
- Conduct thorough safety of flight analysis before each test
- Select appropriate test techniques for each maneuver
- Plan for real-time monitoring and abort criteria

## Dependencies
- Flight test management tools
- Data analysis systems
- Telemetry systems

## Process Integration
- AE-024: Flight Test Planning

``````

## 68 航空航天制导导航控制仿真

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/gnc-simulation/SKILL.md

``````markdown
---
name: gnc-simulation
description: Skill for guidance, navigation, and control system simulation and analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - flight-dynamics
    - gnc
    - navigation
    - simulation
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:sensor-fusion]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# GNC Simulation Skill

## Purpose
Provide guidance, navigation, and control system simulation and analysis capabilities including sensor modeling, filter design, and Monte Carlo analysis.

## Capabilities
- Navigation filter design (EKF, UKF)
- Sensor error modeling (IMU, GPS, star tracker)
- Guidance law implementation
- Monte Carlo simulation execution
- Covariance analysis
- Hardware-in-the-loop support
- Trajectory dispersion analysis
- Performance verification

## Usage Guidelines
- Model sensor errors accurately based on specifications
- Design navigation filters robust to expected error sources
- Implement guidance algorithms for mission requirements
- Run Monte Carlo simulations with realistic dispersions
- Verify GNC performance across operational envelope
- Document filter tuning and performance validation

## Dependencies
- MATLAB/Simulink
- GNC simulation frameworks
- HIL test systems

## Process Integration
- AE-011: Flight Control Law Development
- AE-014: Mission Design and Analysis

``````

## 69 飞行操纵品质分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/handling-qualities/SKILL.md

``````markdown
---
name: handling-qualities
description: Specialized skill for aircraft handling qualities evaluation
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - flight-dynamics
    - handling-qualities
    - pilot-interface
    - certification
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:sensor-fusion]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Handling Qualities Assessment Skill

## Purpose
Provide specialized handling qualities evaluation capabilities for aircraft certification and pilot-vehicle interface optimization.

## Capabilities
- MIL-STD-1797 compliance checking
- Cooper-Harper rating prediction
- Time response criteria evaluation
- Frequency response requirements
- PIO susceptibility analysis
- Category/Phase/Level determination
- Pilot opinion correlation
- Flying qualities demonstration planning

## Usage Guidelines
- Define appropriate flight phases and categories for evaluation
- Apply correct criteria based on aircraft class and mission
- Consider pilot workload and task performance
- Evaluate PIO susceptibility across frequency range
- Correlate analytical predictions with pilot evaluations
- Document handling qualities substantiation for certification

## Dependencies
- MATLAB
- Flying qualities tools
- Simulation interfaces

## Process Integration
- AE-012: Handling Qualities Assessment
- AE-011: Flight Control Law Development

``````

## 70 高超声速气动热分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/hypersonic-aerothermo/SKILL.md

``````markdown
---
name: hypersonic-aerothermo
description: Specialized skill for hypersonic vehicle aerodynamic and thermal analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - aerodynamics
    - hypersonic
    - aerothermodynamics
    - thermal-protection
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:computational-geometry]
  roles: [role:research-engineer, role:computational-scientist]
---

# Hypersonic Aerothermodynamics Skill

## Purpose
Provide specialized hypersonic vehicle aerodynamic and thermal analysis capabilities including real gas effects, aerodynamic heating, and thermal protection system design.

## Capabilities
- High-temperature gas dynamics
- Real gas effects modeling
- Aerodynamic heating prediction
- Thermal protection system sizing
- Shock-boundary layer interaction
- Ablation modeling
- Transition prediction (hypersonic)
- Chemically reacting flow analysis

## Usage Guidelines
- Account for real gas and chemical non-equilibrium effects
- Use appropriate turbulence models for hypersonic boundary layers
- Predict transition location and heating augmentation
- Size TPS with adequate margins for heating uncertainty
- Consider ablation effects on aerodynamic shape
- Validate predictions against ground test data where available

## Dependencies
- High-fidelity CFD codes
- Real-gas models
- Thermal protection system design tools

## Process Integration
- AE-001: CFD Analysis Workflow (hypersonic regime)
- Advanced hypersonic vehicle design processes

``````

## 71 航空航天任务轨迹分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/mission-trajectory/SKILL.md

``````markdown
---
name: mission-trajectory
description: Expert skill for space mission design and trajectory analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - space-systems
    - trajectory
    - orbital-mechanics
    - mission-design
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:computational-geometry]
  roles: [role:research-engineer, role:computational-scientist]
---

# Mission Design and Trajectory Skill

## Purpose
Enable comprehensive space mission design and trajectory analysis including orbital mechanics, launch window optimization, and maneuver planning.

## Capabilities
- Orbital mechanics calculations
- Launch window analysis
- Delta-V budgeting and optimization
- Transfer trajectory design
- Maneuver planning and sequencing
- Rendezvous and proximity operations
- Entry, descent, and landing analysis
- STK and GMAT integration

## Usage Guidelines
- Define clear mission objectives and constraints
- Optimize trajectories for propellant mass or time of flight
- Consider launch vehicle performance and constraints
- Account for perturbations in trajectory propagation
- Plan contingency maneuvers for off-nominal conditions
- Document trajectory design assumptions and margins

## Dependencies
- STK (Systems Tool Kit)
- GMAT
- MATLAB Aerospace Toolbox

## Process Integration
- AE-014: Mission Design and Analysis

``````

## 72 轨道碎片风险分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/orbital-debris/SKILL.md

``````markdown
---
name: orbital-debris
description: Skill for orbital debris risk assessment and mitigation planning
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - space-systems
    - debris
    - risk-assessment
    - compliance
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Orbital Debris Assessment Skill

## Purpose
Provide comprehensive orbital debris risk assessment capabilities for collision avoidance, debris mitigation compliance, and long-term orbit sustainability.

## Capabilities
- Collision probability calculation
- Debris environment modeling (ORDEM, MASTER)
- Conjunction assessment
- Collision avoidance maneuver planning
- Post-mission disposal planning
- Debris mitigation guideline compliance
- Shielding assessment
- Long-term orbit evolution

## Usage Guidelines
- Use current debris environment models for risk assessment
- Calculate collision probability for critical mission phases
- Plan avoidance maneuvers with sufficient lead time
- Design for post-mission disposal compliance
- Consider shielding for high-risk debris encounters
- Document debris mitigation measures for licensing

## Dependencies
- DAS (Debris Assessment Software)
- ORDEM
- STK

## Process Integration
- AE-017: Orbital Debris Assessment

``````

## 73 航空推进系统试验分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/propulsion-test-analysis/SKILL.md

``````markdown
---
name: propulsion-test-analysis
description: Skill for propulsion system ground test data acquisition and analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - propulsion
    - testing
    - data-acquisition
    - validation
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:sensor-fusion]
  roles: [role:research-engineer, role:lab-technician]
---

# Propulsion Test Data Analysis Skill

## Purpose
Support propulsion system ground testing through comprehensive data acquisition configuration, real-time analysis, and test-to-prediction correlation.

## Capabilities
- Test cell instrumentation configuration
- Data acquisition system setup
- Real-time performance calculation
- Test-to-prediction correlation
- Thrust stand calibration verification
- Measurement uncertainty analysis
- Test matrix optimization
- Health monitoring parameter tracking

## Usage Guidelines
- Verify instrumentation calibration before each test campaign
- Define clear success criteria and abort conditions
- Monitor critical parameters in real-time during testing
- Apply appropriate measurement corrections and uncertainty propagation
- Correlate test results with analytical predictions
- Document all test conditions, anomalies, and lessons learned

## Dependencies
- LabVIEW
- MATLAB
- Data acquisition systems
- Test cell control systems

## Process Integration
- AE-006: Propulsion System Testing

``````

## 74 火箭推进系统设计分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/rocket-propulsion/SKILL.md

``````markdown
---
name: rocket-propulsion
description: Comprehensive skill for rocket engine design and performance analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - propulsion
    - rocket
    - combustion
    - nozzle-design
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:computational-geometry]
  roles: [role:research-engineer, role:computational-scientist]
---

# Rocket Propulsion Analysis Skill

## Purpose
Enable comprehensive rocket engine design and performance analysis including combustion analysis, nozzle design, and propellant optimization.

## Capabilities
- CEA combustion analysis integration
- Nozzle design and optimization (bell, aerospike)
- Propellant selection and performance comparison
- Chamber pressure and mixture ratio optimization
- Regenerative cooling analysis
- Injector design considerations
- Thrust vectoring system analysis
- Rocket Propulsion Analysis (RPA) integration

## Usage Guidelines
- Use CEA for accurate combustion product calculations
- Optimize mixture ratio for specific impulse or thrust requirements
- Consider thermal management in chamber and nozzle design
- Account for real gas effects at high pressures
- Validate designs against empirical correlations and test data
- Document propellant properties and compatibility considerations

## Dependencies
- CEA (Chemical Equilibrium with Applications)
- RPA (Rocket Propulsion Analysis)
- MATLAB

## Process Integration
- AE-005: Rocket Propulsion Design

``````

## 75 航天器热控设计

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/aerospace-engineering/skills/spacecraft-thermal/SKILL.md

``````markdown
---
name: spacecraft-thermal
description: Skill for spacecraft thermal control system design and analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - WebFetch
  - WebSearch
  - Bash
metadata:
  version: "1.0"
  category: aerospace-engineering
  tags:
    - space-systems
    - thermal-control
    - analysis
    - design
graph:
  domains: [domain:aerospace-engineering]
  specializations: [specialization:aerospace-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:statistical-analysis]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# Spacecraft Thermal Analysis Skill

## Purpose
Provide comprehensive spacecraft thermal control system design and analysis capabilities for component temperature prediction and thermal management.

## Capabilities
- Thermal Desktop and SINDA modeling
- Orbital environment definition
- Radiator sizing and placement
- Heater control logic design
- Thermal balance verification
- Hot/cold case analysis
- Component temperature prediction
- MLI and coating specification

## Usage Guidelines
- Define worst-case thermal environments for hot and cold cases
- Use appropriate view factors and orbital parameters
- Size radiators with adequate margin for degradation
- Design heater circuits with redundancy for critical components
- Validate thermal models against test data
- Document thermal control system design and operating procedures

## Dependencies
- Thermal Desktop
- SINDA/FLUINT
- ESATAN

## Process Integration
- AE-015: Spacecraft Thermal Analysis

``````

## 76 Aspen Plus流程模拟

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/aspen-plus-simulator/SKILL.md

``````markdown
---
name: aspen-plus-simulator
description: Aspen Plus integration skill for steady-state process simulation, thermodynamic modeling, and equipment rating
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Simulation
  skill-id: CE-SK-001
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:statistical-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Aspen Plus Simulator Skill

## Purpose

The Aspen Plus Simulator Skill provides integration with Aspen Plus for steady-state process simulation, thermodynamic modeling, property estimation, and equipment design calculations.

## Capabilities

- Process flowsheet construction and simulation
- Thermodynamic model selection (NRTL, SRK, PRMHV2, UNIFAC)
- Property estimation (DIPPR, Joback methods)
- Equipment rating and design modes
- Sensitivity analysis and optimization
- Report generation and stream table export
- Convergence troubleshooting
- Custom unit operation modeling
- Economic analysis integration

## Usage Guidelines

### When to Use
- Developing process simulation models
- Evaluating thermodynamic properties
- Sizing and rating equipment
- Optimizing process conditions

### Prerequisites
- Process flow diagram available
- Component list defined
- Operating conditions specified
- Thermodynamic data requirements identified

### Best Practices
- Select appropriate thermodynamic models
- Validate against experimental data
- Document all assumptions
- Perform sensitivity analysis

## Process Integration

This skill integrates with:
- Process Flow Diagram Development
- Heat Integration Analysis
- Equipment Sizing and Specification

## Configuration

```yaml
aspen-plus-simulator:
  thermodynamic-models:
    - NRTL
    - SRK
    - Peng-Robinson
    - UNIFAC
  unit-operations:
    - columns
    - reactors
    - heat-exchangers
    - separators
```

## Output Artifacts

- Simulation files
- Stream tables
- Equipment specifications
- Optimization results
- Property reports

``````

## 77 化工催化剂性能分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/catalyst-analyzer/SKILL.md

``````markdown
---
name: catalyst-analyzer
description: Catalyst performance analysis skill for activity testing, deactivation modeling, and optimization
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Reaction Engineering
  skill-id: CE-SK-008
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:physics-simulation, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-scientist, role:lab-technician]
---

# Catalyst Analyzer Skill

## Purpose

The Catalyst Analyzer Skill evaluates catalyst performance, models deactivation kinetics, and supports catalyst selection and optimization for chemical processes.

## Capabilities

- Catalyst activity measurement analysis
- Selectivity evaluation
- Deactivation kinetics modeling
- Regeneration cycle optimization
- Catalyst screening support
- Turnover frequency calculation
- Surface area and porosity analysis
- Poison identification

## Usage Guidelines

### When to Use
- Evaluating catalyst candidates
- Modeling catalyst deactivation
- Optimizing regeneration cycles
- Troubleshooting performance decline

### Prerequisites
- Experimental data available
- Reaction mechanism understood
- Operating conditions defined
- Reference catalyst identified

### Best Practices
- Use consistent testing protocols
- Account for mass transfer effects
- Consider long-term stability
- Validate deactivation models

## Process Integration

This skill integrates with:
- Catalyst Evaluation and Optimization
- Kinetic Model Development
- Reactor Design and Selection

## Configuration

```yaml
catalyst-analyzer:
  analysis-types:
    - activity
    - selectivity
    - deactivation
    - regeneration
  catalyst-types:
    - heterogeneous
    - homogeneous
    - biocatalyst
```

## Output Artifacts

- Activity profiles
- Deactivation models
- Regeneration protocols
- Screening comparisons
- Recommendation reports

``````

## 78 化工事故后果建模

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/consequence-modeler/SKILL.md

``````markdown
---
name: consequence-modeler
description: Consequence analysis skill for dispersion modeling, fire/explosion analysis, and effect zone determination
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Safety
  skill-id: CE-SK-017
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Consequence Modeler Skill

## Purpose

The Consequence Modeler Skill performs consequence analysis for hazardous material releases including dispersion modeling, fire and explosion effects, and determination of effect zones.

## Capabilities

- Source term modeling
- Atmospheric dispersion (Gaussian, dense gas)
- Pool fire modeling
- Jet fire modeling
- Vapor cloud explosion (VCE) analysis
- BLEVE modeling
- Toxic effect assessment
- Effect zone mapping

## Usage Guidelines

### When to Use
- Quantifying release consequences
- Establishing effect zones
- Supporting siting studies
- Emergency planning

### Prerequisites
- Release scenarios defined
- Material properties available
- Site meteorological data
- Receptor locations identified

### Best Practices
- Use appropriate dispersion models
- Consider atmospheric stability
- Account for terrain effects
- Document modeling assumptions

## Process Integration

This skill integrates with:
- Consequence Analysis
- HAZOP Study Facilitation
- Emergency Response Planning

## Configuration

```yaml
consequence-modeler:
  models:
    - PHAST
    - ALOHA
    - custom-gaussian
  consequence-types:
    - toxic-dispersion
    - flammable-dispersion
    - fire
    - explosion
```

## Output Artifacts

- Consequence reports
- Effect zone maps
- Dispersion plots
- Fire/explosion analysis
- Risk contours

``````

## 79 化工腐蚀与材料选型

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/corrosion-materials-selector/SKILL.md

``````markdown
---
name: corrosion-materials-selector
description: Materials selection skill for corrosion resistance based on process conditions and industry standards
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Design
  skill-id: CE-SK-031
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:statistical-analysis, skill-area:data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:research-scientist]
---

# Corrosion Materials Selector Skill

## Purpose

The Corrosion Materials Selector Skill recommends materials of construction based on process conditions, corrosion mechanisms, and industry standards to ensure equipment reliability.

## Capabilities

- Corrosion mechanism identification
- Material screening
- Corrosion rate estimation
- Corrosion allowance calculation
- Material specification development
- Isocorrosion curve analysis
- Galvanic compatibility assessment
- Stress corrosion cracking evaluation
- Cost-benefit analysis

## Usage Guidelines

### When to Use
- Selecting materials for new equipment
- Evaluating corrosion failures
- Assessing process changes
- Specifying replacement materials

### Prerequisites
- Process conditions defined
- Chemical composition known
- Operating temperature/pressure specified
- Design life established

### Best Practices
- Consider all corrosion mechanisms
- Use conservative assumptions
- Reference industry standards
- Validate with experience data

## Process Integration

This skill integrates with:
- Equipment Sizing and Specification
- Process Flow Diagram Development
- HAZOP Study Facilitation

## Configuration

```yaml
corrosion-materials-selector:
  standards:
    - NACE
    - API
    - ASME
  material-classes:
    - carbon-steel
    - stainless-steel
    - nickel-alloys
    - non-metallics
```

## Output Artifacts

- Material recommendations
- Corrosion assessments
- Material specifications
- Cost comparisons
- Design life estimates

``````

## 80 化工设备尺寸设计

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/equipment-sizing-calculator/SKILL.md

``````markdown
---
name: equipment-sizing-calculator
description: Process equipment sizing skill using established engineering correlations and standards
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Simulation
  skill-id: CE-SK-005
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:mathematical-reasoning, skill-area:statistical-analysis, skill-area:physics-simulation]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Equipment Sizing Calculator Skill

## Purpose

The Equipment Sizing Calculator Skill performs process equipment sizing using established engineering correlations, industry standards, and manufacturer guidelines.

## Capabilities

- Vessel sizing (residence time, L/D ratios)
- Heat exchanger rating and design (TEMA methods)
- Pump sizing and NPSH calculations
- Compressor selection and performance
- Column sizing (flooding, weeping checks)
- Pressure drop calculations
- Agitator sizing
- Piping sizing

## Usage Guidelines

### When to Use
- Sizing process equipment
- Rating existing equipment
- Developing equipment specifications
- Evaluating design alternatives

### Prerequisites
- Process conditions defined
- Flow rates established
- Physical properties available
- Design codes identified

### Best Practices
- Apply appropriate design margins
- Follow applicable standards
- Consider operability requirements
- Document all assumptions

## Process Integration

This skill integrates with:
- Equipment Sizing and Specification
- Distillation Column Design
- Membrane Separation System Design

## Configuration

```yaml
equipment-sizing-calculator:
  equipment-types:
    - vessels
    - heat-exchangers
    - pumps
    - compressors
    - columns
  design-codes:
    - ASME
    - TEMA
    - API
```

## Output Artifacts

- Equipment datasheets
- Sizing calculations
- Specification sheets
- Design drawings

``````

## 81 绿色化学指标评估

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/green-chemistry-metrics/SKILL.md

``````markdown
---
name: green-chemistry-metrics
description: Green chemistry metrics calculation skill for atom economy, E-factor, and process mass intensity
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Sustainability
  skill-id: CE-SK-024
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:mathematical-reasoning, skill-area:data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-scientist, role:computational-scientist]
---

# Green Chemistry Metrics Skill

## Purpose

The Green Chemistry Metrics Skill calculates and evaluates green chemistry metrics to assess process sustainability and guide process improvement toward greener alternatives.

## Capabilities

- Atom economy calculation
- E-factor analysis
- Process mass intensity (PMI)
- Reaction mass efficiency
- Carbon efficiency
- Solvent intensity
- Energy intensity
- Water intensity
- Renewables fraction

## Usage Guidelines

### When to Use
- Evaluating process greenness
- Comparing synthesis routes
- Setting sustainability targets
- Tracking improvement progress

### Prerequisites
- Process stoichiometry defined
- Mass balance available
- Solvent usage documented
- Energy consumption known

### Best Practices
- Calculate multiple metrics
- Compare against benchmarks
- Track trends over time
- Consider full life cycle

## Process Integration

This skill integrates with:
- Green Chemistry Metrics Evaluation
- Process Sustainability Assessment
- Waste Minimization Analysis

## Configuration

```yaml
green-chemistry-metrics:
  metrics:
    - atom-economy
    - e-factor
    - pmi
    - carbon-efficiency
  benchmarks:
    - pharmaceutical
    - fine-chemical
    - commodity
```

## Output Artifacts

- Metrics calculations
- Benchmark comparisons
- Trend analyses
- Improvement recommendations
- Sustainability scorecards

``````

## 82 化工HAZOP分析组织

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/hazop-facilitator/SKILL.md

``````markdown
---
name: hazop-facilitator
description: HAZOP study facilitation skill for systematic deviation analysis and safeguard identification
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Safety
  skill-id: CE-SK-014
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:data-analysis, skill-area:compliance-automation]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# HAZOP Facilitator Skill

## Purpose

The HAZOP Facilitator Skill supports Hazard and Operability studies by guiding systematic deviation analysis, consequence evaluation, and safeguard identification.

## Capabilities

- Node identification and definition
- Guide word application
- Deviation generation
- Cause identification
- Consequence analysis
- Safeguard evaluation
- Recommendation development
- Risk ranking
- Action tracking

## Usage Guidelines

### When to Use
- Conducting HAZOP studies
- Reviewing process modifications
- Revalidating existing HAZOPs
- Training HAZOP teams

### Prerequisites
- P&IDs available and current
- Process description complete
- Design basis documented
- Team assembled

### Best Practices
- Follow structured methodology
- Ensure team expertise coverage
- Document thoroughly
- Track all recommendations

## Process Integration

This skill integrates with:
- HAZOP Study Facilitation
- Safety Instrumented System Design
- Process Hazard Analysis

## Configuration

```yaml
hazop-facilitator:
  guide-words:
    - no
    - more
    - less
    - reverse
    - other
    - part-of
  risk-matrix:
    consequence-levels: 5
    likelihood-levels: 5
```

## Output Artifacts

- HAZOP worksheets
- Recommendation register
- Risk rankings
- Action tracking logs
- Meeting minutes

``````

## 83 HYSYS动态流程模拟

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/hysys-dynamic-simulator/SKILL.md

``````markdown
---
name: hysys-dynamic-simulator
description: Aspen HYSYS integration skill for dynamic simulation, pressure-flow networks, and process dynamics
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Simulation
  skill-id: CE-SK-002
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:dynamic-programming]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# HYSYS Dynamic Simulator Skill

## Purpose

The HYSYS Dynamic Simulator Skill enables dynamic process simulation for transient analysis, control system design, and emergency scenario evaluation.

## Capabilities

- Dynamic process simulation
- Pressure-flow solver configuration
- Controller tuning with dynamics
- Compressible flow analysis
- Transient scenario analysis
- Emergency shutdown simulation
- Trip system verification
- Batch process modeling

## Usage Guidelines

### When to Use
- Analyzing transient behavior
- Designing control systems
- Evaluating emergency scenarios
- Validating trip systems

### Prerequisites
- Steady-state simulation complete
- Equipment volumes defined
- Control strategy established
- Scenario requirements identified

### Best Practices
- Start from converged steady-state
- Define appropriate time steps
- Validate against plant data
- Document scenario assumptions

## Process Integration

This skill integrates with:
- Process Simulation Model Development
- Control Strategy Development
- Process Startup Procedure Development

## Configuration

```yaml
hysys-dynamic-simulator:
  solver-modes:
    - implicit
    - explicit
  scenario-types:
    - startup
    - shutdown
    - emergency
    - load-change
```

## Output Artifacts

- Dynamic simulation files
- Trend plots
- Controller performance data
- Scenario analysis reports

``````

## 84 化工生命周期评价

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/lca-analyzer/SKILL.md

``````markdown
---
name: lca-analyzer
description: Life Cycle Assessment skill for environmental impact evaluation and sustainability analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Sustainability
  skill-id: CE-SK-023
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:data-analysis, skill-area:mathematical-reasoning]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# LCA Analyzer Skill

## Purpose

The LCA Analyzer Skill performs Life Cycle Assessment to evaluate environmental impacts across process life cycles and support sustainable process design decisions.

## Capabilities

- Goal and scope definition
- Life cycle inventory (LCI) development
- Impact assessment (LCIA)
- Carbon footprint calculation
- Water footprint analysis
- Energy analysis
- Sensitivity analysis
- Comparative assessments
- Hot spot identification

## Usage Guidelines

### When to Use
- Evaluating process sustainability
- Comparing design alternatives
- Calculating carbon footprints
- Identifying improvement opportunities

### Prerequisites
- Process data available
- System boundaries defined
- Impact categories selected
- Inventory databases accessible

### Best Practices
- Follow ISO 14040/14044
- Document assumptions clearly
- Perform sensitivity analysis
- Use peer review for public claims

## Process Integration

This skill integrates with:
- Process Sustainability Assessment
- Green Chemistry Metrics Evaluation
- Energy Efficiency Optimization

## Configuration

```yaml
lca-analyzer:
  standards:
    - ISO-14040
    - ISO-14044
  impact-methods:
    - CML
    - ReCiPe
    - TRACI
  databases:
    - ecoinvent
    - US-LCI
    - GaBi
```

## Output Artifacts

- LCA reports
- Impact assessment results
- Comparative analyses
- Hot spot analysis
- Improvement recommendations

``````

## 85 化工装置性能试验设计

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/performance-test-designer/SKILL.md

``````markdown
---
name: performance-test-designer
description: Performance test design skill for test planning, data collection, and acceptance criteria verification
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Commissioning
  skill-id: CE-SK-028
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:sensor-fusion, skill-area:data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:lab-technician]
---

# Performance Test Designer Skill

## Purpose

The Performance Test Designer Skill develops comprehensive performance test plans including test conditions, data collection requirements, and acceptance criteria for process verification.

## Capabilities

- Test plan development
- Test condition specification
- Data collection requirements
- Instrumentation requirements
- Acceptance criteria definition
- Test duration calculation
- Statistical analysis planning
- Guarantee verification
- Report template generation

## Usage Guidelines

### When to Use
- Designing performance tests
- Verifying process guarantees
- Commissioning new equipment
- Validating modifications

### Prerequisites
- Design specifications available
- Guarantee requirements defined
- Instruments calibrated
- Steady-state achievable

### Best Practices
- Define clear acceptance criteria
- Plan adequate test duration
- Ensure instrument accuracy
- Document all conditions

## Process Integration

This skill integrates with:
- Performance Testing and Validation
- Process Startup Procedure Development
- Scale-Up Analysis

## Configuration

```yaml
performance-test-designer:
  test-types:
    - capacity
    - efficiency
    - product-quality
    - emissions
  statistical-methods:
    - uncertainty-analysis
    - ASME-PTC
```

## Output Artifacts

- Test plans
- Data collection sheets
- Analysis procedures
- Report templates
- Acceptance certificates

``````

## 86 工艺流程图与管仪图编制

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/pfd-pid-generator/SKILL.md

``````markdown
---
name: pfd-pid-generator
description: Process flow diagram and P&ID generation skill with standards compliance and symbol libraries
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Design
  skill-id: CE-SK-029
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# PFD/P&ID Generator Skill

## Purpose

The PFD/P&ID Generator Skill creates process flow diagrams and piping and instrumentation diagrams following industry standards with appropriate symbology and documentation.

## Capabilities

- PFD development with heat/mass balance
- P&ID development per ISA standards
- Equipment numbering systems
- Instrument identification
- Line numbering and specifications
- Control loop representation
- Safety system documentation
- Revision management
- Drawing cross-references

## Usage Guidelines

### When to Use
- Developing new PFDs/P&IDs
- Updating existing drawings
- Standardizing documentation
- Supporting design reviews

### Prerequisites
- Process design basis defined
- Equipment list available
- Control philosophy developed
- Standards specified

### Best Practices
- Follow company standards
- Maintain consistency
- Include all required information
- Manage revisions properly

## Process Integration

This skill integrates with:
- Process Flow Diagram Development
- Control Strategy Development
- Equipment Sizing and Specification

## Configuration

```yaml
pfd-pid-generator:
  standards:
    - ISA-5.1
    - ISO-10628
    - PIP
  symbol-libraries:
    - equipment
    - instruments
    - valves
    - piping
```

## Output Artifacts

- Process flow diagrams
- Piping & instrumentation diagrams
- Equipment lists
- Instrument lists
- Line lists

``````

## 87 化工工艺经济估算

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/process-economics-estimator/SKILL.md

``````markdown
---
name: process-economics-estimator
description: Process economics estimation skill for capital costs, operating costs, and profitability analysis
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Design
  skill-id: CE-SK-032
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:mathematical-reasoning, skill-area:data-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Process Economics Estimator Skill

## Purpose

The Process Economics Estimator Skill performs economic analysis of chemical processes including capital cost estimation, operating cost calculation, and profitability metrics.

## Capabilities

- Capital cost estimation (factored, equipment-based)
- Operating cost calculation
- Raw material cost analysis
- Utility cost calculation
- Labor cost estimation
- Depreciation and taxes
- Profitability metrics (NPV, IRR, payback)
- Sensitivity analysis
- Monte Carlo simulation

## Usage Guidelines

### When to Use
- Evaluating project economics
- Comparing process alternatives
- Supporting investment decisions
- Analyzing sensitivity

### Prerequisites
- Equipment list available
- Capacity defined
- Utility requirements known
- Market prices available

### Best Practices
- Use appropriate estimation method
- Document all assumptions
- Include contingency
- Perform sensitivity analysis

## Process Integration

This skill integrates with:
- Equipment Sizing and Specification
- Process Flow Diagram Development
- Separation Sequence Synthesis

## Configuration

```yaml
process-economics-estimator:
  estimation-classes:
    - order-of-magnitude
    - study
    - preliminary
    - definitive
  profitability-metrics:
    - NPV
    - IRR
    - payback
    - ROI
```

## Output Artifacts

- Capital cost estimates
- Operating cost analyses
- Cash flow projections
- Profitability analyses
- Sensitivity charts

``````

## 88 化学反应器设计

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/reactor-designer/SKILL.md

``````markdown
---
name: reactor-designer
description: Chemical reactor design skill for sizing, configuration selection, and performance optimization
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Reaction Engineering
  skill-id: CE-SK-007
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:statistical-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Reactor Designer Skill

## Purpose

The Reactor Designer Skill performs chemical reactor design calculations, including reactor type selection, sizing, configuration optimization, and performance prediction.

## Capabilities

- Reactor type selection (CSTR, PFR, batch, fluidized bed)
- Reactor sizing calculations
- Conversion and yield predictions
- Residence time distribution analysis
- Heat management design
- Multiple reactor configurations
- Recycle stream optimization
- Scale-up considerations

## Usage Guidelines

### When to Use
- Designing new reactor systems
- Optimizing existing reactor performance
- Evaluating reactor alternatives
- Scale-up reactor designs

### Prerequisites
- Kinetic model available
- Feed specifications defined
- Target conversion specified
- Operating constraints identified

### Best Practices
- Consider heat effects carefully
- Evaluate multiple configurations
- Include safety margins
- Validate with pilot data

## Process Integration

This skill integrates with:
- Kinetic Model Development
- Catalyst Evaluation and Optimization
- Process Simulation Model Development

## Configuration

```yaml
reactor-designer:
  reactor-types:
    - cstr
    - pfr
    - batch
    - semi-batch
    - fluidized-bed
  design-methods:
    - sizing
    - optimization
    - performance-prediction
```

## Output Artifacts

- Reactor specifications
- Sizing calculations
- Performance predictions
- Configuration comparisons
- Heat duty calculations

``````

## 89 化工工艺放大分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/scale-up-analyzer/SKILL.md

``````markdown
---
name: scale-up-analyzer
description: Process scale-up analysis skill for dimensional analysis, similarity criteria, and pilot-to-production transitions
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Development
  skill-id: CE-SK-009
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:physics-simulation, skill-area:mathematical-reasoning, skill-area:statistical-analysis]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:computational-scientist]
---

# Scale-Up Analyzer Skill

## Purpose

The Scale-Up Analyzer Skill supports process scale-up from laboratory to pilot to production scale using dimensional analysis, similarity criteria, and scale-up correlations.

## Capabilities

- Dimensional analysis
- Similarity criteria evaluation
- Scale-up factor calculation
- Heat transfer scale-up
- Mass transfer scale-up
- Mixing scale-up (power per volume, tip speed)
- Reaction scale-up considerations
- Risk assessment for scale-up

## Usage Guidelines

### When to Use
- Scaling from lab to pilot
- Scaling from pilot to production
- Evaluating scale-up feasibility
- Identifying scale-sensitive parameters

### Prerequisites
- Lab/pilot data available
- Process fundamentals understood
- Critical parameters identified
- Target scale defined

### Best Practices
- Identify controlling mechanisms
- Maintain appropriate similarity criteria
- Plan incremental scale-up steps
- Validate at each scale

## Process Integration

This skill integrates with:
- Scale-Up Analysis
- Process Simulation Model Development
- Performance Testing and Validation

## Configuration

```yaml
scale-up-analyzer:
  scale-up-methods:
    - geometric-similarity
    - dynamic-similarity
    - thermal-similarity
  scale-factors:
    - 10x
    - 100x
    - 1000x
```

## Output Artifacts

- Scale-up calculations
- Similarity analysis
- Risk assessments
- Scale-up recommendations
- Parameter predictions

``````

## 90 化工安全完整性等级分析

来源：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/chemical-engineering/skills/sil-calculator/SKILL.md

``````markdown
---
name: sil-calculator
description: Safety Integrity Level calculation skill for SIF design and verification per IEC 61511
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Edit
  - Bash
metadata:
  specialization: chemical-engineering
  domain: science
  category: Process Safety
  skill-id: CE-SK-015
graph:
  domains: [domain:chemical-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:mathematical-reasoning, skill-area:compliance-automation]
  workflows: [workflow:experiment-design]
  roles: [role:research-engineer, role:systems-integration-engineer]
---

# SIL Calculator Skill

## Purpose

The SIL Calculator Skill determines Safety Integrity Levels for Safety Instrumented Functions and verifies SIF designs meet required risk reduction per IEC 61511.

## Capabilities

- SIL determination (risk graph, LOPA, risk matrix)
- PFDavg calculations
- Proof test interval optimization
- Common cause failure analysis
- Hardware fault tolerance verification
- Diagnostic coverage assessment
- Systematic capability evaluation
- SIF verification calculations

## Usage Guidelines

### When to Use
- Determining SIL requirements
- Designing safety instrumented functions
- Verifying SIF performance
- Optimizing proof test intervals

### Prerequisites
- HAZOP recommendations available
- Risk criteria defined
- Component failure data available
- Architecture selected

### Best Practices
- Use consistent methodology
- Document all assumptions
- Consider common cause failures
- Verify systematic capability

## Process Integration

This skill integrates with:
- Safety Instrumented System Design
- HAZOP Study Facilitation
- Pressure Relief System Design

## Configuration

```yaml
sil-calculator:
  determination-methods:
    - risk-graph
    - lopa
    - risk-matrix
  failure-databases:
    - OREDA
    - SINTEF
    - exida
```

## Output Artifacts

- SIL determination reports
- PFDavg calculations
- SIF specifications
- Verification reports
- Test interval recommendations

``````
