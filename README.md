# InsightDataEngineering
Code Challenge for Insight Data Engineering - EDGAR Analytics

Approach:
- A class is defined to represent and update key information of an active user weblog session, which includes IP address, first request time, last request time and count of requests
- A growing array is built to store all active user sessions. Once a new line of request is read from the input file stream, system first 

Programming Language:
- Python 3
  
Dependency:
- "Datetime" package is needed
  
Input file:
- "../input/inactivity_period.txt"
- "../input/log.csv"
  
Output file:
- "sessionization.txt"

Run Instruction:
- Run the "run.sh" shell script which will execute the "/src/sessionization.py" code
