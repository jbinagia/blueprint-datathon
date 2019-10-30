# Understanding the Factors Influencing STD Prevalance
**NOTE: I am currently restructuring this repo to improve readability and ease of use. Please check back on 10/30/19**

In this repository is the data analysis our group performed for the [2019 Stanford Blueprint Datathon](https://blueprint-datathon.weebly.com/about.html), a weekend-long hackathon focusing on data science in healthcare. Although this was our first foray into the world of data science, our team placed amongst the top 4 teams for the competition. Our [final presentation](Datathon_Presentation.pdf) is attached for those interested. 

Completed by Yiran Liu, Quenton Bubb, Sai Gourisankar, Jeremy Binagia.

## Background
> Over the last decade, STD rates have steadily been on the rise, with over 2 million new infections reported each year. In the United States alone, the developing STD epidemic has totaled over $16 billion of medical expenses annually, with younger demographics representing the majority of cases. Students in high school and college acquire 50% of new STDs. The Center for Disease Control and Prevention has reported an all-time high in STD cases in 2017, despite recent research suggesting an average decrease in sexual activity across the US. Rates of Gonorrhea diagnoses have increased by nearly 67% over the past few years, with little to no signs of stopping. Syphilis and Chlamydia have shown similarly steep increases in overall diagnoses rates. In some cases, STDs can develop into more serious, lethal infections. Though many of these infections can be cured with antibiotics, many still go undiagnosed and/or untreated. The resulting adverse health effects include ectopic pregnancies, increased HIV risk, and stillbirth. Other serious concerns include the rise of antibiotic resistant STDs, some of which have been shown to resist almost all classes of antibiotics.


More details can be found on the [official website](https://blueprint-datathon.weebly.com/the-case.html) for the datathon. 

## Installation and Usage
- Activate a virtual environment and install the required libraries, e.g.:
```shell
virtualenv -p python .env
source .env/bin/activate
pip install -r requirements.txt
```
- The Jupyter notebooks are organized as follows:
  - [violin_plots.ipynb](https://github.com/jbinagia/blueprint-datathon/blob/master/violin_plots.ipynb): used to create the [violin plots](https://en.wikipedia.org/wiki/Violin_plot?oldformat=true) found in slides 4 - 6 of our [final presentation](Datathon_Presentation.pdf).
  - [line_plots.ipynb](https://github.com/jbinagia/blueprint-datathon/blob/master/violin_plots.ipynb): used to create the line plots shown in slides 7 and 8 of our [presentation](Datathon_Presentation.pdf).
  - [regression.ipynb](regression.ipynb) : used for the hypothesis testing described in slides 9 - 11 of the [presentation](Datathon_Presentation.pdf).
