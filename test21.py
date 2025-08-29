#โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
#	กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
#   กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
#	กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
#	กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"
#	กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print('-----------------------------------')
print('   โปรแกรมแสดงข้อความต้อนรับนักศึกษา   ')
print('-----------------------------------')

std_name = input('ป้อนชื่อนักศึกษา : ')
std_yr = input('ป้อนชั้นปีที่ศึกษา : ')

if std_yr == "1" :
    print("Welcome Freshman")
elif std_yr == "2" :
    print("Welcome Sophomore")
elif std_yr == "3" :
    print("Welcome Junior")
elif std_yr == "4" :
    print("Welcome Senior")
else :
    print("Oh, no.... YOU ARE OUT")