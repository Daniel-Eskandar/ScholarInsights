# This script generates a circular network graph connecting the professors.
# The width of an edge is determined by the number of publications they collaborated on.

library(canvasXpress)

#Load Data
nodes=read.table("../dat/ProfessorNodes.csv", header=TRUE, sep=",")
edges=read.table("../dat/ProfessorEdges.csv", header=TRUE, sep=",")

#Create circle network graph
canvasXpress(
  nodeData=nodes,
  edgeData=edges,
  #background="rgb(245,245,245)",
  graphType="Network",
  networkLayoutType="circular",
  sizeEdgeBy="Cooperations",
  nodeScaleFontFactor=20,
  showAnimation=TRUE,
  showLegend=FALSE,
  showNodeNameSizeThreshold=50,
  showNodeNameThreshold=200,
  sizeNodeBy="nodeEdges",
  edgeColor=rgb(0.5,0.5,0.5),
  nodeSizeScaleFactor= 0.8,
  nodeFontStyle = "bold"
)
