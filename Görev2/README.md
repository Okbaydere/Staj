Kodun amacı kullanıcı girişi ile ToDoApp yapıp oluşturduğumuz notları puanlamak.</br>
Notlar skor ve alfabaye göre sıralanabiliyor.</br>

Kullanmaya başlamadan önce 
```
pip install -r requirements.txt
```
komutunu giriniz.</br>
# Postman ile kullanmak için aşağıdaki adımları izleyin. </br>
`http://127.0.0.1:5000/sign-up` --> Kayıt olmak için GET ile bu url'ye gelin. Body x-www-form-urlencoded 'a girip Key yerine ` email,firstName,password` ve değerlerini girin </br>
`http://127.0.0.1:5000/login `--> Giriş yapmak için GET ile bu url'ye gelin. Body x-www-form-urlencoded 'a girip Key yerine  `email ve password` daha sonra da değerlerini girin </br>
Giriş yaptıktan sonra` http://127.0.0.1:5000/` 'a  yönlendirileceksiniz. Burada not eklemek için POST metodu ile parametre olarak KEY'e `note , score` daha sonra da değerleri girin.</br>
Eğer oluşturduğunuz notu silmek istiyorsanız. Api üzerinden DELETE metodu ile http://127.0.0.1:5000/delete/silmekistediğinizId'yi giriniz. Örneğin 7 numaralı id'yi silmek istiyorsunuz
`http://127.0.0.1:5000/delete/7` şeklinde çağırın. </br>
Eğer istediğiniz tabloyu değiştirmek isterseniz ise http://127.0.0.1:5000/edit/düzenlemekistediğinizId'yi giriniz.Post metoduyla parametre olarak updated_note,updated_score olarak istediğiniz değerleri giriniz
</br>
</br>
Koddaki login,logout ve sign up işlemleri **auth.py**'de </br>
Delete ve add task işlemleri **views.py**'de</br>
Bütün java kodları **base.html'**'de bulunmakta.



