<div align="center">

## Simple Data Pipeline  
#### Retrieve and Process Dow Jones (DJI) Data Using Prefect v3.0

</div>

---

#### I. Overview
This project demonstrates how to build a simple data pipeline to retrieve the Dow Jones Industrial Average (^DJI) historical data from Yahoo Finance using the yfinance library. The data is processed and saved to a .parquet file using the polars library. The primary goal is to showcase the simplicity and efficiency of using Prefect v3.0 as an orchestration tool for developing data pipelines.

---

#### II. Pipeline Flow
1. **Task 1: Fetch Data**
Retrieve historical data for **Dow Jones** (^DJI) using yfinance and convert it to a Polars DataFrame.

2. **Task 2: Process Data**
Perform basic transformations like filtering, renaming columns, and setting date formats using polars.

3. **Task 3: Save Data**
Save the cleaned and processed data to a .parquet file.

4. **Prefect Orchestration**
Each step of the pipeline is orchestrated using Prefect
<div align="center">
  <img src="./documents/Check Server UI.png" alt="Prefect Logo" height="400"/>
</div>

---

#### III.Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/NolanMM/Perfect_v3.0_Data_Engineering_Pipeline.git
    cd Perfect_v3.0_Data_Engineering_Pipeline
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv

    // Linux
    source venv/bin/activate 

    // Window
    cd ./venv/Scripts
    activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
---

#### IV. Usage

**1. Activate the Virtual Environment**
Open a separate terminal and activate the Python virtual environment:
```bash
# On Linux: source venv/bin/activate  
# On Windows: venv\Scripts\activate
```

**2. Start Prefect Server**
In the same terminal, start the Prefect server to enable orchestration and monitoring:
```bash
prefect server start
```
<div align="center">
  <img src="./documents/Run Server.png" alt="Prefect Logo" height="200"/>
</div>

This will launch the Prefect server locally. By default:
- The server UI is accessible at http://127.0.0.1:4200/dashboard
- Keep this terminal running during the execution of the pipeline.

**3. Run the Pipeline**
Open a new terminal, navigate to the project directory, activate the virtual environment,
```bash
# On Linux: source venv/bin/activate  
# On Windows: venv\Scripts\activate
```
and execute the pipeline:
```bash
$env:PREFECT_API_URL="http://127.0.0.1:4200/api"; python Simple_Data_Pipeline.py
```

<div align="center">
  <img src="./documents/Run Pipeline.png" alt="Prefect Logo" height="200"/>
</div>

**4. Monitor Pipeline Execution**
Visit the Prefect server UI in your browser (http://127.0.0.1:4200/dashboard) to monitor task execution, inspect logs, and troubleshoot any issues.

---

#### V.Features
1. **Data Retrieval**: Fetch historical data for ^DJI using yfinance.
2. **Data Processing**: Perform basic data cleaning and processing using polars.
3. **Data Storage**: Save the processed data to a .parquet file.
4. **Orchestration**: Use Prefect v3.0 to orchestrate the data pipeline.

---

#### VI. Requirements
- Python 3.8+
- Libraries:
    - yfinance
    - polars
    - prefect (v3.0 or higher)
