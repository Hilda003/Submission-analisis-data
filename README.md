# Bike Sharing Dashboard

This project provides an interactive dashboard using Streamlit to visualize bike-sharing data.

## Features
- **Weekday vs. Weekend Rentals**: Compare bike rental trends on weekdays and weekends.
- **Hourly Rentals**: View the average number of rentals per hour of the day.
- **Correlation Heatmap**: Analyze correlations between different numerical features.

## Installation
### 1. Clone the repository (if applicable)
```sh
git clone <https://github.com/Hilda003/Submission-analisis-data.git
cd Submission-analisis-data
```

### 2. Install dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

## Running the Dashboard
To launch the Streamlit app, run:
```sh
streamlit run dashboard.py
```

## File Structure
- **dashboard.py**: The main script for running the Streamlit dashboard.
- **day_data.csv** & **hour_data.csv**: The datasets used for visualization.
- **requirements.txt**: List of required Python libraries.

## Dependencies (requirements.txt)
```
streamlit
pandas
seaborn
matplotlib
```

## Notes
- Ensure `day_data.csv` and `hour_data.csv` are in the same directory as `dashboard.py`.
- Modify the file paths in `pd.read_csv()` if the dataset location differs.

## Author
Hildatul Warddah
