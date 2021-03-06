ARG TFSERVING_IMAGE="tensorflow/serving:2.3.0"
FROM $TFSERVING_IMAGE


ARG GRPC_PORT=8500
ARG REST_PORT=8501
ARG MODEL_SHA=063d866c06683311b44b4992fd46003be952409c
ARG MODEL_NAME=universal-sentence-encoder
ARG MODEL_VERSION=4
ARG MODEL_URI=https://tfhub.dev/google/universal-sentence-encoder/4
ARG TFHUB_CACHE_DIR=/opt/models
ARG TFSERVING_DIR=/opt/serving

ENV GRPC_PORT ${GRPC_PORT}
ENV REST_PORT ${REST_PORT}
ENV MODEL_SHA ${MODEL_SHA}
ENV MODEL_NAME=universal-sentence-encoder
ENV MODEL_URI ${MODEL_URI}
ENV MODEL_VERSION ${MODEL_VERSION}
ENV TFHUB_CACHE_DIR ${TFHUB_CACHE_DIR}
ENV TFSERVING_DIR ${TFSERVING_DIR}

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip

RUN pip3 install --upgrade setuptools pip wheel

ADD requirements.txt ${TFSERVING_DIR}/requirements.txt
ADD tfhub_downloader.py ${TFSERVING_DIR}/tfhub_downloader.py

# Cache TFHub model in a Docker image layer
# This increases image size, but also increases the reliability of your service - you don't want to pass a TFHub outage on to your customers. 
RUN pip3 install -r  ${TFSERVING_DIR}/requirements.txt
RUN python3 ${TFSERVING_DIR}/tfhub_downloader.py
RUN mkdir -p ${TFHUB_CACHE_DIR}/${MODEL_NAME}/${MODEL_VERSION}
RUN mv ${TFHUB_CACHE_DIR}/${MODEL_SHA}/* ${TFHUB_CACHE_DIR}/${MODEL_NAME}/${MODEL_VERSION}
ADD model.config ${TFSERVING_DIR}/model.config
ADD metrics.config ${TFSERVING_DIR}/metrics.config
ADD batch.config ${TFSERVING_DIR}/batch.config

EXPOSE ${GRPC_PORT}
EXPOSE ${REST_PORT}

# override entrypoint and use shell format so variables are expanded
# https://docs.docker.com/engine/reference/builder/#entrypoint
# https://github.com/moby/moby/issues/5509
ENTRYPOINT tensorflow_model_server \
    --port=${GRPC_PORT} \
    --rest_api_port=${REST_PORT} \
    --model_config_file=${TFSERVING_DIR}/model.config \
    --monitoring_config_file=${TFSERVING_DIR}/metrics.config \
    --batching_parameters_file=${TFSERVING_DIR}/batch.config --enable_batching