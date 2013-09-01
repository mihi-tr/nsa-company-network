import littlesis
import networkx

startentity=17683

def getother(r,e):
  return r.entity1 if r.entity1!=e else r.entity2

def nadd(g,n):
  if (n.id not in g.nodes()):
    g.add_node(n.id,type=n.primary_type, name=n.name, label=n.name)

def dograph(g,e,n=0):
  print e.name
  nadd(g,e)
  r=e.related
  if n:
    for o in r:
      dograph(g,o,n-1)
  for o in r:
    nadd(g,o)
    g.add_edge(e.id,o.id)

f=open("api-key.txt")
ak=f.read()
f.close()

ls=littlesis.LittleSis(ak)
se=ls.entity(startentity)

g=networkx.Graph()
dograph(g,se,1)

networkx.write_gexf(g,"network.gexf")
