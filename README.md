URL Phishing Detection Tool
     A web-based **URL Phishing Detection Tool** developed using a rule-based approach to analyze URLs and identify potentially suspicious or phishing characteristics.

📌 Project Overview
       Phishing is a common cybersecurity threat in which attackers create deceptive URLs and websites to trick users into revealing sensitive information. This project provides a simple mechanism for analyzing URL characteristics and identifying potential phishing attempts.The system accepts a URL from the user, extracts relevant URL features, applies predefined security rules, calculates a risk score, and classifies the URL as Safe, Suspicious, or Phishing.

🎯 Objectives
* Detect potentially malicious URLs using predefined rules.
* Analyze important structural characteristics of URLs.
* Calculate a risk score based on detected indicators.
* Classify URLs into Safe, Suspicious, or Phishing categories.
* Provide quick and understandable results to users.
* Store URL analysis records using SQLite.

🛠️ Technologies Used

| Technology             | Purpose                                 |
| ---------------------- | --------------------------------------- |
| Python                 | Backend programming and detection logic |
| Flask                  | Web application framework               |
| HTML                   | Frontend structure                      |
| CSS                    | User interface styling                  |
| SQLite                 | Database management                     |
| Visual Studio Code     | Development environment                 |

🔍 Detection Features

The system analyzes several URL characteristics, including:
* HTTPS usage
* URL and domain length
* IP address usage
* Suspicious keywords
* Number of subdomains
* Special characters
* Suspicious URL patterns
* Domain structure

⚙️ How It Works

User enters URL
       ↓
URL Preprocessing
       ↓
Feature Extraction
       ↓
Rule-Based Analysis
       ↓
Risk Score Calculation
       ↓
URL Classification
       ↓
Display Result
       ↓
Store Analysis in SQLite

📊 Classification

The system evaluates the detected indicators and assigns a risk score.
* Safe – No significant suspicious characteristics detected.
* Suspicious – Some potentially risky characteristics detected.
* Phishing – Multiple or significant phishing indicators detected.
> The classification is based on predefined rules and should be treated as an indication rather than a definitive determination of whether a website is malicious.

🗄️ Database

The project uses SQLite to maintain a history of URL analyses.
The database stores:

* URL
* Risk score
* Classification result
* Date and time of analysis

📁 Project Structure

phishing-detection/
│
├── app.py
├── init_db.py
├── database.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

✅ Advantages
* Fast URL analysis
* Simple rule-based implementation
* No machine-learning training required
* Lightweight and resource-efficient
* Easy to understand and maintain
* SQLite database support
* User-friendly web interface

⚠️ Limitations
* Rule-based detection may not identify all sophisticated phishing URLs.
* New phishing patterns may require additional rules.
* The system does not replace professional security or threat-intelligence services.
* Classification depends on the features and rules implemented in the application.

🔮 Future Enhancements
* Integration of machine learning algorithms
* Real-time threat intelligence APIs
* Browser extension for live URL checking
* Advanced domain and SSL analysis
* Webpage content analysis
* Cloud deployment
* Mobile application
* Continuous updating of detection rules

👩‍💻 Author
Rifana Fathima A 
