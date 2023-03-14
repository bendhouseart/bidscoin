FROM python:3.10-slim AS builder

# Make a dcm2niix build from the latest stable source code
RUN apt-get update && apt-get -y install git build-essential cmake; \
    git clone https://github.com/rordenlab/dcm2niix.git; \
    cd dcm2niix; mkdir build && cd build; \
    cmake -DZLIB_IMPLEMENTATION=Cloudflare -DUSE_JPEGLS=ON -DUSE_OPENJPEG=ON ..; \
    make install

# Or install the latest dcm2niix release from the base repository (= typically outdated)
# RUN apt-get update && apt-get -y install dcm2niix

FROM python:3.10-slim

# Install the dcm2niix build
COPY --from=builder /usr/local/bin/dcm2niix /usr/local/bin/dcm2niix

# First install pyqt6 as Debian package to solve dependencies issues occurring when installed with pip
# Then install the latest stable BIDScoin release from Python repository
ENV PIP_NO_CACHE_DIR=off
RUN apt-get update && apt-get -y --no-install-recommends install pigz curl python3-pyqt6 python3-pyqt6.qtx11extras && apt-get clean; \
    pip install --upgrade pip; \
    pip install bidscoin[all]
