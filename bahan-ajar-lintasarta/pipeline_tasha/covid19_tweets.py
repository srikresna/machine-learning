import tensorflow as tf
LABEL_KEY = "label"
FEATURE_KEY = "text"
def transformed_name(key):
    """Renaming transformed features"""
    return key + "_xf"
def preprocessing_fn(inputs):
    """
    Preprocess input features into transformed features
    
    Args:
        inputs: map from feature keys to raw features.
    
    Return:
        outputs: map from feature keys to transformed features.    
    """
    
    outputs = {}
    
    # Convert 'sentimen' to a numeric tensor if it's not already a numeric tensor
    sentimen = tf.cast(inputs[FEATURE_KEY], tf.float32)
    
    # Apply tf.strings.as_string to each tensor in 'sentimen'
    sentimen_as_string = tf.map_fn(tf.strings.as_string, sentimen)
    
    outputs[transformed_name(FEATURE_KEY)] = sentimen_as_string
    
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    
    return outputs
