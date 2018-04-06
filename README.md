# InsightDataEngineering
Code Challenge for Insight Data Engineering - EDGAR Analytics

Approach:
- A class is defined to represent and update key information of an active user weblog session, which includes IP address, first request time, last request time and count of requests
- A realtime array is built to store all active user sessions. Once time proceeds in a new line of input, system checks if any active session becomes inactive based on the provided threshold. If so then this session is removed from the array and printed to the output file. 
- If the IP address of the new input line matches any active session, then update the last request time as well as the count of request for that session. If the IP address of the new input line does not match any active session, then create a new sesson to the end of the array with information from the new input line.
- Repeat the above process until the end of the input file. Then print all remaining active sessions in the array in chronological order.

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
