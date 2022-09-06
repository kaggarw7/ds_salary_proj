# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:52:09 2022

@author: karti
"""

import glassdoor_scraper as gs
import pandas as pd

path = "E:/Fall Classes 2022/Data Science Project/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)
