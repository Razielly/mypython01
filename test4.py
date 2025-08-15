# 1 print lai bab me lai type in ()
# have 4 way 
# st way 
print('Nantasak',2547,'Wednesday',18.08)
# , = 1 spacebar

# nd way +str() จะไม่มีspace หรือบวกspaceเอง ก็เพิ่ม ' ' เอง
print('kkoo'+str(4568987),(54654),'love'+str(3000))

# rd way MethodFormat format()  โดยแสดงข้อมูลในรูปของ string
# (ข้อมูลที่ไม่ใช่สตริงให้ใส่ใน () ของ format และโชว์แทนที่ตำแหน่งของ {} )
# หมายเลขใน {} คือ index number           0   1  2
print('hello {2} Wow {1}KOoK{0}'.format(5555,0,True))

# th way f-string โดยข้อมูลที่แสดงในรูปแบบสตริง
#  (ข้อมูลที่ไมใช่ String ให้เขียนใส่ใน{} ณ ตำแหน่งนะ้นๆเลย)
print(f'hello {2} Wow {1}  KOoK {True}')