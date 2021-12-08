#!/usr/bin/env python
# coding: utf-8

# **v-model:
# V model is a verification and validation model used in a software development life cycle where each level of development life-cycle is verified before moving to the next level.
# 
# **pros:
# High success rate,Easy to manage,Effective for small projects,Specific deliverables,Step-by-step process,Defects tracking
# 
# **cons:
# Rigid and Inflexible, Not suitable for complex projects, No prototypes required,No precision, The risk in meeting customer expectations
# 

# **steps to write clean code:
#     1. Function and Variable naming.
#     2. Constant variables.
#     3. Documentation strings (docstrings)
#     4. Type hints
#     5. Method pointers
#     
#    https://www.youtube.com/watch?v=iMM2IlvpwZM
# 

# In[1]:


# bad code #
x = 5000
y = 3 

def calc(a, b):
    return(1 + a/ 100)*b 


# In[2]:


# code after cleaning #
salary = 5000
per_raise = 3 # if this is constant variable it can be written full capital

def calc_raise(salary, per_raise):
    """ calculates thr raise and returns new salary.
            
            parameters:
                salary(int): the original salary
                per_raise(int): the percent salary raised by
            returns: f(float): new salary. 
    
    """
    return (1 + per_raise/ 100)* salary


# **List of DevOps Tools:
# 
# 1. Version Control tools: GitHub, Bitbucket, GitLab
# 
# 2. Container Management tools: Docker, Kubernetes, Mesos
# 
# 3. Application Performance Monitoring tools: Prometheus, Dynatrace, AppDynamics
# 
# 4. Deployment & Server Monitoring tools: Splunk, Datadog, Sensu
# 
# 5. Configuration Management tools: Chef, puppet, Ansible
# 
# 6. CI / Deployment Automation tools: Bamboo, Jenkins, IBM UrbanCode
# 
# 7. Test Automation tools: Test.ai, Ranorex, Selenium
# 
# 8. Artifact Management tools: Sonatype NEXUS, JFRog Artifactory, CloudRepo
# 
# 9. Codeless Test Automation tools: AccelQ, Appvance, Testim.io
# 
# 

# ** dataops & MLops:
# should be used on top of eachother, after automating data with dataops it becomes easy to automate ML models
# 
# https://www.youtube.com/watch?v=W7P43i6cT2s

# In[ ]:




