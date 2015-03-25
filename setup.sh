#!/bin/bash

mv ./attributesfile ./.gitattributes
git config --local core.attributesfile ./.gitattributes
git config --local filter.dropoutput_ipynb.clean ./ipynb_output_filter.py
git config --local filter.dropoutput_ipynb.smudge cat