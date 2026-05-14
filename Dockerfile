FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .
RUN chmod +x wisecow.sh
ENV PATH="/usr/games:${PATH}"
EXPOSE 4499
CMD ["./wisecow.sh"]
