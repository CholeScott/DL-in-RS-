import tensorflow as tf
import traffic_inference
import traffic_train
import numpy as np


#每十秒加载一次最新的模型，并在测试数据集上测试最新模型的正确率
def test_sample(image):

    image_data=tf.gfile.FastGFile(image,'rb').read()
    decode_image=tf.image.decode_png(image_data,3)
    
    decode_image = tf.image.convert_image_dtype(decode_image, tf.float32)

    image = tf.reshape(decode_image, (1, 28, 28, 3))    
    
    
    test_logit=traffic_inference.inference(image,train=False,regularizer=None)    
    probabilities = tf.nn.softmax(test_logit)    
    correct_prediction = tf.argmax(test_logit, 1)    
    saver = tf.train.Saver()
    
    with tf.Session() as sess:
        #tf.train.get_checkpoint_state函数会通过checkpoint文件自动找到目录中最新的文件
        
        ckpt = tf.train.get_checkpoint_state(traffic_train.MODEL_SAVE_PATH)
        
        if ckpt and ckpt.model_checkpoint_path:
            # 加载模型
            saver.restore(sess, ckpt.model_checkpoint_path)
            # 通过文件名得到迭代的轮数。
            print("加载模型成功：" + ckpt.model_checkpoint_path)
            
            global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
            
            
            
            probabilities, label = sess.run([probabilities, correct_prediction])
            probability = probabilities[0][label]
 
            print("After %s training step(s),validation label = %d, has %g probability" % (global_step, label, probability))

        else:
            print('失败!')
        

def  main(argv=None):
    test_sample('D:/tf/3.png')


if __name__=='__main__':
    #main()
    tf.reset_default_graph()
    tf.app.run()
