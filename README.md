# ImageC doc


## Deploy build docker image

docker build --target live -t joda001/imagec-doc:live .
docker build --target build -t joda001/imagec-doc:v2.0.0 .
docker push  joda001/imagec-doc:v2.0.0



```.htaccess
RewriteEngine On

# If the request doesn't point to an actual file or directory
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# Append .html to the requested path
RewriteRule ^docs/stable/commands/(.*)$ /docs/stable/commands/$1.html [L]
```