# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. 
# - Input: - Total seconds = 3672 
# - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
def convert(time):
        hours=time//3600
        remaining=time%3600
        Minutes=remaining//60
        final_rem=remaining%60
        print("hour:",hours,"Minutes:",Minutes,"Seconds:",final_rem)
convert(3672)