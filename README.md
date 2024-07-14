# imageC Doc

This contains the source for imageC's documentation, hosted at https://imagec-doc.readthedocs.io/en/latest/

## Building locally

1) Start in docker image `joda001/imagec-doc:v1.0.0`
2) Execute `make html`


### Deploy build docker image

docker build --target live -t joda001/imagec-doc:live .
docker build --target build -t joda001/imagec-doc:v1.0.0 .
docker push  joda001/imagec-doc:v1.0.0