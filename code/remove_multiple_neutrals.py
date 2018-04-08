import os
import glob

def remove_neutrals():
    neutralImages = sorted(glob.glob("/home/tushaar/Desktop/code.fun.do/database/emotions/neutral/*"))
    
    previous_sessionID = ""
    for neutralImage in neutralImages:
        current_sessionID = neutralImage[60:64]
        
        if current_sessionID == previous_sessionID:
            print "Removing <%s>" %neutralImage
            os.remove(neutralImage)
        previous_sessionID = current_sessionID
