# docker build -t gcsns/gc-pdf-util:0.0.4 .
# FROM python:3.10-alpine
FROM python:3.10

RUN apt-get update && \
    apt-get install -y libgl1 build-essential cmake git \
    libgtk-3-dev libboost-all-dev python3-dev \
    python3-pip python3-setuptools python3-wheel && \
    # libopenblas-dev liblapack-dev libx11-dev && \
    apt-get clean

RUN apt-get install -y wkhtmltopdf

RUN apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra && \
    rm -rf /var/lib/apt/lists/*

# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/cuda-keyring_1.1-1_all.deb
# RUN dpkg -i cuda-keyring_1.1-1_all.deb
# RUN apt-get update
# RUN apt-get install -y cudnn9-cuda-12

# RUN apt-get install -y software-properties-common
# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/debian12/x86_64/cuda-keyring_1.1-1_all.deb
# RUN dpkg -i cuda-keyring_1.1-1_all.deb
# RUN add-apt-repository contrib
# RUN apt-get update
# RUN apt-get -y install cuda-toolkit-12-4

ARG USER=gcsns
ARG GROUP=$USER
ARG UID=1001
ARG GID=$UID

#use non root user
RUN groupadd --gid $GID $GROUP
RUN useradd --uid $UID --gid $GID -m $USER

WORKDIR /app

RUN chown $USER:$GROUP ./

USER $USER

# Set EasyOCR to store its models and files in the .cache directory
ENV EASYOCR_MODULE_PATH=/home/$USER/.cache/EasyOCR

COPY --chown=$USER:$GROUP ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir uvicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=$USER:$GROUP ./src /app/src

RUN mkdir data

WORKDIR /app/src

CMD ["/home/gcsns/.local/bin/uvicorn", "app:app", "--host=0.0.0.0", "--port=9433"]
EXPOSE 9433