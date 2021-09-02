Kodun amacı kullanıcı girişi ile ToDoApp yapıp oluşturduğumuz notları puanlamak.</br>
Notlar skor ve alfabaye göre sıralanabiliyor.</br>

Kullanmaya başlamadan önce 
```
pip install -r requirements.txt
```
komutunu giriniz.
Çalıştırdıktan sonra Kayıt olup giriş yapın. Şu anlık browser üzerinden not eklerken sorun yaşanıyor. O yüzden Api ile denenmeli. </br>
http://127.0.0.1:5000/sign-up --> Kayıt olmak için </br>
http://127.0.0.1:5000/login --> Giriş yapmak için </br>
Giriş yaptıktan sonra http://127.0.0.1:5000/ 'a  yönlendirileceksiniz. Burada not eklemek için POST metodu ile

```
{
    "note" : "Girmek istediğiniz not",
    "score" : Girmek istediğiniz skor
}
```
Şeklinde Api üzerinden request girin.</br>
Eğer oluşturduğunuz notu silmek istiyorsanız. Api üzerinden DELETE metodu ile http://127.0.0.1:5000/silmekistediğinizId'yi giriniz. Örneğin 7 numaralı id'yi silmek istiyorsunuz
http://127.0.0.1:5000/7 şeklinde çağırın.



