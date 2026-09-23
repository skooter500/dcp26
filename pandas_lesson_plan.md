# Pandas Lesson Plan: Analyzing Irish Traditional Music
## Dataset: 24,000 Traditional Irish Tunes in ABC Notation

---

## **Lesson 1: Loading and Exploring Data (45 min)**

### Learning Objectives
- Load CSV files with pandas
- Understand DataFrame structure
- Explore basic dataset properties

### Exercises

**Exercise 1.1: Load and Inspect**
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('irish_music.csv')

# Basic exploration
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
```

**Exercise 1.2: Understanding Columns**
- What data type is each column?
- How many rows and columns are there?
- Which columns have missing values?

**Exercise 1.3: Quick Statistics**
```python
# Get summary statistics
print(df.describe())
print(df['downloaded'].describe())
```

**Discussion Questions:**
- What does the 'downloaded' column represent?
- Why might some tunes have more downloads than others?

---

## **Lesson 2: Selection and Filtering (60 min)**

### Learning Objectives
- Select specific columns
- Filter rows based on conditions
- Use boolean indexing

### Exercises

**Exercise 2.1: Column Selection**
```python
# Select single column
titles = df['title']

# Select multiple columns
basic_info = df[['title', 'tune_type', 'key_sig']]
```

**Exercise 2.2: Filtering Basics**
```python
# Find all reels
reels = df[df['tune_type'] == 'reel']

# Find tunes in E minor
emin_tunes = df[df['key_sig'] == 'Emin']

# Find popular tunes (>1000 downloads)
popular = df[df['downloaded'] > 1000]
```

**Exercise 2.3: Multiple Conditions**
```python
# Find popular jigs
popular_jigs = df[(df['tune_type'] == 'jig') & (df['downloaded'] > 1000)]

# Find tunes in D major OR G major
d_or_g = df[df['key_sig'].isin(['Dmaj', 'Gmaj'])]

# Find unpopular hornpipes (<500 downloads)
unpopular_hornpipes = df[(df['tune_type'] == 'hornpipe') & (df['downloaded'] < 500)]
```

**Challenge Exercise:**
Find the top 10 most downloaded reels in D major.

---

## **Lesson 3: Grouping and Aggregation (60 min)**

### Learning Objectives
- Use groupby() for categorical analysis
- Apply aggregation functions
- Understand split-apply-combine

### Exercises

**Exercise 3.1: Count by Category**
```python
# How many of each tune type?
tune_counts = df['tune_type'].value_counts()

# How many tunes in each key?
key_counts = df['key_sig'].value_counts()
```

**Exercise 3.2: Groupby Statistics**
```python
# Average downloads by tune type
avg_by_type = df.groupby('tune_type')['downloaded'].mean()

# Multiple statistics
stats_by_type = df.groupby('tune_type')['downloaded'].agg(['mean', 'median', 'min', 'max', 'count'])
```

**Exercise 3.3: Multi-level Grouping**
```python
# Average downloads by tune type AND key signature
type_key_stats = df.groupby(['tune_type', 'key_sig'])['downloaded'].mean()

# Which combination is most popular?
most_popular_combo = type_key_stats.sort_values(ascending=False).head(10)
```

**Challenge Exercise:**
Find the most popular time signature for each tune type.

---

## **Lesson 4: Sorting and Ranking (45 min)**

### Learning Objectives
- Sort DataFrames by single and multiple columns
- Understand ascending vs descending order
- Find top N values

### Exercises

**Exercise 4.1: Basic Sorting**
```python
# Sort by downloads (least to most)
least_popular = df.sort_values('downloaded')

# Sort by downloads (most to least)
most_popular = df.sort_values('downloaded', ascending=False)
```

**Exercise 4.2: Multi-column Sorting**
```python
# Sort by tune type, then by downloads within each type
sorted_df = df.sort_values(['tune_type', 'downloaded'], ascending=[True, False])
```

**Exercise 4.3: Top N Analysis**
```python
# Top 20 most downloaded tunes
top_20 = df.nlargest(20, 'downloaded')

# Bottom 20 least downloaded tunes
bottom_20 = df.nsmallest(20, 'downloaded')

# Top 5 tunes for each tune type
top_per_type = df.groupby('tune_type').apply(lambda x: x.nlargest(5, 'downloaded'))
```

**Challenge Exercise:**
Create a ranking of tune types by their median popularity.

---

## **Lesson 5: Missing Data and Data Cleaning (60 min)**

### Learning Objectives
- Identify missing values
- Handle NaN values
- Clean and transform data

### Exercises

**Exercise 5.1: Finding Missing Data**
```python
# Count missing values per column
missing_counts = df.isnull().sum()

# Percentage of missing values
missing_pct = (df.isnull().sum() / len(df)) * 100

# Which columns have missing data?
cols_with_missing = df.columns[df.isnull().any()].tolist()
```

**Exercise 5.2: Handling Missing Data**
```python
# Drop rows with any missing values
df_no_missing = df.dropna()

# Drop rows where specific columns are missing
df_with_title = df.dropna(subset=['title'])

# Fill missing values
df_filled = df.fillna({'alt_title': 'Unknown', 'source': 'Not specified'})
```

**Exercise 5.3: Data Validation**
```python
# Check for duplicate titles
duplicates = df[df.duplicated(subset=['title'], keep=False)]

# Find unusual values
print(df['time_sig'].unique())
print(df['tune_type'].unique())

# Check for outliers in downloads
print(df['downloaded'].quantile([0.25, 0.5, 0.75, 0.95, 0.99]))
```

---

## **Lesson 6: String Operations (60 min)**

### Learning Objectives
- Use pandas string methods
- Extract information from text
- Search and filter text data

### Exercises

**Exercise 6.1: Basic String Operations**
```python
# Find tunes with "Reel" in the title
has_reel = df[df['title'].str.contains('Reel', case=False, na=False)]

# Find tunes starting with "The"
starts_with_the = df[df['title'].str.startswith('The', na=False)]

# Convert titles to uppercase
df['title_upper'] = df['title'].str.upper()
```

**Exercise 6.2: String Extraction**
```python
# Count title length
df['title_length'] = df['title'].str.len()

# Extract time signature from notation column
# (This column contains ABC notation with time signature info)
df['notation_length'] = df['notation'].str.len()
```

**Exercise 6.3: String Analysis**
```python
# Most common words in tune titles
all_titles = ' '.join(df['title'].dropna())
# Further analysis with split and Counter...

# Find tunes with possessive apostrophes
possessive = df[df['title'].str.contains("'s", na=False)]
```

**Challenge Exercise:**
Extract the number of bars in each tune by analyzing the ABC notation format.

---

## **Lesson 7: Creating New Columns (45 min)**

### Learning Objectives
- Create calculated columns
- Use apply() for custom functions
- Categorize data

### Exercises

**Exercise 7.1: Simple Calculations**
```python
# Create popularity category
df['popularity'] = pd.cut(df['downloaded'], 
                          bins=[0, 500, 1500, 3000, float('inf')],
                          labels=['Low', 'Medium', 'High', 'Very High'])
```

**Exercise 7.2: Conditional Columns**
```python
# Is it a major or minor key?
df['mode'] = df['key_sig'].apply(lambda x: 'major' if 'maj' in str(x).lower() 
                                           else 'minor' if 'min' in str(x).lower() 
                                           else 'other')

# Is it in common time (4/4)?
df['is_4_4'] = df['time_sig'] == '4/4'
```

**Exercise 7.3: Complex Transformations**
```python
# Create a complexity score based on notation length
df['complexity'] = df['notation'].str.len() / 100

# Categorize time signatures
def categorize_time_sig(sig):
    if sig in ['4/4', '2/4', '2/2']:
        return 'simple_duple'
    elif sig in ['6/8', '9/8', '12/8']:
        return 'compound'
    else:
        return 'other'

df['time_category'] = df['time_sig'].apply(categorize_time_sig)
```

---

## **Lesson 8: Visualization with Pandas (60 min)**

### Learning Objectives
- Create basic plots directly from pandas
- Understand different plot types
- Visualize distributions and relationships

### Exercises

**Exercise 8.1: Distribution Plots**
```python
import matplotlib.pyplot as plt

# Histogram of downloads
df['downloaded'].hist(bins=50)
plt.xlabel('Number of Downloads')
plt.ylabel('Frequency')
plt.title('Distribution of Tune Popularity')
plt.show()

# Box plot by tune type
df.boxplot(column='downloaded', by='tune_type', figsize=(10, 6))
plt.show()
```

**Exercise 8.2: Bar Charts**
```python
# Count of each tune type
tune_counts = df['tune_type'].value_counts()
tune_counts.plot(kind='bar')
plt.title('Number of Tunes by Type')
plt.xlabel('Tune Type')
plt.ylabel('Count')
plt.show()

# Average downloads by key signature
key_avg = df.groupby('key_sig')['downloaded'].mean().sort_values(ascending=False)
key_avg.head(10).plot(kind='barh')
plt.show()
```

**Exercise 8.3: Advanced Visualizations**
```python
# Scatter plot: notation length vs downloads
df.plot.scatter(x='notation_length', y='downloaded', alpha=0.5)
plt.show()

# Multiple subplots for different tune types
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i, tune_type in enumerate(['reel', 'jig', 'hornpipe', 'slip jig']):
    row = i // 2
    col = i % 2
    subset = df[df['tune_type'] == tune_type]
    subset['downloaded'].hist(ax=axes[row, col], bins=30)
    axes[row, col].set_title(f'{tune_type.title()} Popularity')
plt.tight_layout()
plt.show()
```

---

## **Final Project: Comprehensive Analysis**

### Project Requirements
Students should create a Jupyter notebook that includes:

1. **Data Loading and Cleaning** (15 points)
   - Load the dataset
   - Identify and handle missing values
   - Document any data quality issues

2. **Exploratory Analysis** (25 points)
   - What is the most common tune type?
   - What is the most popular key signature?
   - What time signatures are represented?
   - Distribution of downloads across the dataset

3. **Advanced Questions** (30 points)
   - Which tune type is most popular on average?
   - Is there a relationship between key signature and popularity?
   - Do certain time signatures correlate with more downloads?
   - Which tune has the longest ABC notation?

4. **Visualization** (20 points)
   - At least 3 different plot types
   - Clear labels and titles
   - Meaningful insights from visualizations

5. **Insights and Conclusions** (10 points)
   - What did you learn about Irish traditional music?
   - What patterns did you discover?
   - What further questions would you explore?

---

## **Assessment Rubric**

| Category | Excellent (4) | Good (3) | Satisfactory (2) | Needs Improvement (1) |
|----------|---------------|----------|------------------|----------------------|
| Code Quality | Clean, well-commented code with proper pandas idioms | Mostly clean code with some comments | Code works but lacks organization | Code has errors or is poorly structured |
| Data Understanding | Deep insights with multiple perspectives | Good understanding of data patterns | Basic understanding demonstrated | Limited data comprehension |
| Technical Skills | Advanced pandas operations used correctly | Core pandas functions used well | Basic functions used adequately | Struggles with basic operations |
| Visualization | Professional, informative plots | Clear plots with good labels | Basic functional plots | Poor or missing visualizations |

---

## **Additional Resources**

- Pandas documentation: https://pandas.pydata.org/docs/
- ABC notation guide: http://abcnotation.com/
- Irish traditional music database: https://thesession.org/

## **Extension Activities**

For advanced students:
1. Parse the ABC notation to extract musical features (note distributions, range, etc.)
2. Build a recommendation system based on tune characteristics
3. Analyze patterns in tune titles using NLP techniques
4. Create an interactive dashboard using Plotly or Streamlit