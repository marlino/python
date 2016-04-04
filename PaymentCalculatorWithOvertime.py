Hours = raw_input('Enter Hours:\n')
Rate = raw_input('Enter Rate:\n')
Hours = float(Hours)
Rate = float(Rate)
if Hours <= 40.00 :
   Pay = Hours * Rate
else:
   OT = Hours - 40
   P1 = 40 * Rate
   P2 = OT * 1.5 * Rate
   Pay = P1 + P2
print Pay
