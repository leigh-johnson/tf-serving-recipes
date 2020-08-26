# From Zero to Preoduction TensorFlow

The missing quick-start guide to deploying [TensorFlow Hub](https://www.tensorflow.org/hub) models with [TensorFlow serving](https://www.tensorflow.org/tfx/guide/serving). 

TensorFlow Serving is a reliable, no-hassle way to create production-ready gRPC/REST APIs for TensorFlow models. Notable TF Serving features include:

1. Canarying/experimentation between multiple model versions
2. Prediction micro-batching
3. Prometheus metrics
4. Platform-specific compiler optimizations ([list of supported instruction sets](https://www.tensorflow.org/tfx/serving/setup#optimized_build))

# Pre-requisites

* [Docker >= 19](https://www.docker.com/get-started)
* [Docker Compose >= 1.26](https://docs.docker.com/compose/install/)
* [NVIDIA Docker Runtime (required for GPU acceleration, not required for CPU-only inference)](https://github.com/NVIDIA/nvidia-docker)
* Python 3.6+ (for example clients)

# Example Models

## Universal Sentence Encoder (USE)

[https://tfhub.dev/google/universal-sentence-encoder/4](TFHub)

USE generates text embeddings for a given string, which is a high-dimensional representation of the text's content. Text embeddings can be used for semantic similarity/search, text classification, clustering, and other NLP tasks.

1. Start a prediction server
```bash
$ cd universal_sentence_encoder
$ docker-compose build
$ docker-compose up

```

2. Make predictions with example clients

```bash
$ cd universal_sentence_encoder
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r client/requirements.txt
$ python client/grpc_example.py
$ python client/rest_example.py
```

3. Example Output

```bash
$ python client/rest_example.py                                                 
{'outputs': [[-0.00179422169,
              -0.0747870058,
              0.0838590711,
              ...
```

```bash
$ python client/grpc_example.py 
outputs {
  key: "outputs"
  value {
    dtype: DT_FLOAT
    tensor_shape {
      dim {
        size: 1
      }
      dim {
        size: 512
      }
    }
    float_val: -0.0050949095748364925
    float_val: -0.070153146982193
    float_val: 0.08538997173309326
    ...
  }
}
model_spec {
  name: "universal-sentence-encoder"
  version {
    value: 4
  }
  signature_name: "serving_default"
}
```


## SSD MobileNet V2 FPNLite

[https://tfhub.dev/tensorflow/collections/object_detection/1](TFHub)

Single-shot object detection using a MobileNet backbone, quantized and converted to TFLite model for optimal performance on a CPU or specialized hardware delegate.

Coming Soon!

## ResNet (Feature Vector "Head")

[https://tfhub.dev/google/imagenet/resnet_v1_101/feature_vector/4](TFHub)

Coming soon! 
