from datetime import datetime, timedelta

# Current date
today = datetime.now()
print("Today:", today)

# After 90 days
after_90_days = today + timedelta(days=90)
print("After 90 days:", after_90_days)

# Before 90 days
before_90_days = today - timedelta(days=90)
print("Before 90 days:", before_90_days)

# After 6 months (manual using replace)
month = today.month + 6
year = today.year

# Handle year change if month > 12
if month > 12:
    month -= 12
    year += 1

# Keep same day if possible, else fallback (e.g., 31st Feb doesn’t exist)
try:
    after_6_months = today.replace(year=year, month=month)
except ValueError:
    # fallback to last valid day of new month
    after_6_months = today.replace(year=year, month=month, day=28)

print("After 6 months:", after_6_months)

# Total seconds in a month (assuming 30 days)
month_30 = timedelta(days=30)
print("Total seconds in 30 days (1 month):", month_30.total_seconds())
