import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# 1. Load Data
# Ensure the cleaned dataset is located in data/processed directory
data_path = 'data/processed/cleaned_gamification_data.csv'
df = pd.read_csv(data_path)

# Create output directory for visualizations if it does not exist
output_dir = 'reports/figures'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define evaluation categories for visualization
categories = ['motivation', 'role_performance', 'task_completion', 'learning_interaction', 'group_integration']

# 2. RADAR CHART - Overall Average Performance
# Prepare values and close the circular plot
values = df[categories].mean().values.flatten().tolist()
values += values[:1] 
angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
angles += angles[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories)
ax.plot(angles, values, linewidth=2, linestyle='solid', color='#1f77b4')
ax.fill(angles, values, '#1f77b4', alpha=0.3)
plt.title('Overall Gamification Performance (Scale 1-4)', size=15, y=1.1)
plt.savefig(f'{output_dir}/radar_chart.png', bbox_inches='tight')
print("Radar chart saved to reports/figures/radar_chart.png")

# 3. MISSION TREND CHART - Performance Evolution over Missions 1-6
plt.figure(figsize=(10, 6))
trend_data = df.groupby('mission')[categories].mean()
sns.lineplot(data=trend_data, markers=True, dashes=False, palette='viridis')
plt.title('Performance Trends Across Missions (1-6)', size=14)
plt.ylabel('Average Score (1-4)')
plt.xlabel('Mission Number')
plt.ylim(1, 4)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Dimensions', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(f'{output_dir}/mission_trend.png')
print("Mission trend chart saved to reports/figures/mission_trend.png")

# 4. CORRELATION HEATMAP - Relationship between different dimensions
plt.figure(figsize=(8, 6))
correlation_matrix = df[categories].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Between Gamification Dimensions', size=14)
plt.tight_layout()
plt.savefig(f'{output_dir}/correlation_heatmap.png')
print("Correlation heatmap saved to reports/figures/correlation_heatmap.png")

print("\nAll analysis and visualization tasks are complete!")