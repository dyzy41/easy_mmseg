# easy_mmseg
everyone can use mmseg easiely.
1. 项目介绍  
mmsegmentation是一个非常好用的框架，但是代码很复杂，调试起来也很麻烦，不熟悉分割的同学可能用不好这个项目库，这对cv learner来说是个巨大的损失，因此我把mmsegmentation最关键的一些地方做了修改，方便大家快速上手使用   
2. 数据集使用方式  
mmsegmentation里面的数据集模式主要是采用了一些常用的经典数据集的存储形式，比如VOC，city，isprs之类的。但是如果我们自己有一个数据集需要训练，重新整理数据就很麻烦，因此我把数据接口给修改了，改成了如下的格式  
数据集导入方式就是三个文本文件，train.txt, val.txt, test.txt 里面的数据存储方式为：  
img_path1&ensp;lab_path1  
img_path2&ensp;lab_path2  
...  
（注意这里中间是有两个空格）  
这样做的好处就是，不管多乱七八糟的数据集，只要写一个代码生成这样的文件就可以开始训练了。我在tools/write_names.py里提供了一种写法。  

3. 训练  
python tools/train.py config_path  
config_path 这个就是配置文件，只需要给一个参数就行，就是配置文件路径，后面的就是可选参数，大家自己研究。  

4. 测试  
如果需要单独测试生成可视化结果  
python tools/test.py config_path checkpoint_path  
config_path这个就是配置文件 checkpoint_path是训练好的pth模型的路径。  

5. 项目注意事项  
5.1 配置文件  
   如果按照我的方式去训练，可以参考这个配置文件 configs/psanet/psanet_r50-d8_4xb4-20k_txt-512x512.py 主要的变化就是这里 base = [ '../base/models/psanet_r50-d8.py', '../base/datasets/txt.py', '../base/default_runtime.py', '../base/schedules/schedule_20k.py' ] 这个txt.py就是我们使用的数据参数，通过这个参数来调用数据接口函数。 打开这个'../base/datasets/txt.py'文件 这个文件里面，主要需要注意的就是data_root参数 以及train_dataloader, val_dataloader, test_dataloader的ann_file参数即可。 代码里读取三个txt的正确路径为： data_root+ann_file

5.2 目前主要是适用于二分类 目前整个代码主要是适用于二分类，因为我用二分类数据做的测试，我后续改一下，也适配多分类。 也就是目前这个项目，只要是二分类的数据都可以无脑训练。 另外需要注意的是mask必须为0-255的二值灰度图。不然会训练不出来结果。
