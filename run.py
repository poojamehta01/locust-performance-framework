import os
from pathlib import Path
from datetime import datetime
import subprocess

def main():
    # Ensure reports directory exists
    reports_dir = Path(__file__).parent / 'reports'
    reports_dir.mkdir(exist_ok=True)

    # Generate timestamp for report files
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Define report file paths
    html_report = reports_dir / f'report_{timestamp}.html'
    csv_report = reports_dir / f'report_{timestamp}.csv'

    # Build the locust command
    cmd = [
        'locust',
        '-f', 'locustfiles/user_behavior.py',
        '--headless',  # Run in headless mode
        '-u', '10',    # Number of users
        '-r', '1',     # Spawn rate
        '-t', '1m',    # Run time
        '--html', str(html_report),
        '--csv', str(csv_report.with_suffix('')),  # Locust will add appropriate extensions
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Test completed successfully!")
        print(f"HTML report saved to: {html_report}")
        print(f"CSV report saved to: {csv_report}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Locust: {e}")
        return 1

if __name__ == "__main__":
    main()
