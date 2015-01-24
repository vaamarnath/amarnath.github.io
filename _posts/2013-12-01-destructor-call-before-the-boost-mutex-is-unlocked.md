---
title: Destructor call before the boost mutex is unlocked!
author: Amarnath
layout: post
permalink: /2013/12/destructor-call-before-the-boost-mutex-is-unlocked/
Layout:
  - 1c
categories:
  - C++
---
<p id="top" />
Trying to work on legacy code makes you go through the loads of messy code. And this is what I came across last week. On invocation of destructor of a class objects, the process was crashing giving the following error.
`<br />
Assertion failed: (!pthread_mutex_destroy(&m)), function ~mutex, file /usr/local/boost/include/boost/thread/pthread/mutex.hpp, line 47.<br />
`  
Let me try to simulate this with a sample snippet. See the following code,  


<pre class="brush: cpp">#include &lt;boost/thread/mutex.hpp&gt;

// class for demostrating
// Assertion failed: (!pthread_mutex_destroy(&m)),
// function ~mutex, file /usr/local/boost/include/boost/thread/pthread/mutex.hpp, line 47.

class lock_failure
{
public:
    // mutex for locking
    boost::mutex m_mutex;
    
    // empty constructor
    lock_failure()
    {
    }
    
    // empty destructor
    ~lock_failure()
    {
    }
};

int main()
{
    // get the class object
    lock_failure* l_ptr = new lock_failure;
    
    // lock the mutex before data manipulation
    // and processing
    boost::mutex::scoped_lock lock(l_ptr-&gt;m_mutex);
    
    // some processing
    
    // now try deleting before the lock
    // is released
    delete l_ptr;
    
}</pre></p> 

Try compiling the code and run it.`<br />
$clang++ lock.cpp -I <BOOST_INCLUDE_DIR><br />
$./a.out<br />
Assertion failed: (!pthread_mutex_destroy(&m)), function ~mutex, file /usr/local/boost/include/boost/thread/pthread/mutex.hpp, line 47.<br />
Abort trap: 6<br />
`
</p>

This is happening just because when the destructor is called, the object still holds the lock. To get rid of this, just go ahead and put the scoped lock and the data processing block into a scope (by using curly braces around the block).

PS: This code might work with out any issues on some platforms. I came across this on Mac OS X 10.8+.