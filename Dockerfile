FROM ubuntu:latest
LABEL authors="danielvink"

ENTRYPOINT ["top", "-b"]