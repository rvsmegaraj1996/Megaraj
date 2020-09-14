#control statement
'''
#if
#elif
#elif
#elif
.
.
.
.
#else:
'''

condenser=input('tell us type of condenser:')
board_year=int(input('how many years of warrenty:'))
if board_year<=3:
    print('voltage offered one/two ton acc')
elif board_year==1 and condenser=='copper':
    print('samsung offered one ton ac')
elif board_year==2 and consdenser=='aluminium':
    print('carrier offered two ton years')
elif board_year==2 and consdenser=='copper':
    print('tfd offered two ton ac')
else:
  print('no ac available for ur requirement')
