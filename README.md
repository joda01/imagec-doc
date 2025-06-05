# ImageC doc


## Deploy build docker image

docker build --target live -t joda001/imagec-doc:live .
docker build --target build -t joda001/imagec-doc:v2.0.0 .
docker push  joda001/imagec-doc:v2.0.0



## Apache2 config

```.htaccess
RewriteEngine On

# If the requested resource is NOT a real file...
RewriteCond %{REQUEST_FILENAME} !-f
# ...and NOT a real directory...
RewriteCond %{REQUEST_FILENAME} !-d
# ...then rewrite by adding ".html" to the requested URL path
RewriteRule ^(.*)$ $1.html [L]
```

Add to
/etc/apache2/sites-available/000-default.conf
```
    <Directory /var/www/html>
        AllowOverride All
        Require all granted
    </Directory>
```