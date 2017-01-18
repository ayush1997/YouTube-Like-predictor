



## data/
### get_IDS.py
The script uses Youtube Search API for extracting Video IDs for the last 7 years(2010-2016).It gives Approx. 22,000-24,000 Video IDs for every category and stores them in a different Pickle file.

### scrape_video.py
The script use the Video IDs saved by ` get_IDS.py` and further extract different attributes using Youtube API and saves the data dictionary in pickle format.

### scrape_channel.py
The script is used to further collect data for all channels present in the video dataset.

### scrape_social.py
The script is used to scrape social links

## notebook/
### FeatureEngineering.ipynb
The notebook has the implementation for creation new derived features.

### DataProcessing.ipynb
This notebook contains data processing implementation for data cleaning and encoding catgorical fetaures

## model/
### mdoel_grid.py
This script generates the tuned parameters for estimator using Grid Search and Cross Validation
 
