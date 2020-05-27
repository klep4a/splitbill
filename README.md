# splitbill  
Приложение позволяетразделить счёт между несколькими друзьями.  
sudo apt install python3-pip  
sudo pip3 install virtualenv  
virtualenv djangoenv  
source djangoenv/bin/activate  
or, in windows: djangoenv\Scripts\activate  
git clone https://github.com/klep4a/splitbill  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  
### User Journey  
1. На главной странице предлагается ввести сумму счёта - Full bill и число на котрое нужно счёт разделить - Split num.  
2. Чтобы разделить счёт детально предлагается ссылка - Detail bill.  
3. Далее предлагается ввести имена друзей, для каждого можно ввести отдельные строчки счёта.  
4. По ссылке - Get final split bill выводится финальный результат сумм детальных счетов по именам друзей.  
---
Чтобы сохранить имена друзей приложение потребует авторизации.  
Авторизованный пользователь может просматривать сохранённые счета по ссылке - My Bills, свой профайл, изменить пароль по e-mail.  
