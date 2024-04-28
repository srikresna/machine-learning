
import tensorflow as tf
from collections import namedtuple
from keras_tuner.engine import base_tuner
from keras_tuner.tuners import Hyperband
from typing import Dict,Text,Any
frm tfx.components.trainer.fn_args_utils import FnArgs

TunerFnResult = namedtuple('TunerFnResult', [('tuner', base_tuner.BaseTuner),
                                             ('fit_kwargs', Dict[Text, Any])])


FEATURE_KEY='SentimentText'

def model_builder(hp):
  hp_nodes=hp.Int('units',min_value=64,max_value=256,step=64)
  hp_learning_rate=hp.Choice('learning_rate',values=[1e-2,1e-3,1e-4])
  hp_vocab=hp.Int('input_dim',values=[x for x in range(1000,10001,1000)])

  embedding_dim=16

  inputs = tf.keras.Input(shape=(1,), name=transformed_name(FEATURE_KEY), dtype=tf.string)
  reshaped_narrative = tf.reshape(inputs, [-1])
  x = vectorize_layer(reshaped_narrative)
  x = layers.Embedding(hp_vocab, embedding_dim, name="embedding")(x)
  x = layers.GlobalAveragePooling1D()(x)
  x = layers.Dense(hp_nodes, activation='relu')(x)
  x = layers.Dense(32, activation="relu")(x)
  outputs = layers.Dense(1, activation='sigmoid')(x)

  model = tf.keras.Model(inputs=inputs, outputs = outputs)

  model.compile(
      loss = 'binary_crossentropy',
      optimizer=tf.keras.optimizers.Adam(hp_learning_rate),
      metrics=[tf.keras.metrics.BinaryAccuracy()])

  return model

def tuner_fn(fn_args: FnArgs) -> TunerFnResult:
  tf_transform_output = tft.TFTransformOutput(fn_args.transform_output)

  train_dataset = input_fn(fn_args.train_files, fn_args.data_accessor, tf_transform_output)
  eval_dataset = input_fn(fn_args.eval_files, fn_args.data_accessor, tf_transform_output)

  tuner=Hyperband(model_builder,
                  objective='val_accuracy',
                  max_epochs=10,
                  directory=fn_args.working_dir,
                  project_name='sentimentanalyzer_tuner')

  return TunerFnResult(tuner=tuner,fit_kwargs={'x':train_dataset,'validation_data':val_dataset})
