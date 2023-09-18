# from datetime import datetime
# dat = {}

# date_string = ['2023-06-02 17:37:21.761583+05:30','2023-06-05 17:37:21.761583+05:30','2023-06-02 17:37:21.761583+05:30','2023-06-02 17:37:21.761583+05:30']

# # date_string = '2023-06-02 17:37:21.761583+05:30'

# # date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f%z")
# print(date_string)

# # print(type(date_obj), date_obj.date())

# for i in date_string:
#     # print((i))
#     date_obj = datetime.strptime(i, "%Y-%m-%d %H:%M:%S.%f%z")
#     # print(type(date_obj))
#     if date_obj.date() in dat.keys():
#         dat[date_obj.date()] += 1
#     else:
#         dat[date_obj.date()] =1

# k = list(sorted(dat.keys()))
# print(k[-1])

import re


# Define regular expression patterns for the two timestamp formats
timestamp_pattern1 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2}"
timestamp_pattern2 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\+\d{2}:\d{2}"

# Input strings to check
date_string1 = "2023-05-02 00:00:00+05:30"
date_string2 = "2023-05-02 11:57:37.606373+05:30"

# Check if the input strings match either of the timestamp patterns
if re.match(timestamp_pattern1, date_string1) or re.match(timestamp_pattern2, date_string1):
    print("Input string 1 matches one of the timestamp formats.")
else:
    print("Input string 1 does not match any of the timestamp formats.")

if re.match(timestamp_pattern1, date_string2) or re.match(timestamp_pattern2, date_string2):
    print("Input string 2 matches one of the timestamp formats.")
else:
    print("Input string 2 does not match any of the timestamp formats.")
