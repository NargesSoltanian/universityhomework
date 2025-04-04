Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> score = float(input("نمره دانشجو را وارد کنید (بین ۰ تا ۱۰۰): "))
...     
...     if score < 0 or score > 100:
...         print("لطفاً نمره‌ای بین ۰ تا ۱۰۰ وارد کنید.")
...     elif score > 90:
...         print("عالی")
...     elif score > 70:
...         print("خوب")
...     elif score > 50:
...         print("متوسط")
...     else:
...         print("مردود")
...         
... except ValueError:
