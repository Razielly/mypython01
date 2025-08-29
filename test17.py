# คำนวณราคาสินค้าที่รับส่วนลดแล้ว โดยป้อนรหัสสินค้า ชื่อสินค้า ประเภทสินค้า มี4ประเภทคือ food, woman, man, kitchen (เป็นตัวย่อ) 
# F,f W,w M,m K,k
# และราคาสินค้า 
# จากนั้นคำนวณราคาสินค้าที่รับส่วนลดแล้วทางหน้าจอ by food 2% woamn 4% man 6% kitchen 10% ของราราสินค้า หากผ้อนใดๆผิด แสดงข้อความว่า คุณป้อนผิด

print('--------------------------------')
print('    โปรแกรมตรวจสอบราคาส่วนลด     ')
print('--------------------------------')
pd_id = input('ป้อนรหัสสินค้า : ')
pd_name = input('ป้อนชื่อสินค้า : ')
pd_type = input(''''ป้อนรหัสประเภทสินค้า  F,f/W,w/M,m/K,k 
    : ''')
pd_price = float(input("ป้อนราคาสินค้า : "))
print('--------------------------------')

if pd_type == 'F' or pd_type == 'f' :
    pd_prosale = pd_price - (pd_price * 2/100)
    print(f"ราคาสินค้ารวมส่วนลดแล้ว = {pd_prosale}")
elif pd_type == 'W' or pd_type == 'w' :
    pd_prosale = pd_price - (pd_price * 4/100)
    print(f"ราคาสินค้ารวมส่วนลดแล้ว = {pd_prosale}")
elif pd_type == 'M' or pd_type == 'm' :
    pd_prosale = pd_price - (pd_price * 6/100)
    print(f"ราคาสินค้ารวมส่วนลดแล้ว = {pd_prosale}")
elif pd_type == 'K' or pd_type == 'k' :
    pd_prosale = pd_price - (pd_price * 10/100)
    print(f"ราคาสินค้ารวมส่วนลดแล้ว = {pd_prosale}")
else :
    print('คุณใส่รหัสประเภทสินค้าผิด กรุณากรอกใหม่')