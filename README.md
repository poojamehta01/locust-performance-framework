# Locust Performance Testing Framework

## Overview
A comprehensive performance testing framework using Locust for API load testing. This project provides a structured approach to performance testing with real-time monitoring and detailed reporting capabilities.

Detailed guide available at: [Load Testing with Locust: A Comprehensive Guide](https://medium.com/@poojamehta1197/load-testing-with-locust-a-comprehensive-guide-from-setup-to-analysis-83351a53a6c5)

## Project Structure
locust-project/
├── config/
│   └── config.yaml         # Configuration settings
├── locustfiles/
│   ├── init.py
│   └── user_behavior.py    # Test scenarios
├── reports/
│   └── .gitkeep           # Directory for test reports
├── utils/
│   ├── init.py
│   └── helpers.py         # Utility functions
└── requirements.txt       # Project dependencies
Copy
## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/locust-performance-testing.git
cd locust-performance-testing

Install dependencies:

bashCopypip3 install -r requirements.txt
Running Tests

Start Locust:

bashCopylocust -f locustfiles/user_behavior.py --web-port=8090 --host=https://jsonplaceholder.typicode.com

Access the web interface:

Open your browser
Navigate to: http://localhost:8090



Author
Pooja Mehta

Medium: @poojamehta1197
