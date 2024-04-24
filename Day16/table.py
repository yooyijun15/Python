from prettytable import PrettyTable

# 테이블 생성
my_table = PrettyTable()
# 컬럼 및 데이터 추가
my_table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
my_table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
# 좌측 정렬
my_table.align = "l"
# 우측 정렬
my_table.align = "r"
# 테이블 출력
print(my_table)
