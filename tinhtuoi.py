from datetime import date

# Nhập ngày sinh
dob = input("Nhập ngày sinh của bạn (YYYY-MM-DD): ")

# Lấy ngày hiện tại
today = date.today()

# Tính tuổi
age = today.year - dob.year

# In ra tuổi
print("Tuổi của bạn là:", age)
