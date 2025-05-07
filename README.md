# Kenya-Oil-Pipeline-model.
## Geospatial model for optimizing oil pipeline routes in Kenya.
### 1. Business Understanding.
- Assess the risk of pipeline segments, design and recommend the most cost-effective route, ecnviromentally safe and socially acceptable pipeline route across regions in Kenya based on their proximity to populated settlements,transport infrastructure and ecological sight, aiming to identify High-Consequence Areas (HCAs) that may require enhanced safety measures or regulatory compliance.

#### 1.2. Problem Statement.
- Modern pipeline infrastructure is critical to energy distribution, but it increasingly faces significant operational risks — including environmental, human, and financial threats — due to aging assets, expanding urbanization, and complex regulatory pressures. Poorly planned pipeline routes can lead to high construction and maintencance cost, enviromental damage, legal conflicts and delays due to terrain challenges. Traditional pipeline risk assessment methods often rely on static, manual inspections, lagging behind the dynamic, real-world conditions that pipelines traverse.

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
**Nature of Pipeline Segments.**
![image](https://github.com/user-attachments/assets/3ee2e368-fafa-4988-b7be-2e06934b8055)
- Majority of the Pipeline lies (65%) `Above Ground` while 35% is `Below Ground`.

**Pipeline Coverage per County.**
![image](https://github.com/user-attachments/assets/2a5ff793-22e7-4c3f-99c0-2b40990691ef)
- The pipeline spans multiple counties, including urban areas like Nairobi and coastal counties such as Kilifi, Kwale, and Mombasa.
- Mombasa has the shortest pipeline coverage (6,127.97 meters), with a percentage coverage of `0.54%`, followed by Meru (17,984.79 meters).
- Kajiado has the longest pipeline coverage (390,091.30 meters) and highest percentage pipeline coverage with `34%`, followed by Taita Taveta (340,304.65 meters) with `30%`.

**Distribution of Risk to Settlements.**
![image](https://github.com/user-attachments/assets/6085746b-b999-4ec6-a423-47454277b7b7)
- The visualization above identifies high risk areas where pipelines pass through densely populated regions.
