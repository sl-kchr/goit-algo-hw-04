
from pathlib import Path
path = Path('HW_4.txt')
path.write_text('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')
def total_salary(path):
    salary = []
    sum_salary = 0
    num_of_w = 0
    avarege_salary = 0
    
    path = Path(path)
    if path.exists():
        if path.stat().st_size == 0:
            print(f'Файл {path} порожній')
        else:
            read_path = path.read_text()
            line_path = read_path.splitlines()       
            for i in line_path:
                num_of_w += 1
                i = i.split(',')
                if len(i) > 1:
                    salary.append(i[1])
            for k in salary:
                sum_salary += int(k)
            avarege_salary = sum_salary/num_of_w
            all_reults = (sum_salary, int(avarege_salary))
            return all_reults
    else:
        print(f'На жаль, файл {path} не був знайдений')

total, average = total_salary('HW_4.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")