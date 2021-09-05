import pandas as pd
data = pd.read_csv('data/budget_data.csv')
total_month = len(data)
total = data['Profit/Losses'].sum()
mean = data['Profit/Losses'].mean()
max = data['Profit/Losses'].max()
max_date = data['Date'][data['Profit/Losses'] == max].item()
min = data['Profit/Losses'].min()
min_date = data['Date'][data['Profit/Losses'] == min].item()

res = f'''Financial Analysis\n----------------------------
Total Months: {total_month}
Total: ${total}
Average  Change: ${mean:.2f}
Greatest Increase in Profits: {max_date} (${max})
Greatest Decrease in Profits: {min_date} (${min})'''

with open('Financial Analysis.txt', 'wt') as f:
    f.write(res)

print(res)
