# ImageC doc


## Deploy build docker image

docker build --target live -t joda001/imagec-doc:live .
docker build --target build -t joda001/imagec-doc:v2.0.0 .
docker push  joda001/imagec-doc:v2.0.0