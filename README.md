# Kenya-Oil-Pipeline-model.
## Geospatial model for optimizing oil pipeline routes in Kenya.
### 1. Business Understanding.
- Assess the risk of pipeline segments, design and recommend the most cost-effective route, enviromentally safe and socially acceptable pipeline route across regions in Kenya based on their proximity to populated settlements,transport infrastructure and ecological sight, aiming to identify High-Consequence Areas (HCAs) that may require enhanced safety measures or regulatory compliance.

#### 1.2. Problem Statement.
- Modern pipeline infrastructure is critical to energy distribution, but it increasingly faces significant operational risks — including environmental, human and financial threats — due to aging assets, expanding urbanization, and complex regulatory pressures. Poorly planned pipeline routes can lead to high construction and maintencance cost, enviromental damage, legal conflicts and delays due to terrain challenges. Traditional pipeline risk assessment methods often rely on static, manual inspections, lagging behind the dynamic, real-world conditions that pipelines traverse.

#### 1.3. KEY BUSINESS QUESTIONS

1. Which pipeline segments are in or near high-risk population areas?

2. How does settlement type influence pipeline compliance?

3. Which segments violate the minimum safe distance regulations?

#### 1.4. Objectives.
- Develop an Intelligent Pipeline Risk Assessment System.
- Enhance Predictive Risk Modeling and Safety Prioritization.
- Provide a Scalable and Efficient Geospatial Risk Pipeline.
  

### 2. Data Understanding.
- To develop an intelligent machine learning system for pipeline risk assessment based on population exposure, the project relies on multiple structured geospatial datasets that capture pipeline geometries, settlement patterns, and inferred human presence across Kenya.

#### 2.1. Data sources.

### 3. Geographic Information System (GIS).
- **Nature of Pipeline Segments.**

![image](https://github.com/user-attachments/assets/3ee2e368-fafa-4988-b7be-2e06934b8055)
Majority of the Pipeline lies (65%) `Above Ground` while 35% is `Below Ground`.

- **Pipeline Coverage per County.**

![image](https://github.com/user-attachments/assets/2a5ff793-22e7-4c3f-99c0-2b40990691ef)
  - The pipeline spans multiple counties, including urban areas like Nairobi and coastal counties such as Kilifi, Kwale, and Mombasa.
  - Mombasa has the shortest pipeline coverage (6,127.97 meters), with a percentage coverage of `0.54%`, followed by Meru (17,984.79 meters).
  - Kajiado has the longest pipeline coverage (390,091.30 meters) and highest percentage pipeline coverage with `34%`, followed by Taita Taveta (340,304.65 meters) with `30%`.

- **Distribution of Risk to Settlements.**

![image](https://github.com/user-attachments/assets/6085746b-b999-4ec6-a423-47454277b7b7)

The visualization above identifies high risk areas where pipelines pass through densely populated regions.

- **Map Visual**

![image](https://github.com/user-attachments/assets/c3dc93f8-95a4-4c48-b233-bf0286b5242b)
The map above shows the features used for Geospatial Analysis and Modeling, the red line in represents the pipeline route that was predicted in the Turkana region.

### 4. Modeling
Modeling

Building on the rich geospatial datasets described in the Data Understanding section, our modeling approach aims to predict environmental risks associated with oil and gas pipelines in Kenya. We employed a stacking ensemble method to leverage the strengths of multiple machine learning models, enhancing predictive performance for the critical high-risk class.

**Stacking Ensemble**

Stacking, or stacked generalization, is an ensemble technique that integrates predictions from several base models through a meta-model, which learns how to optimally combine these predictions. This method was chosen to capture diverse learning patterns and mitigate the weaknesses of individual models, thereby enhancing generalization and robustness.

*Base Models*

The stacking ensemble incorporates three base models:

RandomForest: Selected for its ability to handle categorical data and provide feature importance scores, which are crucial for understanding key risk factors.
XGBoost: A gradient boosting algorithm that excels at handling imbalanced data and capturing complex interactions through residual correction.
Support Vector Machine (SVM): Chosen for its effectiveness in margin separation, particularly useful for distinguishing between risk categories with clear boundaries.

**Meta-Model**
A meta-model, typically a logistic regression or another simple classifier, is trained on the predictions of the base models to produce the final risk classification. This allows the ensemble to learn when to trust each base model, improving prediction accuracy for critical outcomes.

**Feature Engineering**
The model utilizes a rich set of geospatial features derived from various data sources, including:
Proximity Features: Distances to roads, settlements, waterways, and national parks, calculated using GeoPandas.

Categorical Features: Indicators such as whether a pipeline segment lies within a no-disturbance zone or its location type (above or below ground).

Engineered Features: Additional features like elevation changes or interaction terms may be included to capture complex risk factors.

Feature importance analysis highlights that distance to road and within no disturbance of settlement are particularly influential in predicting high-risk segments.

**Evaluation Metrics**

Given the class imbalance in pipeline risk data, we prioritize the weighted F1-score as the primary evaluation metric. This metric accounts for the differing class distributions by computing a weighted average of F1-scores for each risk category, ensuring that the model performs well across all classes, especially the critical high-risk segments.

Additionally, we focus on precision and recall for the high-risk class:

Precision: Ensures that predicted high-risk segments are indeed high-risk, minimizing false alarms and unnecessary maintenance costs.

Recall: Ensures that actual high-risk segments are correctly identified, preventing potential failures or environmental damage.

**Data Preparation**

Data preparation involves several steps using Python and GeoPandas:

Geometric Processing: Converting pipeline linestrings into lengths and extracting GPS point sequences.

Proximity Calculations: Determining distances to sensitive features like water bodies and protected areas.

Feature Extraction: Labeling pipelines based on risk rules and encoding categorical attributes.

Normalization: Scaling numerical features to ensure consistent model input.
### 5. Deployment
