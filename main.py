
monthConversions = {
    "Jan": "January" ,
    "Feb": "February" ,
    "Mar": "March" ,
    "Apr": "April" ,
    "May": "May" ,
    "Jun": "June" ,
    "July": "July" ,
    "Aug": "August" ,
    "Sep": "September" ,
    "Oct": "October" ,
    "Nov": "November" ,
    "Dec": "December",
}

print(monthConversions.get("Jan"))
print(monthConversions.get("0" , "Not a Valid Key"))

