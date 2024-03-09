<h2>Hello! I am instructing you about this project.</h3>
<p>-DJANGO</p>
<p>-DjangoRestFramework</p>
<p>-REDIS</p>
<p>-WEBSOCKETS</p>
<h3>Description and capabilities: </h3>
<p>This application is a video hosting where users can publish various videos, with the ability to comment, add to the favorites tab, edit their profile, and online anonymous chat using WebSockets technology</p>
<br>
<p>Also, in this project I added an API section.
Through POSTMAN you can receive database objects.
Of course, I added my access rights there.
Get a token and perform operations to create/delete/update objects.</p> 
<hr>
<h3>Installation</h3>
<p>1)Download, then drag and drop the myproject directory into your project</h4>
<p>2)Mark this directory 'as sourses root'</p>
<hr>

```bash
cd myproject
```

```bash
pip install -r requirements.txt
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash
python manage.py loaddata users/fixtures/users.json
```
```bash
python manage.py loaddata myapp/fixtures/tags.json
```
```bash
python manage.py loaddata myapp/fixtures/products.json
```
*Make sure redis is working correctly and play with it
```bash
redis-cli ping
```
A little about online anonymous chat:
Monitor the operation of the websocket by watching the console. When connecting to the room, the corresponding command HANDSHAKING and then CONNECT will be displayed. If you leave the room, the connection is immediately interrupted, and you will see the corresponding DISCONNECT response in the console.

```bash
python manage.py runserver
```
<hr>
<p>This project was developed by me personally! </p>
<hr>
<p>If you have questions or suggestions, please contact me through my email <b>nazik3110@gmail.com</b></p>
