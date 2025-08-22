# input 
Name =  input('Enter name: ')
year_born =  input('YYYY: ')

# Variable คือชื่อที่เดฟตั้งขึ้นมาเองเอาไว้เก็บข้อมูล หรือการกำหนดตัวแปร
# 

print('--------------')
print(f'Hi {Name} your BY is {year_born}')
print(f'Your old is {2025 -int(year_born)}')
print('--------------')
# ใช้ ,
print('Hi',Name,'your BY is',year_born)
print('Your old is',(2025 - int(year_born)))
print('--------------')



# ใช้ +
print('Hi'+' '+Name +' '+'your'+' '+"BY"+" "+'is'+' '+year_born)
print('Your'+' '+'old'+' '+'is'+' '+str(2025 - int(year_born)))
print('--------------')



# ใช้ format
print('Hi {} your BY is {}'.format(Name,year_born))
print('Your old is {}'.format(2025 - int(year_born)))
print('--------------')
