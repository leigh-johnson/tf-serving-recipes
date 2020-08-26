import grpc
import tensorflow as tf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc


tf.compat.v1.app.flags.DEFINE_string('server', 'localhost:8500',
                                     'PredictionService host:port')
FLAGS = tf.compat.v1.app.flags.FLAGS

def main():
  channel = grpc.insecure_channel(FLAGS.server)
  stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
  request = predict_pb2.PredictRequest()
  request.model_spec.name = 'universal-sentence-encoder'
  request.model_spec.signature_name = 'serving_default'

  test_string = '''
    You must understand the whole of life, not just one little part of it. That is why you must read, that is why you must look at the skies, that is why you must sing, and dance, and write poems, and suffer, and understand, for all that is life.
  '''
  request.inputs['inputs'].CopyFrom(
      tf.make_tensor_proto(test_string, shape=[1]))
  result = stub.Predict(request, 10)  # 10 secs timeout
  print(result)

if __name__ == '__main__':
    main()