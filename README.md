Mining Little Sis for NSA connections
=====================================

Looks at 2 levels of relationships on Little Sis and outputs the results as
a gexf file....

setup
-----

create a virtualenv 

```
pip install -r requirements.txt
```

Add your little-sis API key to api-key.txt

```
echo MYKEY > api-key.txt
```

run with

```
python lsnetwork.py
```

Examine network.gexf

adapting
--------

There are two parameters to be adjusted: the starting entity id and the
depth... edit them at the top of the script to perform different searches.


