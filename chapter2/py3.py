#!/usr/bin/env python
# Strings

single_quoted_string = 'data science'
double_quoted_string = "data science"

# special characters
tab_string = "\t"
print len(tab_string) # 1

# Use _raw_ string to denote the string that contain "\" and "t"
not_tab_string = r"\t"
print len(not_tab_string) # 2
