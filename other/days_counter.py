from datetime import date

from PySide2.QtWidgets import QMessageBox, QApplication

otp_date = date(2021, 6, 18)
cur_date = date.today()

zp_date = date(cur_date.year, cur_date.month, 16)
if cur_date.day < 16:
    if date(cur_date.year, cur_date.month, 16).weekday() not in [5, 6]:
        zp_date = date(cur_date.year, cur_date.month, 16)
    elif date(cur_date.year, cur_date.month, 16).weekday() == 5:
        zp_date = date(cur_date.year, cur_date.month, 18)
    elif date(cur_date.year, cur_date.month, 16).weekday() == 6:
        zp_date = date(cur_date.year, cur_date.month, 17)
else:
    if date(cur_date.year, cur_date.month + 1, 16).weekday() not in [5, 6]:
        zp_date = date(cur_date.year, cur_date.month + 1, 16)
    elif date(cur_date.year, cur_date.month + 1, 16).weekday() == 5:
        zp_date = date(cur_date.year, cur_date.month + 1, 18)
    elif date(cur_date.year, cur_date.month + 1, 16).weekday() == 6:
        zp_date = date(cur_date.year, cur_date.month + 1, 17)

days_zp = (zp_date - cur_date).days
days_otp = (otp_date - cur_date).days
msg = f'До зарплаты осталось {days_zp} дн.\nДо отпуска осталось {days_otp} дн.'

app = QApplication([])
msgBox = QMessageBox(QMessageBox.Warning, "Самая важная часть работы", msg, QMessageBox.NoButton)
msgBox.exec_()
