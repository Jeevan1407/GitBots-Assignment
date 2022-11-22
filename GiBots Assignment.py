#!/usr/bin/env python
# coding: utf-8

# In[41]:


def ohm_law(voltage=None,resistance=None,current=None):
    
   
    
    result = None
    lst = [voltage,resistance,current]
    
    if len([x for x in lst if x is None])>=2:
        return "Invalid"
    if len([x for x in lst if x is None])==0:
        return "Invalid"
    
    #print(len([x for x in lst if x is None]))
    
    
    if voltage is None:
        result = resistance * current
        
    if resistance is None:
        result = voltage / current
        
    if current is None:
        result = voltage / resistance
    
    result = round(result,2)
    
    if result.is_integer():
        result=int(result)
    
    #return round(result,2)
    return result

test_case_one = ohm_law(12, 220, None) 
test_case_two = ohm_law(230, None, 2) 
test_case_three = ohm_law(None, 220, 0.02) 
test_case_four = ohm_law(None, None, 10) 
test_case_five = ohm_law(500, 50, 10) 



print(test_case_one)
print(test_case_two)
print(test_case_three)
print(test_case_four)
print(test_case_five)

    


# In[ ]:





# In[ ]:





# In[ ]:




