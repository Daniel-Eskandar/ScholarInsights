library(canvasXpress)

#load data
nodes=read.table("../data/nodes.csv", header=TRUE, sep=",")
edges=read.table("../data/edges.csv", header=TRUE, sep=",")
groups =read.table("../data/groups.txt", header=TRUE, sep=";", quote="", fill=TRUE, check.names=FALSE, stringsAsFactors=FALSE)

#create network with groups
canvasXpress(
  nodeData=nodes,
  edgeData=edges,
  groupData=groups,
  colorNodeBy="Research.Field",
  sizeEdgeBy="Paper.Cooperations",
  graphType="Network",
  networkColaAvoidOverlaps=TRUE,
  networkLayoutType="cola",
  nodeScaleFontFactor=0.5,
  edgeColor=rgb(0.5,0.5,0.5),
  networkColaStartUnconstrainedIterations=1000,
  networkColaJaccardLinkLengthDefault=0.7,
  networkColaJaccardLinkLengths=40
)

#create circle network
canvasXpress(
  nodeData=nodes,
  edgeData=edges,
  background="rgb(245,245,245)",
  colorNodeBy="Research.Field",
  graphType="Network",
  networkLayoutType="circular",
  sizeEdgeBy="Paper.Cooperations",
  nodeScaleFontFactor=10,
  showAnimation=TRUE,
  showLegend=TRUE,
  showSizeEdgeLegend=FALSE,
  showSizeNodeLegend=FALSE,
  showColorNodeLegend=TRUE,
  showNodeNameSizeThreshold=25,
  showNodeNameThreshold=100,
  sizeNodeBy="nodeEdges",
  #title="Professor Cooperation",
  edgeColor=rgb(0.5,0.5,0.5),
  nodeSizeScaleFactor= 0.5
)