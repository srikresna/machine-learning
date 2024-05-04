import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from kerastuner.tuners import RandomSearch
import tensorflow as tf
import tensorflow_transform as tft 
from tensorflow.keras import layers
import os  
import tensorflow_hub as hub
from tfx.components.trainer.fn_args_utils import FnArgs

LABEL_KEY = "CATEGORY"
FEATURE_KEY = "MESSAGE"

def transformed_name(key):
    """Renaming transformed features"""
    return key + "_xf"
 
def gzip_reader_fn(filenames):
    """Loads compressed data"""
    return tf.data.TFRecordDataset(filenames, compression_type='GZIP')
 
 
def input_fn(file_pattern, 
             tf_transform_output,
             num_epochs,
             batch_size=64)->tf.data.Dataset:
    """Get post_tranform feature & create batches of data"""
    
    # Get post_transform feature spec
    transform_feature_spec = (
        tf_transform_output.transformed_feature_spec().copy())
    
    # create batches of data
    dataset = tf.data.experimental.make_batched_features_dataset(
        file_pattern=file_pattern,
        batch_size=batch_size,
        features=transform_feature_spec,
        reader=gzip_reader_fn,
        num_epochs=num_epochs,
        label_key = transformed_name(LABEL_KEY))
    return dataset

VOCAB_SIZE = 10000
SEQUENCE_LENGTH = 100

embedding_dim=16
def build_model(hp):
    model = Sequential([
        Embedding(input_dim=VOCAB_SIZE, output_dim=embedding_dim, input_length=SEQUENCE_LENGTH),
        LSTM(units=hp.Int('units', min_value=32, max_value=64, step=32)),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        loss='binary_crossentropy',
        optimizer=tf.keras.optimizers.Adam(
            hp.Choice('learning_rate', values=[1e-3, 1e-4])),
        metrics=['accuracy'])
    return model


 
vectorize_layer = layers.TextVectorization(
    standardize="lower_and_strip_punctuation",
    max_tokens=VOCAB_SIZE,
    output_mode='int',
    output_sequence_length=SEQUENCE_LENGTH)
    

def _get_serve_tf_examples_fn(model, tf_transform_output):
    
    model.tft_layer = tf_transform_output.transform_features_layer()
    
    @tf.function
    def serve_tf_examples_fn(serialized_tf_examples):
        
        feature_spec = tf_transform_output.raw_feature_spec()
        
        feature_spec.pop(LABEL_KEY)
        
        parsed_features = tf.io.parse_example(serialized_tf_examples, feature_spec)
        
        transformed_features = model.tft_layer(parsed_features)
        
        # get predictions using the transformed features
        return model(transformed_features)
        
    return serve_tf_examples_fn
    
def run_fn(fn_args: FnArgs) -> None:
    
    log_dir = os.path.join(os.path.dirname(fn_args.serving_model_dir), 'logs')
    
    # tensorboard_callback = tf.keras.callbacks.TensorBoard(
    #     log_dir = log_dir, update_freq='batch'
    # )
    
    # es = tf.keras.callbacks.EarlyStopping(monitor='val_binary_accuracy', mode='max', verbose=1, patience=10)
    # mc = tf.keras.callbacks.ModelCheckpoint(fn_args.serving_model_dir, monitor='val_binary_accuracy', mode='max', verbose=1, save_best_only=True)
    
    
    # Load the transform output
    tf_transform_output = tft.TFTransformOutput(fn_args.transform_graph_path)
    
    # Create batches of data
    train_set = input_fn(fn_args.train_files, tf_transform_output, 10)
    val_set = input_fn(fn_args.eval_files, tf_transform_output, 10)
    vectorize_layer.adapt(
        [j[0].numpy()[0] for j in [
            i[0][transformed_name(FEATURE_KEY)]
                for i in list(train_set)]])
    
    # Build the model
    model = build_model()
    
        # Hyperparameter tuning
    tuner = RandomSearch(
        build_model,
        objective='val_accuracy',
        max_trials=5, 
        executions_per_trial=3,  
        directory='my_dir',
        project_name='spam_classifier')

    tuner.search(x = train_set,
            validation_data = val_set,
                 epochs=20,
                 callbacks=[EarlyStopping(monitor='val_loss', patience=3)])

    # Get the best trained model
    best_model = tuner.get_best_models(num_models=1)[0]
    signatures = {
        'serving_default':
        _get_serve_tf_examples_fn(model, tf_transform_output).get_concrete_function(
                                    tf.TensorSpec(
                                    shape=[None],
                                    dtype=tf.string,
                                    name='examples'))
    }
    best_model.save(fn_args.serving_model_dir, save_format='tf', signatures=signatures)


    return best_model



    # model.fit(x = train_set,
    #         validation_data = val_set,
    #         callbacks = [tensorboard_callback, es, mc],
    #         steps_per_epoch = 1000, 
    #         validation_steps= 1000,
    #         epochs=10)
    # signatures = {
    #     'serving_default':
    #     _get_serve_tf_examples_fn(model, tf_transform_output).get_concrete_function(
    #                                 tf.TensorSpec(
    #                                 shape=[None],
    #                                 dtype=tf.string,
    #                                 name='examples'))
    # }
    # model.save(fn_args.serving_model_dir, save_format='tf', signatures=signatures)
