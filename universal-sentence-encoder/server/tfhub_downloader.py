import hashlib
import tensorflow_hub; 

model_uri = "https://tfhub.dev/google/universal-sentence-encoder/4"
tensorflow_hub.load(model_uri)
sha = hashlib.sha1(model_uri.encode("utf8")).hexdigest()
print(sha)