# Pseudo code
#
# NN module
#
# Camera module will instantiate a NN module.
# Camera then will pass an image to the instantiated class.
# Ie:
# NN = new NNModule()
#
# while(true):
#     img = getImage()
#     NN.anaylyze(img)
#     wait 1 second


# class outline
# class NNModule:
#     def __init__(self):
#       Initialize the NN, set up any variables
#
#
#     def analyze(img):
#       Input:  img=opencv2.imread() formatted image
#       Output:
#       This runs the analysis code from example
#       This method will determine what object(s) are present in an image.
#       Once anaylsis is complete, output data
#
#
#     def drawbox_on_found_object(img, object_data):
#       This class will export the data
#
#     def img_out(img, highlighting):
#       Outputs the image, will draw a box around the found target if highlighting is true
#
#     def output(data):
#       This method will output statistical data as needed to the next stage
import tensorflow as tf


def __init__():
    # Initialize the NN, set up any variables
    print "Constructor called"
    # Unpersists graph from file
    with tf.gfile.FastGFile("/tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    # Loads label file, strips off carriage return
    global label_lines
    label_lines = [line.rstrip() for line in tf.gfile.GFile("/tf_files/retrained_labels.txt")]


def analyze_image(image_path):
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
    return analyze(image_data)


def analyze(image_data):
    global label_lines
    print "Analyze called"
    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            return '%s (score = %.5f)' % (human_string, score)


def draw_box_on_found_objects(img, object_data):
    print "TODO:Draw a box on img!"


def img_out(img, highlighting):
    if highlighting:
        print "TODO:Highlighting disabled"
    else:
        print "TODO:Highlighting enabled"


def output(data):
    print "TODO:This is where output data will occur"