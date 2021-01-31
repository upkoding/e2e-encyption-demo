# e2e-encyption-demo

Demo Enkripsi End-to-end dengan metode [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange) dengan Python. Demo ini hanyalah sebagai contoh dan bukan untuk digunakan di production.

Dimana teknik yang sama kemungkinan digunakan oleh Whatsapp atau Telegram dalam mengimplementasikan End-to-end encryption mereka, namun pastinya tidak sesederhana yang ini :)

![Image](https://raw.githubusercontent.com/upkoding/e2e-encyption-demo/main/demo.gif)

> Terlihat diatas dimana terminal kiri adalah user Alice, terminal tengah adalah log server dan yang paling kanan adalah user Bob. Dimana pesan yang dikirimkan oleh Alice dan Bob terenkripsi dan tidak dapat dibaca di server tanpa mengetahui Private Key yang masing masing hanya dimiliki oleh Alice dan Bob.

## Coba sendiri

1. Install dependencies

```
pip install simple-crypt
```

2. Jalankan server
```
python server.py
```

3. Jalankan client 1 dan 2 di terminal berbeda
```
python client.py Bambang
python client.py Jono
```

Demo ini adalah bahan penunjang untuk salah satu video di [Channel Youtube UpKoding](https://www.youtube.com/c/UpKoding/videos) mengenai **[Cara Kerja End-to-end encryption di Whatsapp/Telegram](https://youtu.be/jk3alKS0RFw)**.
