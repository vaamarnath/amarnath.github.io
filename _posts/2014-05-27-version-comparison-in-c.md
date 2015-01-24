---
title: Version comparison in C++
author: Amarnath
layout: post
permalink: /2014/05/version-comparison-in-c/
categories:
  - C++
---
<p id="top" />
This is a utility function to compare two version strings in C++. The function works for any digit verisoning system. The function returns 0 when versions are same and 1 when 1st parameter is greater than 2nd and -1 on the other case.</p> 

Make sure that you have boost to use this function. This function makes use of boost/algorithm/string.hpp for splitting the version string based on &#8216;.&#8217; delimiter.
</p>

<pre class="brush: cpp">//C++ code to compare two version strings.
//For example, input can be 1.0.2.241 and 1.0.3.
//The method returns 0 when the versions are equal,
//1 when param1 &gt; param2 and -1 when param1 &lt; param2.

//@brief: Version compare
//
//@return: 0, 1, -1
int versionCheck(std::string param1, std::string param2)
{
    
    if (param1.empty() || param2.empty())
    {
        //throw exception
    }
    
    // If both version strings are same.
    // Return 0.
    if (param1.compare(param2) == 0)
    {
        return 0;
    }
    
    std::vector&lt;std::string&gt; param1_vtr;
    std::vector&lt;std::string&gt; param2_vtr;
    
    boost::split(param1_vtr, param1, boost::is_any_of("."));
    boost::split(param2_vtr, param2, boost::is_any_of("."));
    
    if (param1_vtr.size() &gt; param2_vtr.size())
    {
        // Fill the smaller vector with 0s
        while (param1_vtr.size() != param2_vtr.size())
        {
            param2_vtr.push_back("0");
        }
    }
    else
    {
        // Fill the smaller vector with 0s
        while (param1_vtr.size() != param2_vtr.size())
        {
            param1_vtr.push_back("0");
        }
    }
    
    size_t loop_value = param1_vtr.size();
    
    size_t i = 0;
    int retVal = 0;
    while (loop_value)
    {
        int param1_v = atoi(param1_vtr[i].c_str());
        int param2_v = atoi(param2_vtr[i].c_str());
        loop_value--;
        i++;

        if (param1_v == param2_v)
        {
            continue;
        }
        else if (param1_v &lt; param2_v)
        {
            retVal = -1;
            break;
        }
        else
        {
            retVal = 1;
            break;            
        }
    
    }
    return retVal;
}</pre>