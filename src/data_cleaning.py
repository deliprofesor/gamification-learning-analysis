import pandas as pd
import os

# 1. Load data
input_path = 'data/raw/gamification_collaborative_learning.xlsx'
df = pd.read_excel(input_path)

# 2. Rename columns to English (Simplified & Clean)
new_columns = {
    'Seleccione que estudiante es :': 'student_id',
    'Misión de la gamificación que se evalúa': 'mission',
    'Motivación del grupo [Motivación del grupo]': 'motivation',
    'Desempeño de roles [Desempeño de roles]': 'role_performance',
    'Cumplimiento en realización de tareas o actividades. [Cumplimiento en realización de tareas o actividades.]': 'task_completion',
    'Aprendizaje e interacción grupal. [Aprendizaje e interacción grupal.]': 'learning_interaction',
    'Integraciónistas grupal [Integraciónistas grupal]': 'group_integration'
}
df = df.rename(columns=new_columns)

# 3. Drop useless columns
# We only keep the columns we renamed
df = df[list(new_columns.values())]

# 4. Numerical Transformation
def map_scores(text):
    if pd.isna(text): return None
    text = str(text).upper()
    if 'BAJO' in text: return 1
    if 'BÁSICO' in text: return 2
    if 'ALTO' in text: return 3
    if 'SUPERIOR' in text: return 4
    return None

score_cols = ['motivation', 'role_performance', 'task_completion', 'learning_interaction', 'group_integration']
for col in score_cols:
    df[col] = df[col].apply(map_scores)

# 5. Final Touch: Remove any rows that are completely empty or headers accidentally added
df = df.dropna(subset=['mission']) # Mission sütunu boşsa o satırı sil

# 6. Save
output_path = 'data/processed/cleaned_gamification_data.csv'
df.to_csv(output_path, index=False)

print("Data is now 100% clean and ready for analysis!")