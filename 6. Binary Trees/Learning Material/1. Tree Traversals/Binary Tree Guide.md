# Binary Tree Guide
## Traversals
  * bfs
  * dfs
    * pre order
    * in order
    * post order
## Questions to Ask:
  * need to traverse tree?
    * bfs: node looking for closer to root rather than leaf nodes (bc bfs travels one by one level)
    * dfs: node looking for closer to leaf nodes rather than root (bc follows all the children nodes)
      * do we care about diff traversals? care about order in which value is visited?
        * pre order: value, left, right
        * in order: left, value, right
        * post order: left, right, value
