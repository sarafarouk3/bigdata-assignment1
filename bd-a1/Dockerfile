FROM ubuntu:22.04

RUN apt-get update && apt-get -y install python3 build-essential python3-pip

WORKDIR /home/doc-bd-a1

COPY . .

RUN pip install --no-input -r requirements.txt && \
    rm -rf ~/.cache/pip

CMD ["/bin/bash"]
