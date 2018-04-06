# Source Python Code of Insight Data Engineering Code Challenge 2018 - by Jingnan Zhao
# Read input data stream from SEC EDGAR weblog to record user sessions of document requests in chronological order
# Input1: log.csv (comma separated with header line)
# Input2: inactivity_period.txt (single integer)
# Output: sessionization.txt (comma separated without header line)


# Import datetime package
from datetime import datetime

# Define session as a class to represent a user session
class session():
  def __init__(self,ip,startdatetime,enddatetime):
    self.ip = ip # IP address of a user
    self.startdatetime = startdatetime  # Start datetime of the session
    self.enddatetime = enddatetime  # End datetime of the session
    self.request = 1  # Count of file requests during the session, initialized as 1 at beginning of session

  # If user requests a new file within an active session, the enddatetime will be updated to reflect current datetime
  def update_time(self, enddatetime):
    self.enddatetime = enddatetime

  # If user requests a new file within an active session, the request counter will increase by 1
  def new_request(self):
    self.request = self.request + 1

# Main function
def main():

  # Read from "inactivity_period.txt" to obtain the time period threshold for inactivity
  prepfile = open("../input/inactivity_period.txt","r")
  if prepfile.mode == 'r': # Check to make sure that the file was opened
    lapse = int(prepfile.read()) # lapse is an integer to indicate number of inactive seconds before a user session terminates
  prepfile.close()

  # Open the input weblog file
  with open("../input/log.csv", "r") as inputfile:

    # Create a new output file
    with open("../output/sessionization.txt", "w") as outputfile:

      # Session_Array is the array to store all active sessions, initialized as blank
      Session_Array = []
      # Timestamp is a time stamp used to check if time from current input line proceeds from last input line, initialized as 1900/1/1
      # If the answer is no, then no inactivity check is needed at this moment
      timestamp = datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")

      for line in inputfile: # Read the input file line by line
        currentline = line.split(",") # Read content of each line as comma separated fields
        if currentline[0] != "ip":  # Skip the first line of the input file which includes header information
          now_ip = currentline[0]   # IP address of current line
          now_date = datetime.strptime(currentline[1], "%Y-%m-%d").date()  # Date of current line
          now_time = datetime.strptime(currentline[2], "%H:%M:%S").time()  # Time of current line
          now_datetime = datetime.combine(now_date,now_time) # Combine date and time into a datetime variable


          # When current line's time proceeds from last line, check if any session in the Session_Array has been inactive for more than lapse seconds
          # If so print this session to the output file and remove the session from the array
          if now_datetime > timestamp:
            temp = [] 
            for i in Session_Array:
              time_diff = (now_datetime - i.enddatetime).seconds  # Time difference between current time and the last request time in the session
              if time_diff > lapse:  # If inactivity longer than threshold, than this session is terminated
                str_start = i.startdatetime.strftime("%Y-%m-%d %H:%M:%S") # Convert session start datetime into string
                str_end = i.enddatetime.strftime("%Y-%m-%d %H:%M:%S")  # Convert session end datetime into string
                duration = (i.enddatetime - i.startdatetime).seconds+1  # Calculate session duration in seconds (inclusive)
                # Print the session information to the output file
                outputfile.write(str(i.ip) + "," + str_start + "," + str_end + "," + str(duration) + "," + str(i.request) + "\n")
              else:
                temp.append(i)  # temp is temporarily used to store all the non-terminated sessions
            Session_Array = temp[:] # Redefine the Session_Array by copying from temp, effectively removing the terminated sessions
            del temp[:] # Delete the temporary array to save space
            timestamp = now_datetime # Update time stamp


          # Add information from current line into the array of non-terminated sessions at current datetime
          tag = 0  # tag is a local flag to check if any user session in the array has same IP as current line
          # If IP of current line belongs to an existing user session in the array, then update the enddatetime and the request count
          for i in Session_Array:
            if now_ip == i.ip:
              i.new_request()
              i.update_time(now_datetime)
              tag = 1
          # If not then this is a new user session, append this session to the bottom of the array
          if tag == 0:
            Session_Array.append(session(now_ip,now_datetime,now_datetime))

      # When stream from the input file is complete, print the remaining active sessions in the array to the output file
      for i in Session_Array:
        str_start = i.startdatetime.strftime("%Y-%m-%d %H:%M:%S")
        str_end = i.enddatetime.strftime("%Y-%m-%d %H:%M:%S")
        duration = (i.enddatetime - i.startdatetime).seconds+1
        outputfile.write(str(i.ip) + "," + str_start + "," + str_end + "," + str(duration) + "," + str(i.request) + "\n")

if __name__ == "__main__":
  main()
