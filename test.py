import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_dates(start, end, n=10):
    return [start + timedelta(days=random.randint(0, (end - start).days)) for _ in range(n)]

# Constants for dataset generation
num_projects = 100
project_names = [f"Project {i+1}" for i in range(num_projects)]
start_dates = random_dates(datetime(2024, 1, 1), datetime(2024, 6, 30), num_projects)
end_dates = [start + timedelta(days=random.randint(30, 180)) for start in start_dates]
budgets = [round(random.uniform(20000, 100000), 2) for _ in range(num_projects)]
actual_costs = [round(random.uniform(10000, budget), 2) for budget in budgets]
team_sizes = [random.randint(3, 15) for _ in range(num_projects)]
statuses = random.choices(['Not Started', 'In Progress', 'Completed', 'On Hold'], k=num_projects)
priorities = random.choices(['Low', 'Medium', 'High'], k=num_projects)
risk_levels = random.choices(['Low', 'Medium', 'High'], k=num_projects)
client_satisfaction = [random.randint(1, 10) for _ in range(num_projects)]
completion_percentages = [round(random.uniform(0, 100), 2) for _ in range(num_projects)]

# Create the DataFrame
data = {
    "ProjectID": list(range(1, num_projects + 1)),
    "ProjectName": project_names,
    "StartDate": start_dates,
    "EndDate": end_dates,
    "Budget": budgets,
    "ActualCost": actual_costs,
    "TeamSize": team_sizes,
    "Status": statuses,
    "Priority": priorities,
    "RiskLevel": risk_levels,
    "ClientSatisfaction": client_satisfaction,
    "CompletionPercentage": completion_percentages
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("large_project_management_data.csv", index=False)

print("Dataset generated successfully!")



