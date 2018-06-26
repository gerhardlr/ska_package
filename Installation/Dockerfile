FROM gerhardlr/tango_python:latest

USER root

#create workdir conating source code
RUN mkdir /home/ska_package

WORKDIR /home/ska_package

ENV HOME /home/ska_package

ADD .. /home/ska_package
RUN pip install -e .

RUN useradd --create-home --home-dir $HOME developer \
    && chown -R developer:developer $HOME

USER developer
