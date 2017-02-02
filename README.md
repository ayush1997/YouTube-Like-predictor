## YouTube Like Count Predictor

This a tool for getting youtube video like count prediction.A Random Forest model was used for training on a large dataset of ~3,50,000 videos.Feature engineering,Data cleaning, Data selection and many other techniques were used for this task.

## Report

`Report.pdf` contains a detailed explanation of different steps and techniques that were used for this task.

## Tools Used

* python 2.7
* Pandas
* Sklearn
* NumPy
* [visualize_ML](https://github.com/ayush1997/visualize_ML)

## How to run :

1. **Clone this repo**

      ```sh
      $ git clone https://gitlab.com/ayush1997/PS17_Ayush_Singh.git
      $ cd PS17_Ayush_Singh
      ```
2. **Create new virtual environment**

      ```sh
      $ sudo pip install virtualenv
      $ virtualenv venv
      $ source venv/bin/activate
      $ pip install -r requirements.txt
       ```
3. **Predictions**

    There are two ways for getting the prediction results.

    3.1. **Training the model and run prediction**

    ```sh
    $ cd model
    $ python train_model.py
    ```

    This will save a `model-final` file in the same folder,Training takes **~18 Mins**.Then run

    ```sh
    $ python predict.py <list of video ids>
    ```
    for ex: ``` $ python predict.py dOyJqGtP-wU ASO_zypdnsQ wEduiMyl0ko```

    3.2 **From pretrained model**

    A pretrained model has been uploaded on dropbox.Download model(~500MB) from the [link](https://www.dropbox.com/s/yv2jv55nz81fs5j/model-final.zip?dl=0).

     Unzip the `model-final` file in the `model` folder.
    ```sh
    $ cd model
    $ python predict.py <list of video ids>
    ```
    for ex: ``` $ python predict.py vid1 vid2 vid3] ```

**Note:** List can contain a maximum of **40** Video IDs at the time of run.      


## Code Details

Below is a brief description for the Code files/folder in repo.

## data/

This folder contains scripts which were used to fetch data using **Youtube API** and populatin the base.

```sh
$ cd data
```

### get_IDS.py

The script uses Youtube Search API for extracting **Video IDs** for the last **7 years(2010-2016)**.It gives Approx. **22,000-24,000** Video IDs for every category and stores them in a Pickle files for different categories.

```sh
$ python predict.py <list of video ids>
```
### scrape_video.py
The script use the Video IDs saved by ` get_IDS.py` and further extract different video related attributes using Youtube API and saves the data Dictionary in pickle format.

```sh
$ python scrape_video.py
```

### scrape_channel.py
The script is used to further collect data for all channels present in the video dataset.It makes use of the data stored for videos to extract channelIds.

```sh
$ python scrape_channel.py
```

### scrape_social.py
The script is used to scrape social links

```sh
$ python scrape_social.py
```
**Note** : Due to large amount of data to be extracted for different attributes,the extraction was done at different levels therefore it was not viable to make a single script for data collection which could make debugging a little messy.

## notebook/
This folder contains ipython notebooks which contain implementation for merging different data extracted and tasks like Data cleaning and processing.

```sh
$ jupyter notebook
```

### FeatureEngineering.ipynb
The notebook has the implementation for making new derived features.

### DataProcessing.ipynb
This notebook contains data processing implementation for data cleaning and encoding processes.


**Note** : The final *data* generated after all processing has been uploaded in `dataset/data.csv`. `dataset/data_final.csv` has the data which is used for training the model.

## model/

This folders contains scripts used for training,tuning model and getting the prediction results.
### model_grid.py
This script generates the tuned parameters for estimator using **Grid Search** and **Cross Validation**.

```sh
$ python model_grid.py
```

### train_model.py
This script is used for training the model over training data ( `dataset/data_final.csv` )
Because of **Bootstrap Sampling** in random forest the results migght vary after every trainig process.
```sh
$ python train_model.py
```

### predict.py
This script returns the **Like count** prediction along with the **difference** and the **Error rate**
```sh
$ cd model
$ python predict.py <list of video ids>
```
for ex: ``` $ python predict.py [vid1,vid2,vid3] ```

### Issues
A very common [issue](http://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations) comes with the pickling process which sometime leads to loss of information and different results every time. 

## Report
##
![1](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/1.png)
![2](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/2.png)
![3](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/3.png)
![4](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/4.png)
![5](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/5.png)
![6](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/6.png)
![7](https://github.com/ayush1997/YouTube-Like-predictor/blob/master/images/7.png)
