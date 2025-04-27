FROM sphinxdoc/sphinx AS live

RUN pip install readthedocs-sphinx-search==0.3.2
RUN pip install myst-parser==2.0.0
RUN pip install sphinx-rtd-theme==1.3.0
RUN pip install sphinx-design==0.5.0
RUN pip install sphinxcontrib-video==0.4.1

FROM live as build

RUN apt-get update && apt-get install -y git