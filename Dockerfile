FROM ubuntu:jammy
COPY /rohc-2.3.1 /rohc/
WORKDIR /rohc

# Install build essentials like make
RUN apt update && apt install -y make
RUN ./configure --prefix=/usr
RUN make all
RUN make install

