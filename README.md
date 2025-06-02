# Healthcare Data ETL Pipeline

## 📋 Project Description
This project implements an ETL (Extract, Transform, Load) pipeline for healthcare data using Python, MongoDB, and Docker. The pipeline processes patient data from CSV files and loads it into a MongoDB database for analysis.

## 🏗️ Architecture
- **MongoDB**: NoSQL database for storing patient data
- **Mongo Express**: Web-based MongoDB admin interface
- **Python**: ETL script with data cleaning and transformation
- **Docker**: Containerized environment for reproducible deployment

## 📂 Project Structure
```
├── docker-compose.yml         # Docker services configuration
├── .env                      # Environment variables
├── README.md                 # Project documentation
├── data/                     # Input CSV files
│   └── healthcare_dataset-20250506.csv
├── src/                      # Source code
│   └── etl_script.py         # ETL pipeline script
├── analysis.ipynb           # Data analysis notebook
├── logs/                    # ETL execution logs
└── results.pdf             # Analysis results and queries
```

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose
- Python 3.11+ (for running the notebook locally)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd healthcare-etl
```

### 2. Start the services
```bash
docker-compose up
```

This will:
- Start MongoDB on port 27017
- Start Mongo Express on port 8081
- Run the ETL script automatically
- Process the CSV data and load it into MongoDB

### 3. Access the data
- **Mongo Express**: http://localhost:8081
  - Username: admin
  - Password: admin

### 4. Run the analysis
```bash
jupyter notebook analysis.ipynb
```

## 🔧 ETL Process

### Extract
- Reads CSV files from the `/data` directory
- Handles files with semicolon (`;`) separators

### Transform
- **Name cleaning**: Standardizes capitalization (`"bobby JacksOn"` → `"Bobby Jackson"`)
- **Date formatting**: Converts DD/MM/YYYY to proper datetime objects
- **Data validation**: Ensures data integrity before insertion

### Load
- Bulk insertion into MongoDB using `insert_many()`
- Preserves original column names for simplicity
- Logs all operations for monitoring

## 📊 Database Schema
The MongoDB collection `patients` contains documents with the following structure:
```json
{
  "Name": "John Doe",
  "Age": 45,
  "Gender": "Male",
  "Medical Condition": "Diabetes",
  "Date of Admission": "2023-05-15T00:00:00.000Z",
  "Discharge Date": "2023-05-20T00:00:00.000Z",
  "Medication": "Metformin",
  ...
}
```

## 🧪 Analysis Queries
The project includes analysis for:
1. Total patient count
2. Patients admitted after January 1, 2023
3. Demographics analysis (age > 50, specific names)
4. Medical condition distribution
5. Medication frequency analysis
6. Specific medication usage (e.g., Lipitor)

## 📝 Configuration

### Environment Variables (.env)
```
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin
MONGO_INITDB_DATABASE=healthcare_db
ME_CONFIG_MONGODB_ADMINUSERNAME=admin
ME_CONFIG_MONGODB_ADMINPASSWORD=admin
ME_CONFIG_MONGODB_SERVER=mongo
ME_CONFIG_BASICAUTH_USERNAME=admin
ME_CONFIG_BASICAUTH_PASSWORD=admin
```

## 🔍 Monitoring
- ETL logs are written to `/logs/etl.log`
- Real-time monitoring via Docker logs: `docker-compose logs -f python`

## 🛠️ Troubleshooting

### Common Issues
1. **Connection refused**: Ensure MongoDB container is running
2. **CSV not found**: Check that files are in the `/data` directory
3. **Permission errors**: Verify Docker has access to project directories

### Useful Commands
```bash
# View logs
docker-compose logs python

# Restart services
docker-compose restart

# Clean up
docker-compose down
```


