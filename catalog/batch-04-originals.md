# 第四批完整原始说明

以下保留已采集的原作者SKILL.md全文，版本链接随条目列出。本批仅整理清单，并未创建或修改原技能。

## 91 · 车辆网络安全工程辅助

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/automotive-engineering/skills/automotive-cybersecurity

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/automotive-engineering/skills/automotive-cybersecurity/SKILL.md

``````markdown
---
name: automotive-cybersecurity
description: Vehicle cybersecurity engineering per ISO/SAE 21434
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
  category: automotive-engineering
  tags:
    - security
    - cybersecurity
    - iso-21434
    - threat-analysis
graph:
  domains: [domain:automotive-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:motion-planning, skill-area:physics-simulation]
  roles: [role:systems-integration-engineer, role:embedded-engineer]
---

# Automotive Cybersecurity Skill

## Purpose
Provide vehicle cybersecurity engineering capabilities per ISO/SAE 21434 including threat analysis, security control design, and incident response.

## Capabilities
- Threat Analysis and Risk Assessment (TARA)
- Attack tree generation
- Security control selection
- Secure communication design (SecOC, TLS)
- Key management system design
- Penetration testing guidance
- Intrusion detection system design
- Incident response planning

## Usage Guidelines
- Conduct TARA during concept phase
- Generate attack trees for critical assets
- Select security controls based on risk level
- Implement secure communication protocols
- Design key management for lifecycle security
- Plan incident response procedures

## Dependencies
- Cybersecurity analysis tools
- AUTOSAR SecOC
- HSM integration

## Process Integration
- SAF-004: Cybersecurity Engineering (ISO/SAE 21434)
- ASD-004: Over-the-Air (OTA) Update Implementation
- ASD-001: AUTOSAR Architecture Implementation

``````

## 92 · AUTOSAR软件平台配置

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/automotive-engineering/skills/autosar-config

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/automotive-engineering/skills/autosar-config/SKILL.md

``````markdown
---
name: autosar-config
description: AUTOSAR Classic and Adaptive Platform configuration and implementation expertise
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
  category: automotive-engineering
  tags:
    - automotive-software
    - autosar
    - ecu
    - embedded
graph:
  domains: [domain:automotive-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:motion-planning, skill-area:physics-simulation]
  roles: [role:systems-integration-engineer, role:embedded-engineer]
---

# AUTOSAR Configuration Skill

## Purpose
Provide AUTOSAR Classic and Adaptive Platform configuration and implementation expertise for automotive ECU software development.

## Capabilities
- Software component (SWC) design and modeling
- RTE configuration and code generation
- Basic Software (BSW) module configuration
- AUTOSAR COM stack setup
- Memory stack configuration (NvM, Fee, Ea)
- Diagnostic stack configuration (Dcm, Dem)
- AUTOSAR Adaptive Platform services
- ARXML file generation and validation

## Usage Guidelines
- Design SWC interfaces following AUTOSAR methodology
- Configure RTE for proper scheduling and communication
- Set up BSW modules according to ECU requirements
- Implement diagnostic services per UDS standards
- Validate ARXML against AUTOSAR schema
- Document configuration decisions and rationale

## Dependencies
- Vector DaVinci
- ETAS ISOLAR
- EB tresos
- Artop

## Process Integration
- ASD-001: AUTOSAR Architecture Implementation
- ASD-002: ECU Software Development and Testing
- ASD-003: Diagnostic Implementation (UDS/OBD)

``````

## 93 · 动力电池与BMS开发辅助

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/automotive-engineering/skills/bms-development

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/automotive-engineering/skills/bms-development/SKILL.md

``````markdown
---
name: bms-development
description: Battery system design, BMS algorithm development, and validation expertise
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
  category: automotive-engineering
  tags:
    - electrification
    - battery
    - bms
    - ev
graph:
  domains: [domain:automotive-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:motion-planning, skill-area:physics-simulation]
  roles: [role:systems-integration-engineer, role:embedded-engineer]
---

# Battery Management System Skill

## Purpose
Provide comprehensive battery system design and BMS algorithm development capabilities for electric vehicle applications including state estimation and thermal management.

## Capabilities
- Cell characterization data analysis (HPPC, capacity, OCV)
- State-of-Charge (SoC) estimation algorithms
- State-of-Health (SoH) estimation methods
- Cell balancing strategy implementation
- Thermal management system sizing
- Battery pack electrical design
- Fault detection and diagnostics
- Abuse testing scenario definition

## Usage Guidelines
- Characterize cells across full temperature and SOC range
- Validate SoC algorithms against reference methods
- Design thermal management for worst-case conditions
- Implement robust fault detection for safety
- Consider cell aging in lifetime predictions
- Document battery specifications and safety limits

## Dependencies
- GT-SUITE
- AVL CRUISE M
- MATLAB/Simulink
- Battery testing equipment

## Process Integration
- PTE-001: Battery System Design and Validation
- PTE-004: Powertrain Calibration and Optimization
- SAF-001: Functional Safety Development (ISO 26262)

``````

## 94 · 电机与驱动单元设计

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/automotive-engineering/skills/electric-motor-design

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/automotive-engineering/skills/electric-motor-design/SKILL.md

``````markdown
---
name: electric-motor-design
description: Electric motor and drive unit design and optimization expertise
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
  category: automotive-engineering
  tags:
    - electrification
    - motor
    - inverter
    - drive-unit
graph:
  domains: [domain:automotive-engineering]
  skillAreas: [skill-area:sensor-fusion, skill-area:motion-planning, skill-area:physics-simulation]
  roles: [role:systems-integration-engineer, role:embedded-engineer]
---

# Electric Motor Design Skill

## Purpose
Enable electric motor and drive unit design and optimization including electromagnetic analysis, thermal modeling, and control algorithm development.

## Capabilities
- Motor topology selection (PMSM, induction, SRM)
- Electromagnetic FEA simulation (JMAG, Motor-CAD, ANSYS Maxwell)
- Efficiency map generation and analysis
- Thermal modeling and cooling design
- NVH analysis for electric motors
- Demagnetization analysis
- Inverter sizing and selection
- Field-oriented control (FOC) algorithm development

## Usage Guidelines
- Select motor topology based on performance and cost requirements
- Optimize efficiency across typical drive cycles
- Design cooling for continuous and peak power requirements
- Analyze NVH characteristics for acceptable noise levels
- Validate demagnetization resistance at extreme temperatures
- Document motor specifications and control parameters

## Dependencies
- JMAG
- Motor-CAD
- ANSYS Maxwell
- MATLAB/Simulink

## Process Integration
- PTE-002: Electric Drive Unit Development
- PTE-003: Hybrid Powertrain Integration
- PTE-004: Powertrain Calibration and Optimization

``````

## 95 · 机器人行为树设计

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/robotics-simulation/skills/behavior-trees

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/robotics-simulation/skills/behavior-trees/SKILL.md

``````markdown
---
name: Behavior Trees Skill
description: Behavior tree design and implementation for robot decision making
slug: behavior-trees
category: Decision Making
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
graph:
  domains: [domain:robotics]
  specializations: [specialization:robotics-simulation]
  skillAreas: [skill-area:motion-planning, skill-area:sensor-fusion]
  roles: [role:research-engineer]
---

# Behavior Trees Skill

## Overview

Expert skill for designing and implementing behavior trees for robot decision making, task sequencing, and reactive behaviors.

## Capabilities

- Design behavior trees for complex robot behaviors
- Configure BehaviorTree.CPP nodes and trees
- Implement custom action, condition, and decorator nodes
- Set up blackboard for state sharing
- Configure subtrees and tree switching
- Implement reactive behaviors and fallbacks
- Debug behavior tree execution with Groot
- Set up behavior tree logging and analysis
- Configure timeout and recovery behaviors
- Implement parallel and sequence nodes

## Target Processes

- nav2-navigation-setup.js
- autonomous-exploration.js
- multi-robot-coordination.js
- hri-interface.js

## Dependencies

- BehaviorTree.CPP
- Groot
- nav2_behavior_tree

## Usage Context

This skill is invoked when processes require complex decision-making logic, task sequencing, or reactive robot behaviors.

## Output Artifacts

- Behavior tree XML definitions
- Custom BT node implementations
- Blackboard configurations
- Groot visualization setups
- Recovery behavior designs
- BT logging configurations

``````

## 96 · 机器人边缘模型部署

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/robotics-simulation/skills/edge-deployment

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/robotics-simulation/skills/edge-deployment/SKILL.md

``````markdown
---
name: Edge Deployment Skill
description: ML model optimization and deployment on robot edge devices (Jetson, embedded)
slug: edge-deployment
category: Deployment
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
graph:
  domains: [domain:robotics]
  specializations: [specialization:robotics-simulation]
  skillAreas: [skill-area:motion-planning, skill-area:sensor-fusion]
  roles: [role:research-engineer]
---

# Edge Deployment Skill

## Overview

Expert skill for optimizing and deploying machine learning models on robot edge devices including NVIDIA Jetson and embedded systems.

## Capabilities

- Configure TensorRT optimization for NVIDIA Jetson
- Set up ONNX model conversion and optimization
- Implement INT8 and FP16 quantization
- Configure DeepStream for video analytics
- Set up CUDA graph optimization
- Implement model pruning and distillation
- Configure DLA (Deep Learning Accelerator) deployment
- Set up multi-stream inference
- Implement ROS2 inference nodes
- Profile and benchmark on target hardware

## Target Processes

- nn-model-optimization.js
- object-detection-pipeline.js
- rl-robot-control.js
- field-testing-validation.js

## Dependencies

- TensorRT
- ONNX Runtime
- NVIDIA Jetson SDK
- DeepStream

## Usage Context

This skill is invoked when processes require deploying ML models on edge devices with optimized inference performance.

## Output Artifacts

- TensorRT engine files
- ONNX optimized models
- Quantization configurations
- DeepStream pipeline configs
- Inference benchmark reports
- ROS2 inference node implementations

``````

## 97 · 多机器人任务协同

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/robotics-simulation/skills/multi-robot-coordination

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/robotics-simulation/skills/multi-robot-coordination/SKILL.md

``````markdown
---
name: Multi-Robot Coordination Skill
description: Coordination and task allocation for multi-robot systems and fleets
slug: multi-robot-coordination
category: Fleet Management
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
graph:
  domains: [domain:robotics]
  specializations: [specialization:robotics-simulation]
  skillAreas: [skill-area:motion-planning, skill-area:sensor-fusion]
  roles: [role:research-engineer]
---

# Multi-Robot Coordination Skill

## Overview

Expert skill for coordinating multi-robot systems including task allocation, path planning, and collision avoidance for robot fleets.

## Capabilities

- Implement auction-based task allocation
- Configure market-based coordination
- Set up conflict-based search (CBS) for path planning
- Implement ORCA/RVO collision avoidance
- Configure formation control algorithms
- Set up distributed consensus protocols
- Implement priority-based planning
- Configure multi-master ROS communication
- Set up fleet management APIs
- Implement traffic management zones

## Target Processes

- multi-robot-coordination.js
- fleet-management-system.js
- path-planning-algorithm.js
- dynamic-obstacle-avoidance.js

## Dependencies

- multimaster_fkie
- free_fleet
- Open-RMF

## Usage Context

This skill is invoked when processes require multi-robot coordination, fleet management, or multi-agent path planning.

## Output Artifacts

- Task allocation algorithms
- Multi-robot path planners
- Collision avoidance configurations
- Formation control implementations
- Fleet management APIs
- Traffic zone configurations

``````

## 98 · ROS2硬件接口与控制器管理

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/robotics-simulation/skills/ros2-control

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/robotics-simulation/skills/ros2-control/SKILL.md

``````markdown
---
name: ros2_control Skill
description: Hardware abstraction and controller management using ros2_control framework
slug: ros2-control
category: Control
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
graph:
  domains: [domain:robotics]
  specializations: [specialization:robotics-simulation]
  skillAreas: [skill-area:motion-planning, skill-area:sensor-fusion]
  roles: [role:research-engineer]
---

# ros2_control Skill

## Overview

Expert skill for configuring the ros2_control framework for hardware abstraction, controller management, and real-time robot control.

## Capabilities

- Configure hardware interfaces (GPIO, system, actuator, sensor)
- Set up controller manager and controller lifecycle
- Implement position, velocity, and effort controllers
- Configure joint trajectory controller
- Set up diff_drive and ackermann controllers
- Implement custom hardware interfaces
- Configure transmission interfaces
- Set up joint limits and saturation
- Implement combined robot controllers
- Debug controller loading and activation

## Target Processes

- robot-system-design.js
- mpc-controller-design.js
- moveit-manipulation-planning.js
- robot-bring-up.js

## Dependencies

- ros2_control
- ros2_controllers
- hardware_interface

## Usage Context

This skill is invoked when processes require hardware abstraction layer setup, controller configuration, or real-time control system integration.

## Output Artifacts

- Hardware interface configurations
- Controller YAML parameters
- URDF ros2_control tags
- Custom hardware interface code
- Controller launch files
- Transmission configurations

``````

## 99 · 仿真输入概率分布拟合

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/industrial-engineering/skills/distribution-fitter

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/distribution-fitter/SKILL.md

``````markdown
---
name: distribution-fitter
description: Statistical distribution fitting skill for input modeling in simulation and analysis.
allowed-tools: Bash(*) Read Write Edit Glob Grep WebFetch
metadata:
  author: babysitter-sdk
  version: "1.0.0"
  category: simulation
  backlog-id: SK-IE-006
graph:
  domains: [domain:industrial-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:organizational-design, skill-area:data-analysis]
  roles: [role:operations-analyst, role:research-engineer]
---

# distribution-fitter

You are **distribution-fitter** - a specialized skill for fitting statistical distributions to data for input modeling in simulation and analysis.

## Overview

This skill enables AI-powered distribution fitting including:
- Goodness-of-fit testing (Chi-square, K-S, Anderson-Darling)
- Maximum likelihood estimation
- Distribution parameter estimation
- Inter-arrival time analysis
- Service time distribution fitting
- Empirical distribution construction
- Distribution comparison and selection

## Prerequisites

- Python 3.8+ with scipy, fitter installed
- Statistical analysis libraries
- Understanding of probability distributions

## Capabilities

### 1. Automated Distribution Fitting

```python
from fitter import Fitter
import numpy as np

def fit_distribution(data, distributions=None):
    """
    Fit multiple distributions and select best fit
    """
    if distributions is None:
        distributions = ['norm', 'expon', 'gamma', 'lognorm',
                        'weibull_min', 'beta', 'uniform', 'triang']

    f = Fitter(data, distributions=distributions)
    f.fit()

    # Get summary
    summary = f.summary()

    # Best distribution
    best = f.get_best(method='sumsquare_error')

    return {
        "best_distribution": list(best.keys())[0],
        "parameters": best,
        "summary": summary.to_dict(),
        "all_fits": f.fitted_param
    }
```

### 2. Goodness-of-Fit Testing

```python
from scipy import stats
import numpy as np

def goodness_of_fit_tests(data, distribution, params):
    """
    Perform multiple goodness-of-fit tests
    """
    results = {}

    # Kolmogorov-Smirnov test
    ks_stat, ks_pvalue = stats.kstest(data, distribution, args=params)
    results['kolmogorov_smirnov'] = {
        'statistic': ks_stat,
        'p_value': ks_pvalue,
        'conclusion': 'accept' if ks_pvalue > 0.05 else 'reject'
    }

    # Chi-square test
    observed, bins = np.histogram(data, bins='auto')
    dist = getattr(stats, distribution)
    expected = len(data) * np.diff(dist.cdf(bins, *params))

    # Combine bins with low expected counts
    mask = expected >= 5
    chi2_stat, chi2_pvalue = stats.chisquare(
        observed[mask], expected[mask]
    )
    results['chi_square'] = {
        'statistic': chi2_stat,
        'p_value': chi2_pvalue,
        'degrees_of_freedom': sum(mask) - len(params) - 1
    }

    # Anderson-Darling test (for specific distributions)
    if distribution in ['norm', 'expon', 'gumbel', 'logistic']:
        ad_result = stats.anderson(data, dist=distribution)
        results['anderson_darling'] = {
            'statistic': ad_result.statistic,
            'critical_values': dict(zip(
                ['15%', '10%', '5%', '2.5%', '1%'],
                ad_result.critical_values
            ))
        }

    return results
```

### 3. Maximum Likelihood Estimation

```python
from scipy.optimize import minimize
from scipy import stats

def mle_fit(data, distribution):
    """
    Fit distribution using maximum likelihood
    """
    dist = getattr(stats, distribution)

    # Get parameter bounds
    bounds = get_parameter_bounds(distribution)

    # Negative log-likelihood function
    def neg_log_likelihood(params):
        return -np.sum(dist.logpdf(data, *params))

    # Initial guess
    x0 = get_initial_params(data, distribution)

    # Optimize
    result = minimize(neg_log_likelihood, x0, bounds=bounds,
                     method='L-BFGS-B')

    # Standard errors via Hessian
    from scipy.optimize import approx_fprime
    hessian = np.zeros((len(result.x), len(result.x)))
    epsilon = 1e-5
    for i in range(len(result.x)):
        hessian[i] = approx_fprime(result.x,
            lambda p: approx_fprime(p, neg_log_likelihood, epsilon)[i],
            epsilon)

    se = np.sqrt(np.diag(np.linalg.inv(hessian)))

    return {
        "distribution": distribution,
        "parameters": result.x.tolist(),
        "standard_errors": se.tolist(),
        "log_likelihood": -result.fun,
        "aic": 2 * len(result.x) + 2 * result.fun,
        "bic": len(result.x) * np.log(len(data)) + 2 * result.fun
    }
```

### 4. Inter-arrival Time Analysis

```python
def analyze_interarrival_times(timestamps):
    """
    Analyze inter-arrival times from timestamp data
    """
    # Calculate inter-arrival times
    timestamps = np.array(timestamps)
    interarrivals = np.diff(timestamps)

    # Basic statistics
    stats_summary = {
        "count": len(interarrivals),
        "mean": np.mean(interarrivals),
        "std": np.std(interarrivals),
        "cv": np.std(interarrivals) / np.mean(interarrivals),
        "min": np.min(interarrivals),
        "max": np.max(interarrivals),
        "median": np.median(interarrivals)
    }

    # Fit exponential (Poisson process test)
    exp_params = stats.expon.fit(interarrivals, floc=0)
    ks_stat, ks_pvalue = stats.kstest(interarrivals, 'expon', args=exp_params)

    is_poisson = ks_pvalue > 0.05 and 0.8 < stats_summary['cv'] < 1.2

    # Fit other distributions
    fit_result = fit_distribution(interarrivals)

    return {
        "statistics": stats_summary,
        "poisson_process_test": {
            "ks_statistic": ks_stat,
            "p_value": ks_pvalue,
            "cv_test": stats_summary['cv'],
            "is_poisson": is_poisson
        },
        "best_fit": fit_result,
        "arrival_rate": 1 / stats_summary['mean']
    }
```

### 5. Empirical Distribution

```python
class EmpiricalDistribution:
    """
    Create empirical distribution from data
    """
    def __init__(self, data):
        self.data = np.sort(data)
        self.n = len(data)
        self.ecdf = np.arange(1, self.n + 1) / self.n

    def cdf(self, x):
        """Cumulative distribution function"""
        return np.searchsorted(self.data, x, side='right') / self.n

    def ppf(self, q):
        """Percent point function (inverse CDF)"""
        idx = int(q * self.n)
        return self.data[min(idx, self.n - 1)]

    def sample(self, size=1):
        """Generate random samples"""
        u = np.random.uniform(0, 1, size)
        return np.array([self.ppf(ui) for ui in u])

    def to_dict(self):
        """Export for storage"""
        return {
            "type": "empirical",
            "values": self.data.tolist(),
            "probabilities": self.ecdf.tolist()
        }
```

### 6. Distribution Comparison

```python
def compare_distributions(data, candidates):
    """
    Compare multiple distribution fits
    """
    results = []

    for dist_name in candidates:
        try:
            dist = getattr(stats, dist_name)
            params = dist.fit(data)

            # Log-likelihood
            ll = np.sum(dist.logpdf(data, *params))

            # Information criteria
            k = len(params)
            n = len(data)
            aic = 2 * k - 2 * ll
            bic = k * np.log(n) - 2 * ll

            # KS test
            ks_stat, ks_pvalue = stats.kstest(data, dist_name, args=params)

            results.append({
                "distribution": dist_name,
                "parameters": params,
                "log_likelihood": ll,
                "aic": aic,
                "bic": bic,
                "ks_statistic": ks_stat,
                "ks_pvalue": ks_pvalue
            })
        except Exception as e:
            continue

    # Sort by AIC
    results.sort(key=lambda x: x['aic'])

    return {
        "rankings": results,
        "best_by_aic": results[0]['distribution'],
        "best_by_bic": min(results, key=lambda x: x['bic'])['distribution']
    }
```

## Process Integration

This skill integrates with the following processes:
- `discrete-event-simulation-modeling.js`
- `queuing-system-analysis.js`
- `demand-forecasting-model-development.js`

## Output Format

```json
{
  "data_summary": {
    "n": 500,
    "mean": 5.2,
    "std": 2.1,
    "cv": 0.40
  },
  "best_fit": {
    "distribution": "gamma",
    "parameters": {"shape": 6.1, "scale": 0.85},
    "goodness_of_fit": {
      "ks_statistic": 0.032,
      "ks_pvalue": 0.67,
      "aic": 1523.4
    }
  },
  "alternative_fits": [
    {"distribution": "lognorm", "aic": 1528.1},
    {"distribution": "weibull", "aic": 1531.2}
  ],
  "recommendation": "Use gamma(6.1, 0.85) for simulation input"
}
```

## Tools/Libraries

| Library | Description | Use Case |
|---------|-------------|----------|
| scipy.stats | Statistical functions | Core fitting |
| fitter | Auto fitting | Quick analysis |
| statsmodels | Advanced stats | Detailed tests |
| R fitdistrplus | R package | Complex fitting |

## Best Practices

1. **Visualize first** - Always plot histograms and Q-Q plots
2. **Consider theory** - Choose distributions based on process
3. **Test multiple** - Compare several candidate distributions
4. **Check tails** - Extreme values matter for simulation
5. **Document choice** - Record rationale for selected distribution
6. **Update periodically** - Re-fit as new data becomes available

## Constraints

- Report goodness-of-fit statistics, not just parameters
- Document data collection methodology
- Consider censored or truncated data
- Test for time-varying parameters

``````

## 100 · 工业试验设计与分析

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/industrial-engineering/skills/doe-designer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/doe-designer/SKILL.md

``````markdown
---
name: doe-designer
description: Design of Experiments planning and analysis skill for factorial and response surface experiments.
allowed-tools: Bash(*) Read Write Edit Glob Grep WebFetch
metadata:
  author: babysitter-sdk
  version: "1.0.0"
  category: quality-engineering
  backlog-id: SK-IE-017
graph:
  domains: [domain:industrial-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:organizational-design, skill-area:data-analysis]
  roles: [role:operations-analyst, role:research-engineer]
---

# doe-designer

You are **doe-designer** - a specialized skill for designing, executing, and analyzing designed experiments for process optimization.

## Overview

This skill enables AI-powered DOE including:
- Full factorial design generation
- Fractional factorial design with confounding analysis
- Response surface methodology (CCD, Box-Behnken)
- Screening design (Plackett-Burman, definitive screening)
- ANOVA analysis of experimental results
- Main effects and interaction plots
- Contour plots and surface plots
- Optimal factor level determination
- Confirmation run planning

## Capabilities

### 1. Full Factorial Design

```python
import pyDOE2 as doe
import numpy as np
import pandas as pd

def full_factorial_design(factors, levels=2):
    """
    Generate full factorial design

    factors: dict of {name: (low, high)} for 2-level
             or {name: [level1, level2, ...]} for multi-level
    """
    factor_names = list(factors.keys())
    n_factors = len(factors)

    if levels == 2:
        # 2^k design
        design_coded = doe.ff2n(n_factors)
        n_runs = 2 ** n_factors

        # Convert to actual values
        design_actual = np.zeros_like(design_coded)
        for i, (name, bounds) in enumerate(factors.items()):
            low, high = bounds
            design_actual[:, i] = np.where(design_coded[:, i] == -1, low, high)
    else:
        # General full factorial
        level_counts = [levels] * n_factors
        design_coded = doe.fullfact(level_counts)
        n_runs = levels ** n_factors

        design_actual = np.zeros_like(design_coded)
        for i, (name, levels_list) in enumerate(factors.items()):
            for j, level in enumerate(levels_list):
                design_actual[design_coded[:, i] == j, i] = level

    df = pd.DataFrame(design_actual, columns=factor_names)
    df['Run'] = range(1, n_runs + 1)
    df['StdOrder'] = df['Run']

    # Randomize
    df['RunOrder'] = np.random.permutation(n_runs) + 1
    df = df.sort_values('RunOrder').reset_index(drop=True)

    return {
        "design_matrix": df,
        "coded_matrix": design_coded,
        "num_runs": n_runs,
        "num_factors": n_factors,
        "design_type": f"{levels}^{n_factors} Full Factorial",
        "resolution": "Full"
    }
```

### 2. Fractional Factorial Design

```python
def fractional_factorial_design(factors, resolution='IV'):
    """
    Generate fractional factorial design

    resolution: 'III', 'IV', or 'V'
    """
    n_factors = len(factors)
    factor_names = list(factors.keys())

    # Common fractional factorial generators
    generators = {
        3: {'III': 'a b ab'},  # 2^(3-1)
        4: {'IV': 'a b c abc'},  # 2^(4-1)
        5: {'V': 'a b c d abcd', 'III': 'a b ab c ac'},  # 2^(5-1) or 2^(5-2)
        6: {'IV': 'a b c d ab cd', 'III': 'a b ab c ac bc'},
        7: {'IV': 'a b c d ab ac bc', 'III': 'a b ab c ac d ad'}
    }

    if n_factors in generators and resolution in generators[n_factors]:
        gen = generators[n_factors][resolution]
        design_coded = doe.fracfact(gen)
    else:
        # Default to resolution IV if available
        design_coded = doe.fracfact(' '.join(['abcdefghij'[:n_factors]]))

    n_runs = len(design_coded)

    # Convert to actual values
    design_actual = np.zeros_like(design_coded)
    for i, (name, bounds) in enumerate(factors.items()):
        low, high = bounds
        design_actual[:, i] = np.where(design_coded[:, i] == -1, low, high)

    df = pd.DataFrame(design_actual, columns=factor_names)

    # Analyze confounding
    confounding = analyze_confounding(n_factors, resolution)

    return {
        "design_matrix": df,
        "num_runs": n_runs,
        "resolution": resolution,
        "confounding_pattern": confounding,
        "design_type": f"2^({n_factors}-p) Resolution {resolution}"
    }

def analyze_confounding(n_factors, resolution):
    """Describe confounding pattern by resolution"""
    patterns = {
        'III': "Main effects confounded with 2-factor interactions",
        'IV': "Main effects clear; 2FIs confounded with each other",
        'V': "Main effects and 2FIs clear; 3FIs confounded"
    }
    return patterns.get(resolution, "Unknown confounding pattern")
```

### 3. Response Surface Designs

```python
def central_composite_design(factors, alpha='rotatable', center_points=5):
    """
    Generate Central Composite Design (CCD)

    alpha: 'rotatable', 'orthogonal', or numeric value
    """
    n_factors = len(factors)
    factor_names = list(factors.keys())

    # Generate CCD
    design_coded = doe.ccdesign(n_factors, center=(0, center_points), alpha=alpha)

    n_runs = len(design_coded)

    # Convert to actual values
    design_actual = np.zeros_like(design_coded)
    for i, (name, bounds) in enumerate(factors.items()):
        low, high = bounds
        center = (low + high) / 2
        half_range = (high - low) / 2
        design_actual[:, i] = center + design_coded[:, i] * half_range

    df = pd.DataFrame(design_actual, columns=factor_names)

    return {
        "design_matrix": df,
        "coded_matrix": design_coded,
        "num_runs": n_runs,
        "design_type": "Central Composite Design",
        "alpha": alpha,
        "center_points": center_points
    }

def box_behnken_design(factors, center_points=3):
    """
    Generate Box-Behnken Design

    Good for 3-4 factors, avoids extreme corners
    """
    n_factors = len(factors)
    factor_names = list(factors.keys())

    design_coded = doe.bbdesign(n_factors, center=center_points)
    n_runs = len(design_coded)

    # Convert to actual values
    design_actual = np.zeros_like(design_coded)
    for i, (name, bounds) in enumerate(factors.items()):
        low, high = bounds
        center = (low + high) / 2
        half_range = (high - low) / 2
        design_actual[:, i] = center + design_coded[:, i] * half_range

    df = pd.DataFrame(design_actual, columns=factor_names)

    return {
        "design_matrix": df,
        "num_runs": n_runs,
        "design_type": "Box-Behnken Design",
        "center_points": center_points,
        "advantage": "No corner points - avoids extreme conditions"
    }
```

### 4. ANOVA Analysis

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

def analyze_factorial_experiment(data, response_col, factor_cols):
    """
    Perform ANOVA on factorial experiment
    """
    # Build formula with main effects and interactions
    main_effects = ' + '.join(factor_cols)
    interactions = ' + '.join([f'{a}:{b}' for i, a in enumerate(factor_cols)
                               for b in factor_cols[i+1:]])
    formula = f'{response_col} ~ {main_effects} + {interactions}'

    model = ols(formula, data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    # Effect estimates
    effects = {}
    for factor in factor_cols:
        high_mean = data[data[factor] == data[factor].max()][response_col].mean()
        low_mean = data[data[factor] == data[factor].min()][response_col].mean()
        effects[factor] = high_mean - low_mean

    return {
        "anova_table": anova_table.to_dict(),
        "r_squared": model.rsquared,
        "adj_r_squared": model.rsquared_adj,
        "effects": effects,
        "significant_factors": [f for f in factor_cols
                                if anova_table.loc[f, 'PR(>F)'] < 0.05],
        "model_summary": model.summary().as_text()
    }
```

### 5. Response Surface Analysis

```python
def fit_response_surface(data, response_col, factor_cols):
    """
    Fit second-order response surface model
    """
    # Build quadratic formula
    linear = ' + '.join(factor_cols)
    quadratic = ' + '.join([f'I({f}**2)' for f in factor_cols])
    interactions = ' + '.join([f'{a}:{b}' for i, a in enumerate(factor_cols)
                               for b in factor_cols[i+1:]])

    formula = f'{response_col} ~ {linear} + {quadratic} + {interactions}'

    model = ols(formula, data=data).fit()

    # Find stationary point
    # Extract coefficients for optimization
    coeffs = model.params

    return {
        "model": model,
        "r_squared": model.rsquared,
        "coefficients": coeffs.to_dict(),
        "significant_terms": [t for t in model.pvalues.index
                             if model.pvalues[t] < 0.05],
        "formula": formula
    }

def find_optimal_conditions(model, factor_cols, bounds, maximize=True):
    """
    Find optimal factor settings using response surface
    """
    from scipy.optimize import minimize

    def predict(x):
        data = pd.DataFrame([dict(zip(factor_cols, x))])
        pred = model.predict(data)[0]
        return -pred if maximize else pred

    # Multiple starts for global optimization
    best_result = None
    for _ in range(20):
        x0 = [np.random.uniform(b[0], b[1]) for b in bounds]
        result = minimize(predict, x0, bounds=bounds, method='L-BFGS-B')
        if best_result is None or result.fun < best_result.fun:
            best_result = result

    optimal = dict(zip(factor_cols, best_result.x))
    optimal_response = -best_result.fun if maximize else best_result.fun

    return {
        "optimal_settings": optimal,
        "predicted_response": optimal_response,
        "optimization_success": best_result.success
    }
```

### 6. Confirmation Run Planning

```python
def plan_confirmation_runs(optimal_settings, model, n_runs=5, alpha=0.05):
    """
    Plan confirmation runs at optimal settings
    """
    from scipy import stats

    # Predict at optimal
    data = pd.DataFrame([optimal_settings])
    predicted = model.predict(data)[0]

    # Prediction interval
    pred_se = np.sqrt(model.mse_resid)  # Simplified
    t_val = stats.t.ppf(1 - alpha/2, model.df_resid)

    pi_lower = predicted - t_val * pred_se * np.sqrt(1 + 1/len(model.model.data.orig_endog))
    pi_upper = predicted + t_val * pred_se * np.sqrt(1 + 1/len(model.model.data.orig_endog))

    return {
        "optimal_settings": optimal_settings,
        "predicted_response": predicted,
        "prediction_interval": {
            "lower": pi_lower,
            "upper": pi_upper,
            "confidence": 1 - alpha
        },
        "confirmation_runs": n_runs,
        "acceptance_criterion": f"Mean of {n_runs} runs should fall within [{pi_lower:.3f}, {pi_upper:.3f}]"
    }
```

## Process Integration

This skill integrates with the following processes:
- `design-of-experiments-execution.js`
- `root-cause-analysis-investigation.js`
- `statistical-process-control-implementation.js`

## Output Format

```json
{
  "design_type": "2^4 Full Factorial",
  "factors": ["Temperature", "Pressure", "Time", "Catalyst"],
  "num_runs": 16,
  "analysis": {
    "significant_factors": ["Temperature", "Pressure"],
    "significant_interactions": ["Temperature:Pressure"],
    "r_squared": 0.94
  },
  "optimal_settings": {
    "Temperature": 180,
    "Pressure": 2.5,
    "Time": 60,
    "Catalyst": 0.5
  },
  "predicted_response": 95.3,
  "confirmation_plan": {
    "runs": 5,
    "prediction_interval": [93.1, 97.5]
  }
}
```

## Best Practices

1. **Start with screening** - Use Plackett-Burman for many factors
2. **Choose appropriate resolution** - Resolution IV minimum for main effects
3. **Include center points** - Detect curvature
4. **Randomize run order** - Reduce systematic bias
5. **Replicate** - Estimate error for significance testing
6. **Confirm results** - Always run confirmation experiments

## Constraints

- Document all experimental conditions
- Control nuisance factors
- Follow design exactly as planned
- Report both practical and statistical significance

``````

## 101 · 工业业务流程挖掘

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/industrial-engineering/skills/process-mining-analyzer

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/process-mining-analyzer/SKILL.md

``````markdown
---
name: process-mining-analyzer
description: Process mining skill for event log analysis, process discovery, and conformance checking.
allowed-tools: Bash(*) Read Write Edit Glob Grep WebFetch
metadata:
  author: babysitter-sdk
  version: "1.0.0"
  category: work-measurement
  backlog-id: SK-IE-036
graph:
  domains: [domain:industrial-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:organizational-design, skill-area:data-analysis]
  roles: [role:operations-analyst, role:research-engineer]
---

# process-mining-analyzer

You are **process-mining-analyzer** - a specialized skill for process mining including event log analysis, process discovery, and conformance checking.

## Overview

This skill enables AI-powered process mining including:
- Event log preparation and cleaning
- Process discovery algorithms (Alpha, Heuristic Miner)
- Conformance checking
- Performance analysis
- Bottleneck identification
- Variant analysis
- Social network analysis
- Dotted chart visualization

## Capabilities

### 1. Event Log Preparation

```python
import pandas as pd
import numpy as np
from datetime import datetime
from collections import defaultdict

def prepare_event_log(raw_data: pd.DataFrame, mappings: dict):
    """
    Prepare event log for process mining

    raw_data: DataFrame with raw event data
    mappings: {'case_id': col, 'activity': col, 'timestamp': col, 'resource': col}
    """
    # Map columns
    event_log = pd.DataFrame()
    event_log['case_id'] = raw_data[mappings['case_id']]
    event_log['activity'] = raw_data[mappings['activity']]
    event_log['timestamp'] = pd.to_datetime(raw_data[mappings['timestamp']])

    if 'resource' in mappings and mappings['resource'] in raw_data.columns:
        event_log['resource'] = raw_data[mappings['resource']]

    # Sort by case and timestamp
    event_log = event_log.sort_values(['case_id', 'timestamp'])

    # Add derived columns
    event_log['event_id'] = range(len(event_log))

    # Calculate duration to next event
    event_log['next_timestamp'] = event_log.groupby('case_id')['timestamp'].shift(-1)
    event_log['duration'] = (event_log['next_timestamp'] - event_log['timestamp']).dt.total_seconds()

    # Statistics
    stats = {
        'total_events': len(event_log),
        'total_cases': event_log['case_id'].nunique(),
        'unique_activities': event_log['activity'].nunique(),
        'activities': event_log['activity'].unique().tolist(),
        'date_range': {
            'start': str(event_log['timestamp'].min()),
            'end': str(event_log['timestamp'].max())
        }
    }

    return {
        'event_log': event_log,
        'statistics': stats
    }
```

### 2. Process Discovery

```python
def discover_process_model(event_log: pd.DataFrame):
    """
    Discover process model from event log using footprint analysis
    """
    # Build directly-follows graph
    dfg = defaultdict(int)
    start_activities = set()
    end_activities = set()

    for case_id, case_data in event_log.groupby('case_id'):
        activities = case_data['activity'].tolist()

        if activities:
            start_activities.add(activities[0])
            end_activities.add(activities[-1])

        for i in range(len(activities) - 1):
            dfg[(activities[i], activities[i + 1])] += 1

    # Build footprint matrix
    activities = sorted(event_log['activity'].unique())
    n = len(activities)
    act_idx = {a: i for i, a in enumerate(activities)}

    # Relations: > (directly follows), < (preceded by), || (parallel), # (no relation)
    relations = {}

    for a1 in activities:
        for a2 in activities:
            a1_to_a2 = dfg.get((a1, a2), 0)
            a2_to_a1 = dfg.get((a2, a1), 0)

            if a1_to_a2 > 0 and a2_to_a1 > 0:
                relations[(a1, a2)] = '||'  # Parallel
            elif a1_to_a2 > 0:
                relations[(a1, a2)] = '>'   # Follows
            elif a2_to_a1 > 0:
                relations[(a1, a2)] = '<'   # Preceded by
            else:
                relations[(a1, a2)] = '#'   # No relation

    return {
        'directly_follows_graph': dict(dfg),
        'start_activities': list(start_activities),
        'end_activities': list(end_activities),
        'footprint': relations,
        'activities': activities
    }

def heuristic_miner(event_log: pd.DataFrame, dependency_threshold: float = 0.5):
    """
    Heuristic Miner algorithm for process discovery
    """
    # Build frequency tables
    activity_freq = event_log['activity'].value_counts().to_dict()
    dfg = defaultdict(int)

    for case_id, case_data in event_log.groupby('case_id'):
        activities = case_data['activity'].tolist()
        for i in range(len(activities) - 1):
            dfg[(activities[i], activities[i + 1])] += 1

    # Calculate dependency measure
    # D(a,b) = (|a>b| - |b>a|) / (|a>b| + |b>a| + 1)
    dependencies = {}
    activities = list(activity_freq.keys())

    for a in activities:
        for b in activities:
            a_to_b = dfg.get((a, b), 0)
            b_to_a = dfg.get((b, a), 0)

            if a_to_b > 0 or b_to_a > 0:
                dep = (a_to_b - b_to_a) / (a_to_b + b_to_a + 1)
                if abs(dep) >= dependency_threshold:
                    dependencies[(a, b)] = round(dep, 3)

    # Filter to positive dependencies (actual follows relations)
    causal_relations = {k: v for k, v in dependencies.items() if v > 0}

    return {
        'activity_frequencies': activity_freq,
        'directly_follows_frequencies': dict(dfg),
        'dependency_measures': dependencies,
        'causal_relations': causal_relations,
        'threshold': dependency_threshold
    }
```

### 3. Conformance Checking

```python
def check_conformance(event_log: pd.DataFrame, expected_sequence: list,
                     strict: bool = False):
    """
    Check conformance of traces against expected process

    expected_sequence: list of activities in expected order
    strict: if True, exact match required; if False, subsequence match
    """
    results = []

    for case_id, case_data in event_log.groupby('case_id'):
        trace = case_data['activity'].tolist()

        if strict:
            # Exact match
            is_conforming = trace == expected_sequence
            deviations = []

            if not is_conforming:
                # Find deviations
                for i, (actual, expected) in enumerate(zip(trace, expected_sequence)):
                    if actual != expected:
                        deviations.append({
                            'position': i,
                            'expected': expected,
                            'actual': actual
                        })

                # Check for missing or extra activities
                if len(trace) < len(expected_sequence):
                    deviations.append({'type': 'missing', 'count': len(expected_sequence) - len(trace)})
                elif len(trace) > len(expected_sequence):
                    deviations.append({'type': 'extra', 'count': len(trace) - len(expected_sequence)})

        else:
            # Check if expected is subsequence
            exp_idx = 0
            is_conforming = True

            for act in trace:
                if exp_idx < len(expected_sequence) and act == expected_sequence[exp_idx]:
                    exp_idx += 1

            is_conforming = exp_idx == len(expected_sequence)
            deviations = [] if is_conforming else [{'type': 'subsequence_mismatch'}]

        results.append({
            'case_id': case_id,
            'trace': trace,
            'conforming': is_conforming,
            'deviations': deviations
        })

    # Summary statistics
    conforming_count = sum(1 for r in results if r['conforming'])
    total = len(results)

    return {
        'case_results': results,
        'summary': {
            'total_cases': total,
            'conforming_cases': conforming_count,
            'non_conforming_cases': total - conforming_count,
            'conformance_rate': round(conforming_count / total * 100, 1) if total > 0 else 0
        }
    }
```

### 4. Performance Analysis

```python
def analyze_performance(event_log: pd.DataFrame):
    """
    Analyze process performance from event log
    """
    # Case duration
    case_durations = event_log.groupby('case_id').agg({
        'timestamp': ['min', 'max']
    })
    case_durations.columns = ['start', 'end']
    case_durations['duration_hours'] = (case_durations['end'] - case_durations['start']).dt.total_seconds() / 3600

    # Activity duration statistics
    activity_stats = event_log.groupby('activity')['duration'].agg(['mean', 'median', 'std', 'count']).reset_index()
    activity_stats.columns = ['activity', 'mean_duration', 'median_duration', 'std_duration', 'count']
    activity_stats['mean_duration'] = activity_stats['mean_duration'] / 60  # Convert to minutes

    # Identify bottlenecks (longest average duration)
    bottlenecks = activity_stats.nlargest(3, 'mean_duration')

    # Waiting time analysis
    waiting_times = event_log.copy()
    waiting_times['prev_end'] = waiting_times.groupby('case_id')['timestamp'].shift(1)
    waiting_times['waiting_time'] = (waiting_times['timestamp'] - waiting_times['prev_end']).dt.total_seconds() / 60
    waiting_times = waiting_times[waiting_times['waiting_time'].notna()]

    waiting_by_activity = waiting_times.groupby('activity')['waiting_time'].mean().reset_index()
    waiting_by_activity.columns = ['activity', 'avg_waiting_minutes']

    return {
        'case_duration': {
            'mean_hours': round(case_durations['duration_hours'].mean(), 2),
            'median_hours': round(case_durations['duration_hours'].median(), 2),
            'std_hours': round(case_durations['duration_hours'].std(), 2)
        },
        'activity_performance': activity_stats.to_dict('records'),
        'bottlenecks': bottlenecks[['activity', 'mean_duration']].to_dict('records'),
        'waiting_times': waiting_by_activity.to_dict('records')
    }
```

### 5. Variant Analysis

```python
def analyze_variants(event_log: pd.DataFrame):
    """
    Analyze process variants (unique traces)
    """
    # Get trace for each case
    traces = event_log.groupby('case_id')['activity'].apply(lambda x: '->'.join(x)).reset_index()
    traces.columns = ['case_id', 'trace']

    # Count variants
    variant_counts = traces['trace'].value_counts().reset_index()
    variant_counts.columns = ['variant', 'count']
    variant_counts['percentage'] = round(variant_counts['count'] / len(traces) * 100, 1)
    variant_counts['cumulative_pct'] = variant_counts['percentage'].cumsum()

    # Get duration by variant
    case_durations = event_log.groupby('case_id').agg({
        'timestamp': ['min', 'max']
    })
    case_durations.columns = ['start', 'end']
    case_durations['duration_hours'] = (case_durations['end'] - case_durations['start']).dt.total_seconds() / 3600
    case_durations = case_durations.reset_index()

    traces_with_duration = traces.merge(case_durations[['case_id', 'duration_hours']], on='case_id')
    variant_duration = traces_with_duration.groupby('trace')['duration_hours'].mean().reset_index()
    variant_duration.columns = ['variant', 'avg_duration_hours']

    variant_analysis = variant_counts.merge(variant_duration, on='variant')

    return {
        'total_cases': len(traces),
        'unique_variants': len(variant_counts),
        'top_variants': variant_analysis.head(10).to_dict('records'),
        'pareto': {
            'variants_for_80pct': len(variant_analysis[variant_analysis['cumulative_pct'] <= 80]) + 1
        }
    }
```

### 6. Social Network Analysis

```python
def analyze_handoffs(event_log: pd.DataFrame):
    """
    Analyze resource handoffs for social network analysis
    """
    if 'resource' not in event_log.columns:
        return {"error": "Resource column not available"}

    handoffs = defaultdict(int)

    for case_id, case_data in event_log.groupby('case_id'):
        resources = case_data['resource'].tolist()
        for i in range(len(resources) - 1):
            if resources[i] != resources[i + 1]:  # Different resource
                handoffs[(resources[i], resources[i + 1])] += 1

    # Calculate metrics
    resources = set()
    for (r1, r2) in handoffs.keys():
        resources.add(r1)
        resources.add(r2)

    # Centrality - how often a resource is involved in handoffs
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for (r1, r2), count in handoffs.items():
        out_degree[r1] += count
        in_degree[r2] += count

    resource_metrics = []
    for r in resources:
        resource_metrics.append({
            'resource': r,
            'in_degree': in_degree[r],
            'out_degree': out_degree[r],
            'total_handoffs': in_degree[r] + out_degree[r]
        })

    resource_metrics.sort(key=lambda x: x['total_handoffs'], reverse=True)

    return {
        'handoff_matrix': dict(handoffs),
        'resource_metrics': resource_metrics,
        'total_handoffs': sum(handoffs.values()),
        'unique_resource_pairs': len(handoffs)
    }
```

## Process Integration

This skill integrates with the following processes:
- `process-discovery-analysis.js`
- `conformance-checking-audit.js`
- `process-improvement-analysis.js`

## Output Format

```json
{
  "event_log_stats": {
    "total_events": 15000,
    "total_cases": 500,
    "unique_activities": 12
  },
  "process_model": {
    "start_activities": ["Register"],
    "end_activities": ["Close"],
    "directly_follows": {"Register->Approve": 450}
  },
  "conformance": {
    "conformance_rate": 85.2
  },
  "performance": {
    "avg_case_duration_hours": 24.5,
    "bottlenecks": ["Approval", "Review"]
  },
  "variants": {
    "unique": 45,
    "top_variant_coverage": 65.2
  }
}
```

## Best Practices

1. **Clean event log** - Remove noise and duplicates
2. **Validate timestamps** - Ensure correct ordering
3. **Define case concept** - Clear case ID definition
4. **Iterative discovery** - Refine with domain experts
5. **Combine techniques** - Use multiple algorithms
6. **Focus on deviations** - They reveal improvement opportunities

## Constraints

- Requires quality event data
- Complex processes may be hard to visualize
- Timestamps must be accurate
- Parallel activities add complexity

``````

## 102 · 人工搬举作业风险评估

原技能：https://github.com/a5c-ai/babysitter/tree/main/library/specializations/domains/science/industrial-engineering/skills/niosh-lifting-calculator

固定版本原文：https://raw.githubusercontent.com/a5c-ai/babysitter/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/niosh-lifting-calculator/SKILL.md

``````markdown
---
name: niosh-lifting-calculator
description: NIOSH Lifting Equation calculator for manual material handling risk assessment.
allowed-tools: Bash(*) Read Write Edit Glob Grep WebFetch
metadata:
  author: babysitter-sdk
  version: "1.0.0"
  category: ergonomics
  backlog-id: SK-IE-020
graph:
  domains: [domain:industrial-engineering]
  skillAreas: [skill-area:statistical-analysis, skill-area:organizational-design, skill-area:data-analysis]
  roles: [role:operations-analyst, role:research-engineer]
---

# niosh-lifting-calculator

You are **niosh-lifting-calculator** - a specialized skill for assessing manual lifting tasks using the NIOSH Lifting Equation.

## Overview

This skill enables AI-powered lifting risk assessment including:
- Recommended Weight Limit (RWL) calculation
- Lifting Index (LI) computation
- Multiplier factor analysis (HM, VM, DM, AM, FM, CM)
- Single-task and multi-task analysis
- Risk level classification
- Work redesign recommendations
- Comparison of job modifications

## Capabilities

### 1. NIOSH Lifting Equation

```python
from dataclasses import dataclass
from typing import Optional
import math

@dataclass
class LiftingTaskParameters:
    """
    Input parameters for NIOSH Lifting Equation
    """
    # Load characteristics
    load_weight_lbs: float  # Actual weight being lifted

    # Origin parameters
    horizontal_origin: float  # H: Horizontal distance from midpoint between ankles (inches)
    vertical_origin: float  # V: Vertical height at origin (inches)

    # Destination parameters
    horizontal_dest: float  # H at destination
    vertical_dest: float  # V at destination

    # Task parameters
    vertical_travel: float  # D: Vertical travel distance (inches)
    asymmetry_angle: float  # A: Angle of asymmetry (degrees)
    frequency: float  # F: Lifts per minute
    duration: float  # Duration category: 1 (≤1hr), 2 (1-2hr), 8 (2-8hr)
    coupling: str  # "good", "fair", "poor"

def calculate_rwl(params: LiftingTaskParameters, at_origin: bool = True):
    """
    Calculate Recommended Weight Limit using NIOSH equation

    RWL = LC x HM x VM x DM x AM x FM x CM

    LC = Load Constant = 51 lbs
    """
    LC = 51  # Load Constant in lbs

    # Select origin or destination for location-specific RWL
    H = params.horizontal_origin if at_origin else params.horizontal_dest
    V = params.vertical_origin if at_origin else params.vertical_dest

    # Horizontal Multiplier (HM)
    # HM = 10/H, where H is between 10-25 inches
    H = max(10, min(H, 25))  # Clamp to valid range
    HM = 10 / H

    # Vertical Multiplier (VM)
    # VM = 1 - 0.0075|V - 30|
    VM = 1 - 0.0075 * abs(V - 30)
    VM = max(0, VM)  # Cannot be negative

    # Distance Multiplier (DM)
    # DM = 0.82 + 1.8/D
    D = max(10, params.vertical_travel)  # Minimum 10 inches
    DM = 0.82 + (1.8 / D)
    DM = min(1, DM)  # Cannot exceed 1

    # Asymmetric Multiplier (AM)
    # AM = 1 - 0.0032A
    A = min(135, params.asymmetry_angle)  # Max 135 degrees
    AM = 1 - (0.0032 * A)

    # Frequency Multiplier (FM)
    FM = get_frequency_multiplier(params.frequency, params.duration, V)

    # Coupling Multiplier (CM)
    CM = get_coupling_multiplier(params.coupling, V)

    # Calculate RWL
    RWL = LC * HM * VM * DM * AM * FM * CM

    return {
        "RWL": round(RWL, 1),
        "multipliers": {
            "LC": LC,
            "HM": round(HM, 3),
            "VM": round(VM, 3),
            "DM": round(DM, 3),
            "AM": round(AM, 3),
            "FM": round(FM, 3),
            "CM": round(CM, 3)
        },
        "location": "origin" if at_origin else "destination"
    }

def get_frequency_multiplier(frequency, duration, vertical):
    """
    Frequency Multiplier lookup table
    """
    # Simplified FM table
    FM_TABLE = {
        # (frequency, duration, V>=30): FM value
        (0.2, 1, True): 1.00, (0.2, 1, False): 1.00,
        (0.5, 1, True): 0.97, (0.5, 1, False): 0.97,
        (1, 1, True): 0.94, (1, 1, False): 0.94,
        (2, 1, True): 0.91, (2, 1, False): 0.91,
        (3, 1, True): 0.88, (3, 1, False): 0.88,
        (4, 1, True): 0.84, (4, 1, False): 0.84,
        (5, 1, True): 0.80, (5, 1, False): 0.80,
        # Add more as needed
    }

    # Find closest match or interpolate
    v_category = vertical >= 30
    key = (min(15, frequency), int(duration), v_category)

    # Default approximation
    if frequency <= 0.2:
        return 1.0
    elif frequency >= 15:
        return 0.0
    else:
        # Linear approximation
        return max(0, 1 - 0.05 * frequency)

def get_coupling_multiplier(coupling, vertical):
    """
    Coupling Multiplier based on handle quality
    """
    CM_TABLE = {
        ("good", True): 1.00,
        ("good", False): 1.00,
        ("fair", True): 0.95,
        ("fair", False): 1.00,
        ("poor", True): 0.90,
        ("poor", False): 0.90
    }

    v_category = vertical >= 30
    return CM_TABLE.get((coupling.lower(), v_category), 0.90)
```

### 2. Lifting Index Calculation

```python
def calculate_lifting_index(params: LiftingTaskParameters):
    """
    Calculate Lifting Index

    LI = Load Weight / RWL

    LI interpretation:
    - LI ≤ 1.0: Acceptable for most workers
    - 1.0 < LI ≤ 3.0: Increased risk, some workers may be at risk
    - LI > 3.0: Unacceptable for most workers
    """
    # Calculate RWL at both origin and destination
    rwl_origin = calculate_rwl(params, at_origin=True)
    rwl_dest = calculate_rwl(params, at_origin=False)

    # Use the more restrictive (lower) RWL
    rwl = min(rwl_origin['RWL'], rwl_dest['RWL'])
    limiting_location = "origin" if rwl_origin['RWL'] < rwl_dest['RWL'] else "destination"

    # Calculate Lifting Index
    li = params.load_weight_lbs / rwl if rwl > 0 else float('inf')

    # Risk classification
    if li <= 1.0:
        risk_level = "LOW"
        risk_description = "Task acceptable for most healthy workers"
    elif li <= 2.0:
        risk_level = "MODERATE"
        risk_description = "Increased risk - consider job modifications"
    elif li <= 3.0:
        risk_level = "HIGH"
        risk_description = "High risk - job redesign recommended"
    else:
        risk_level = "VERY HIGH"
        risk_description = "Unacceptable risk - immediate redesign required"

    return {
        "lifting_index": round(li, 2),
        "rwl": rwl,
        "rwl_origin": rwl_origin['RWL'],
        "rwl_dest": rwl_dest['RWL'],
        "limiting_location": limiting_location,
        "actual_weight": params.load_weight_lbs,
        "risk_level": risk_level,
        "risk_description": risk_description,
        "multipliers_origin": rwl_origin['multipliers'],
        "multipliers_dest": rwl_dest['multipliers']
    }
```

### 3. Multi-Task Analysis

```python
def multi_task_lifting_index(tasks: list):
    """
    Calculate Composite Lifting Index for multiple tasks

    CLI = LI_max + sum of (LI_adjusted for remaining tasks)
    """
    if not tasks:
        return None

    # Calculate individual LIs
    task_results = []
    for task in tasks:
        result = calculate_lifting_index(task['params'])
        result['task_name'] = task.get('name', 'Unnamed')
        result['frequency'] = task['params'].frequency
        task_results.append(result)

    # Sort by LI descending
    task_results.sort(key=lambda x: x['lifting_index'], reverse=True)

    # Calculate CLI
    cli = task_results[0]['lifting_index']

    for i in range(1, len(task_results)):
        # Frequency adjustment for additional tasks
        # Simplified: add fraction of each additional LI
        freq_factor = sum(t['frequency'] for t in task_results[:i+1]) / \
                     sum(t['frequency'] for t in task_results[:i])
        cli += task_results[i]['lifting_index'] * (freq_factor - 1) / freq_factor

    return {
        "composite_lifting_index": round(cli, 2),
        "individual_tasks": task_results,
        "most_stressful_task": task_results[0]['task_name'],
        "risk_level": get_risk_level(cli)
    }

def get_risk_level(li):
    if li <= 1.0:
        return "LOW"
    elif li <= 2.0:
        return "MODERATE"
    elif li <= 3.0:
        return "HIGH"
    else:
        return "VERY HIGH"
```

### 4. Multiplier Analysis and Recommendations

```python
def analyze_multipliers(result: dict):
    """
    Identify which factors are limiting and provide recommendations
    """
    multipliers = result.get('multipliers_origin', {})
    limiting_factors = []

    # Identify factors below threshold
    thresholds = {
        "HM": 0.7,  # Horizontal distance issue
        "VM": 0.8,  # Vertical height issue
        "DM": 0.8,  # Travel distance issue
        "AM": 0.8,  # Asymmetry issue
        "FM": 0.7,  # Frequency issue
        "CM": 0.9   # Coupling issue
    }

    recommendations = []

    for factor, threshold in thresholds.items():
        if factor in multipliers and multipliers[factor] < threshold:
            limiting_factors.append(factor)

            if factor == "HM":
                recommendations.append({
                    "factor": "Horizontal Distance",
                    "issue": f"HM = {multipliers[factor]:.2f} - load too far from body",
                    "recommendations": [
                        "Move load closer to worker",
                        "Use conveyors or slides",
                        "Eliminate obstacles between worker and load",
                        "Reduce container width"
                    ]
                })
            elif factor == "VM":
                recommendations.append({
                    "factor": "Vertical Location",
                    "issue": f"VM = {multipliers[factor]:.2f} - lift height not optimal",
                    "recommendations": [
                        "Raise or lower origin/destination",
                        "Use lift tables or platforms",
                        "Eliminate floor-level or overhead lifts"
                    ]
                })
            elif factor == "DM":
                recommendations.append({
                    "factor": "Travel Distance",
                    "issue": f"DM = {multipliers[factor]:.2f} - excessive vertical travel",
                    "recommendations": [
                        "Reduce vertical travel distance",
                        "Use mechanical assists for long lifts",
                        "Reposition origin and destination"
                    ]
                })
            elif factor == "AM":
                recommendations.append({
                    "factor": "Asymmetry",
                    "issue": f"AM = {multipliers[factor]:.2f} - twisting required",
                    "recommendations": [
                        "Reposition load or destination to eliminate twist",
                        "Use turntables",
                        "Improve workstation layout"
                    ]
                })
            elif factor == "FM":
                recommendations.append({
                    "factor": "Frequency",
                    "issue": f"FM = {multipliers[factor]:.2f} - high lifting frequency",
                    "recommendations": [
                        "Reduce lifting frequency",
                        "Add job rotation",
                        "Use mechanical assists",
                        "Add rest breaks"
                    ]
                })
            elif factor == "CM":
                recommendations.append({
                    "factor": "Coupling",
                    "issue": f"CM = {multipliers[factor]:.2f} - poor grip/handles",
                    "recommendations": [
                        "Add handles to containers",
                        "Use containers with hand-holds",
                        "Improve grip surface"
                    ]
                })

    return {
        "limiting_factors": limiting_factors,
        "recommendations": recommendations,
        "priority": limiting_factors[0] if limiting_factors else None
    }
```

### 5. Job Modification Comparison

```python
def compare_modifications(baseline: LiftingTaskParameters, modifications: list):
    """
    Compare baseline to proposed modifications
    """
    baseline_result = calculate_lifting_index(baseline)

    comparisons = [{
        "scenario": "Baseline",
        "changes": None,
        "lifting_index": baseline_result['lifting_index'],
        "rwl": baseline_result['rwl'],
        "risk_level": baseline_result['risk_level'],
        "improvement": 0
    }]

    for mod in modifications:
        mod_result = calculate_lifting_index(mod['params'])
        improvement = (baseline_result['lifting_index'] - mod_result['lifting_index']) / \
                     baseline_result['lifting_index'] * 100

        comparisons.append({
            "scenario": mod['name'],
            "changes": mod.get('description', ''),
            "lifting_index": mod_result['lifting_index'],
            "rwl": mod_result['rwl'],
            "risk_level": mod_result['risk_level'],
            "improvement": round(improvement, 1)
        })

    # Sort by improvement
    comparisons.sort(key=lambda x: x['lifting_index'])

    return {
        "comparisons": comparisons,
        "best_scenario": comparisons[0]['scenario'],
        "best_improvement": comparisons[0]['improvement']
    }
```

## Process Integration

This skill integrates with the following processes:
- `ergonomic-risk-assessment.js`
- `workstation-design-optimization.js`

## Output Format

```json
{
  "lifting_index": 1.8,
  "rwl": 28.3,
  "actual_weight": 51,
  "risk_level": "MODERATE",
  "limiting_factors": ["HM", "AM"],
  "recommendations": [
    {
      "factor": "Horizontal Distance",
      "recommendations": ["Move load closer to worker"]
    }
  ],
  "improvement_options": [
    {
      "scenario": "Add lift table",
      "improvement": 45
    }
  ]
}
```

## Best Practices

1. **Measure accurately** - Use tape measure, goniometer
2. **Worst case analysis** - Assess most strenuous conditions
3. **Consider variations** - Different workers, load sizes
4. **Multi-task jobs** - Use CLI for varied tasks
5. **Verify after changes** - Re-assess after modifications
6. **Document everything** - Photos, measurements, observations

## Constraints

- NIOSH equation has limitations (no pushing/pulling)
- Valid for two-handed lifts only
- Assumes adequate grip
- Does not account for environmental factors

``````
