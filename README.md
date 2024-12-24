# Locust Performance Testing Framework

## Overview
A comprehensive performance testing framework using Locust for API load testing. This project provides a structured approach to performance testing with real-time monitoring and detailed reporting capabilities.

[![Medium Article](https://img.shields.io/badge/Medium-Read%20Article-black)](https://medium.com/@poojamehta1197/load-testing-with-locust-a-comprehensive-guide-from-setup-to-analysis-83351a53a6c5)

## Features
- Real-time metrics monitoring
- Configurable test scenarios
- Detailed reporting capabilities
- Custom error handling
- Multiple endpoint testing
- Easy-to-use web interface

## Project Structure
```
locust-project/
├── config/
│   └── config.yaml         # Configuration settings
├── locustfiles/
│   ├── __init__.py
│   └── user_behavior.py    # Test scenarios
├── reports/
│   └── .gitkeep           # Directory for test reports
├── utils/
│   ├── __init__.py
│   └── helpers.py         # Utility functions
├── requirements.txt       # Project dependencies
└── run.py                # Main execution script
```

## Prerequisites
- Python 3.x
- pip3 (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/poojamehta01/locust-performance-framework.git
cd locust-performance-framework
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Running Tests

### Start Locust Server
```bash
locust -f locustfiles/user_behavior.py --web-port=8090 --host=https://jsonplaceholder.typicode.com
```

### Access Web Interface
1. Open your browser
2. Navigate to: `http://localhost:8090`
3. Configure test parameters:
   - Number of users
   - Spawn rate
   - Start the test

## Test Scenarios
Current implementation includes:
- GET `/posts` - Fetch all posts
- POST `/posts` - Create new post
- GET `/users/{id}` - Fetch user details
- GET `/comments?postId={id}` - Fetch post comments

## Reports
Test reports are automatically generated in the `reports/` directory:
- CSV reports for requests
- CSV reports for failures
- CSV reports for exceptions
- HTML reports for overall test results

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**Pooja Mehta**
- Medium: [@poojamehta1197](https://medium.com/@poojamehta1197)
- GitHub: [@poojamehta01](https://github.com/poojamehta01)

## Acknowledgments
- [Locust Documentation](https://docs.locust.io/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

---
Made with ❤️ for testers and developers