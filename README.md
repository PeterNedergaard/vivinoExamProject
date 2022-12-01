### Project name:
Vivino multi-tool©℗®™
### Short description:
This project gets the data of almost 30.000 wines from vivino.com. With this data, it performs a variety of actions described further down. 
The idea was to use the wine data in combination with data preparation, transformation, and presentation to present interesting facts about wine

### List of used technologies:
  - Pandas
  - Numpy
  - Machine learning (Decision Tree Classifier, Linear regression)
  - Web scraping
  - Pickle
  - PySimpleGUI
  - RegEx (minor)
### Installation guide (if any libraries need to be installed):
#### To install the required libraries, this line should be run in the terminal:
  - pip install -r requirements.txt
#### These files should be run, since the data they generate are too large for github:
  - prepareData.py
  - flavorML.py
### User guide (how to run the program):
  - To run the program, simply run the main.py file
### Status (What has been done (and if anything: what was not done)):
  - Finds the correlation between the specifications of the wine, and the wines rating
  - Uses ML to predict the rating of a wine from its specifications
  - Presents a graph of the countries with the best average rating. Is France, stereotypically, in top 1?
  - Tells you which country is best suited for purchases of wine in a specified price range
  - Presents a graph of the most popular wines from a specified country
  - Uses ML to recommend a wine based on your favorite flavor-profiles (ex. chocolate, apple, raspberry or even wet concrete)
### List of Challenges you have set up for your self (The things in your project you want to highlight):
  - Machine learning
  - PySimpleGUI
  - Data preparation, transformation, presentation
  - Web scraping/api scraping
  - Our homemade Onehot-encoder (deprecated but still interesting)
