FROM python:3-slim

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# COPY . .

# CMD python script.py