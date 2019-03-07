import sys
import subprocess

try:
    # Read charger & battery status
    with open('/sys/class/power_supply/ADP1/online', 'r') as a:
        ac_stat = bool(int(a.readline()))
        print(f'Plugged in: {ac_stat}')
    with open('/sys/class/power_supply/CMB0/capacity', 'r') as b:
        bat_pct = int(b.readline())
        print(f'Capacity: {bat_pct}')
except IOError:
    # Exit on error
    sys.exit()

# Determine when to notify start/stop charging.
# Check whether charging:
if ac_stat:
    print('Battery is charging.')
    # Check battery percentage
    if bat_pct >= 60:
        print("Battery above 60%, stop charging!")
else:
    print('Battery is discharging.')
    # Check battery percentage
    if bat_pct <= 40:
        print("Battery below 40%, start charging!")

### Use notify-send to display a notification pop up.
subprocess.run(['notify-send', 'hello world'])

