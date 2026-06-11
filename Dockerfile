FROM python:3.11-slim

# Cài đặt Docker (để chạy Docker-in-Docker - không khuyến khích trên Render)
# Hoặc cài nhiều Python versions
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y \
    python3.9 \
    python3.10 \
    python3.11 \
    python3.12 \
    && rm -rf /var/lib/apt/lists/*

# Tạo symlink cho các Python versions
RUN ln -s /usr/bin/python3.9 /usr/local/bin/python3.9 && \
    ln -s /usr/bin/python3.10 /usr/local/bin/python3.10 && \
    ln -s /usr/bin/python3.11 /usr/local/bin/python3.11 && \
    ln -s /usr/bin/python3.12 /usr/local/bin/python3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cài đặt pystyle cho từng Python version
RUN python3.9 -m pip install pystyle && \
    python3.10 -m pip install pystyle && \
    python3.11 -m pip install pystyle && \
    python3.12 -m pip install pystyle

EXPOSE 5000

CMD ["gunicorn", "app:app"]
