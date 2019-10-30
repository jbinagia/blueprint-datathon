# Understanding the Factors Influencing STD Prevalance
**NOTE: I am currently restructuring this repo to improve readability and ease of use. Please check back on 10/30/19**

In this repository is the data analysis our group performed for the [2019 Stanford Blueprint Datathon](https://blueprint-datathon.weebly.com/about.html), a weekend-long hackathon focusing on data science in healthcare. Although this was our first foray into the world of data science, our team placed amongst the top 4 teams for the competition. Our [final presentation](Datathon_Presentation.pdf) is attached for those interested. The [original case information](blueprint-case.pdf) is also included and it is highly recommended

Completed by Yiran Liu, Quenton Bubb, Sai Gourisankar, Jeremy Binagia.

## Installation and Usage
- Activate a virtual environment and install the required libraries, e.g.:
```shell
virtualenv -p python .env
source .env/bin/activate
pip install -r requirements.txt
```
- The Jupyter notebooks are organized as follows:
  - [violin_plots.ipynb](https://github.com/jbinagia/blueprint-datathon/blob/master/violin_plots.ipynb): used to create the [violin plots](https://en.wikipedia.org/wiki/Violin_plot?oldformat=true) found in slides 4 - 6 of our [final presentation](Datathon_Presentation.pdf).
  - [line_plots.ipynb](https://github.com/jbinagia/blueprint-datathon/blob/master/violin_plots.ipynb): used to create the figures shown in slides 7 and 8 of our [presentation](Datathon_Presentation.pdf).
  - [regression.ipynb](regression.ipynb) : used for the hypothesis testing described in slides 9 - 11 of the presentation.
