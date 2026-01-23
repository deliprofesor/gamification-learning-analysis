# Data Dictionary: Gamification & Collaborative Learning Analysis

This data dictionary describes the variables used to evaluate student performance in collaborative group work within a gamified environment.

---

## 1. Primary Dimensions (Variables)

| Variable Name (Spanish) | Variable Name (English) | Definition |
| :--- | :--- | :--- |
| **Motivación del grupo** | **Group Motivation** | Measures the level of active participation and enthusiasm within the group. |
| **Desempeño de roles** | **Role Performance** | Assesses how clearly roles are defined and executed by group members. |
| **Cumplimiento de tareas** | **Task Completion** | Evaluates the quality and punctuality of activities or assigned tasks. |
| **Aprendizaje e interacción** | **Learning and Interaction** | Measures peer-to-peer communication and the level of shared knowledge acquisition. |
| **Integración grupal** | **Group Integration** | Refers to the group's ability to collaborate harmoniously and resolve conflicts. |

---

## 2. Qualitative Scale & Numerical Transformation

The categorical descriptions in the dataset were transformed into a numerical scale ($1-4$) for quantitative analysis.

| Scale Label (ES) | Scale Label (EN) | Value | Criteria Description |
| :--- | :--- | :---: | :--- |
| **SUPERIOR** | **Superior** | 4 | High quality, exceeds expectations, excellent collaboration. |
| **ALTO** | **High** | 3 | Good performance, minor delays or slight adaptation needed. |
| **BÁSICO** | **Basic** | 2 | Irregular participation, requires extra time or teacher support. |
| **BAJO** | **Low** | 1 | Poor motivation, tasks not completed, or role failure. |

---

## 3. Statistical Metadata (Quantitative Analysis)

These fields represent the calculated statistics found in the analysis reports.

* **Mean**: The average score calculated for each dimension (e.g., Group Motivation Mean is 2.9).
* **SD (Standard Deviation)**: Indicates the variability in student performance within that dimension.
* **Median**: The middle value of the data set (Consistently 3 across all dimensions).
* **Normalized_0to1**: A decimal representation ($0.7$) used for uniform chart scaling.
* **Angle_deg / Angle_rad**: Angular coordinates used to map dimensions on the Radar (Spider) Chart.

---

## 4. Student Records

* **Seleccione que estudiante es**: Identifier for the student (e.g., Estudiante 1 to Estudiante 11).
* **Comentarios**: Qualitative feedback or observations regarding group dynamics (mostly empty in raw data).
