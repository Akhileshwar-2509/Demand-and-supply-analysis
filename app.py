import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Set the default Plotly theme
pio.templates.default = "plotly_white"

# Load the data
data = pd.read_csv('rides.csv')

# Display the first few rows of the data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Drop rows with missing values
data = data.dropna()

# Extract relevant columns for analysis
demand = data["Riders Active Per Hour"]
supply = data["Drivers Active Per Hour"]

# Create a scatter plot with a trendline for demand and supply analysis
figure = px.scatter(data, x="Drivers Active Per Hour",
                    y="Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)
figure.show()

# Calculate elasticity of demand with respect to the number of active drivers per hour
avg_demand = data['Riders Active Per Hour'].mean()
avg_supply = data['Drivers Active Per Hour'].mean()
pct_change_demand = (max(data['Riders Active Per Hour']) - min(data['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(data['Drivers Active Per Hour']) - min(data['Drivers Active Per Hour'])) / avg_supply * 100
elasticity = pct_change_demand / pct_change_supply

# Print the elasticity result
print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))

# Calculate the supply ratio for each level of driver activity
data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']

# Display the first few rows of the updated data
print(data.head())

# Create a scatter plot for Supply Ratio vs. Driver Activity
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], 
                         y=data['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)
fig.show()
