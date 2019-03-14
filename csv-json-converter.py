import csv  
import json  
  

f = open( '/Users/kevindavis/Desktop/ProjectsFolder/Chaos_Search/ServiceNowLogs.csv')  

reader = csv.DictReader( f, fieldnames = ( "AlertID","Alias","TinyID" ))  

out = json.dumps( [ row for row in reader ] )  
print("Your JSON has been parsed!")

f = open( '/Users/kevindavis/Desktop/ProjectsFolder/Chaos_Search/serviceNowOut.json', "a")  
f.write(out)  

print("And now your JSON has been saved!  YEAH YEAH")  
f.close()
