import json
import re

from konlpy.tag import Twitter
from collections import Counter

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser
from dataCrawling.matplotlibTest.ex02 import font_location

def showGraph(wordInfo):
    
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)
    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
