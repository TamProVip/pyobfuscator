FROM ubuntu:22.04

# Cài đặt Python 3.9, 3.10, 3.11, 3.12
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update \
    && apt-get install -y \
        python3.9 \
        python3.9-venv \
        python3.9-dev \
        python3.10 \
        python3.10-venv \
        python3.10-dev \
        python3.11 \
        python3.11-venv \
        python3.11-dev \
        python3.12 \
        python3.12-venv \
        python3.12-dev \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.11 làm mặc định
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Cài thư viện cho tất cả các versions
RUN for v in 9 10 11 12; do \
        python3.$v -m pip install --upgrade pip; \
        python3.$v -m pip install flask flask-cors gunicorn pystyle; \
    done

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
