# Sustainable Transportation - Homework 2

**Instructor:** Dr. Kermanshah

**Due Date:** 5 Day, 1404, 11:59 PM

---

## Objective

In this assignment, we aim to evaluate transportation accessibility. This assessment is one of the most important indicators in transportation and land use planning programs. This assessment must be done using accessibility to job opportunities for residents of Qazvin city through transportation modes using the standard procedures in transport and land use planning:

1. **Gravity-Based Accessibility Method** - Using a function with parameter 0.1068
2. **Cumulative Opportunities Method** - Using the 30-minute threshold method

---

## Data Provided

You will have three datasets in the folder:

- **Origin-Destination Travel Time Matrix** (O-D Travel Time Matrix): Based on travel times between residential zones and employment centers, including walking time, transfer waiting time, and transfer time (in minutes). File name -> /Users/keivanjamali/Projects/Pure-Python/P5/11-sustainable/HW2/data/qazvin_cen_to_cen_tt.csv

- **Geographic File with Zone Information**: Including zone identification, population and employment data for each zone, along with geographic information by 8 zones in the city. File name -> /Users/keivanjamali/Projects/Pure-Python/P5/11-sustainable/HW2/data/QazvinNeighborhoods_name_id_Mantagheh.geojson

- **Employment Data by Zone**: Number of jobs and information for each zone. File name -> /Users/keivanjamali/Projects/Pure-Python/P5/11-sustainable/HW2/data/qazvin_id_jobs_pop.xlsx

---

## Assignment Tasks

### Task 1: Generate Accessibility Indicators Table for Each Zone

Create a table with the following structure for each zone:

```
| id | jobs_grav | jobs_cumul30 |
```

Calculate accessibility indicators for each residential zone by aggregating the indicators. The table should be presented in the following format:

```
| Zone | jobs_grav | jobs_cumul30 |
```

Each zone may contain multiple zones.

### Task 2: Create an Accessibility Map

Create a map showing accessibility indicators for all zones using any tool of your choice:

- **Python**
- **QGIS**
- **ArcGIS**
- **Kepler.gl**
- **Folium**
- **Altair**
- Or any other mapping tool

Color the zones according to their accessibility indicators.

### Task 3: Compare Methods and Justify Your Choice

Describe which method (gravity-based or cumulative opportunities) is more appropriate and why, considering the geographic patterns and observed differences.

### Task 4: Analyze Geographic Patterns

Discuss the geographic patterns of accessibility inequality. Why are certain areas more accessible than others?

### Task 5: Recommendations for Improvement

Provide recommendations (minimum 4 points) to increase accuracy and reliability in the accessibility assessment process, considering the gravity-based concept and the reality of actual accessibility in your analysis.

---

## Submission Notes

All visualizations and analyses should be presented in the deliverable documents, with clear explanations and geographic representations of accessibility patterns.
