import pandas as pd
from datetime import datetime

# Load data and parse datetime
df = pd.read_csv('/opt/mybatop/final.csv')
df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'], format='%m/%d/%y %H:%M:%S')
df = df.sort_values('DATETIME').reset_index(drop=True)

# Convert charge values to percentages
df['CHARGE_PCT'] = df['CHARGE_NOW'] / df['CHARGE_FULL'] * 100

# Initialize variables
cycle_count = 0
cumulative_discharge = 0
current_cycle_start = df['DATETIME'].iloc[0]
results = []

# Iterate through battery states
for i in range(1, len(df)):
    prev = df.iloc[i-1]
    curr = df.iloc[i]
    
    # Calculate time difference in hours
    time_diff = (curr['DATETIME'] - prev['DATETIME']).total_seconds() / 3600
    
    # Calculate discharge amount
    if prev['STATUS'] == 'Discharging':
        discharge_pct = prev['CHARGE_PCT'] - curr['CHARGE_PCT']
        cumulative_discharge += max(discharge_pct, 0)  # Handle charging interruptions
        
    # Track Active vs Connected Standby time
    if prev['STATE'] == 'Active':
        active_time = time_diff
        standby_time = 0
    else:
        active_time = 0
        standby_time = time_diff
    
    # Detect cycle completion (100% cumulative discharge)
    if cumulative_discharge >= 100:
        cycle_count += 1
        cumulative_discharge %= 100  # Carry over partial discharge
        
        # Record cycle details
        results.append({
            'cycle_number': cycle_count,
            'start_date': current_cycle_start.date(),
            'end_date': curr['DATETIME'].date(),
            'active_hours': active_time,
            'standby_hours': standby_time
        })
        
        current_cycle_start = curr['DATETIME']

# Create final dataframe
cycle_df = pd.DataFrame(results)

# Sum hours per cycle
summary_df = cycle_df.groupby('cycle_number').agg({
    'start_date': 'first',
    'end_date': 'last',
    'active_hours': 'sum',
    'standby_hours': 'sum'
}).reset_index()

print("Battery Usage per Cycle:")
print(summary_df.round(2))

# Optional: Save to CSV
summary_df.to_csv('battery_usage_per_cycle.csv', index=False)
