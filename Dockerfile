FROM mcr.microsoft.com/devcontainers/jekyll:0-bullseye as live

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN pip install -r requirements.txt -U

RUN apt-get update && apt-get install -y pandoc git


RUN cat Gemfile.lock | tail -n 2 | grep -C2 "BUNDLED WITH" | tail -n 1 | xargs gem install bundler -v
RUN bundle install

RUN rm -rf /usr/local/post-create.sh

RUN apt-get update && apt-get install -y librsvg2-bin texlive-xetex texlive-fonts-extra

FROM live as build

