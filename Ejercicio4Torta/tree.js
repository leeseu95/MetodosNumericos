// Use: var tree = new OST(); tree.select(4); tree.insert(key,value)
var OST = function () {
  // Order statistic tree node
  var Node = function (leftChild, key, value, rightChild, parent) {
    return {
      leftChild: (typeof leftChild === "undefined") ? null : 
      leftChild,
      key: (typeof key === "undefined") ? null : key,
      value: (typeof value === "undefined") ? null : value,
      rightChild: (typeof rightChild === "undefined") ? null : 
      rightChild,
      parent: (typeof parent === "undefined") ? null : parent,
      size: (typeof size  === "undefined") ? 0 : size,
    };
  },
  /*
  * Private Class: Node
  *
  * A OST node constructor
  *
  * Parameters:
  *        leftChild - a reference to the left child of the node.
  *        key - The key of the node.
  *        value - the value of the node.
  *        rightChild - a reference to the right child of the node.
  *        parent - a reference to the parent of the node.
  *        size - size of subtree rooted at the node.
  *
  * Note: All parameters default to null.
  */
  
  /*
   * Private Variable: root
   *
   * The root node of the BST.
   */
  root = new Node(),

  /*
   * Private Method: searchNode
   *
   * Search through a binary tree.
   *
   * Parameters:
   *     node - the node to search on.
   *     key - the key to search for (as an integer).
   *
   * Returns:
   *     the value of the found node,
   *     or null if no node was found.
   *
   */
  searchNode = function (node, key) {
    if (node.key === null) {
      return null; // key not found
    }

    var nodeKey = parseInt(node.key, 10);

    if (key < nodeKey) {
      return searchNode(node.leftChild, key);
    } else if (key > nodeKey) {
      return searchNode(node.rightChild, key);
    } 
    else { // key is equal to node key
        return node;
    }
  },

  deleteNode = function(key, current) {
    childCount = (current.leftChild !== null ? 1 : 0) + (current.rightChild !== null ? 1 : 0);
    var parent = current.parent;

    if (current === root){
      switch(childCount){
        case 0:
          root = null;
          break;

        case 1:
          root = (current.rightChild === null ? current.leftChild : current.rightChild);
          break;

        case 2:
          //new root will be the old root's leftChild child
          //...maybe
          var replacement = root.leftChild;

          //find the rightChild-most leaf node to be 
          //the real new root
          while (replacement.rightChild !== null){
            var replacementParent = replacement;
            replacement = replacement.rightChild;
          }

          //it's not the first node on the leftChild
          if (replacementParent !== null){

            //remove the new root from it's 
            //previous position
            replacementParent.rightChild = replacement.leftChild;

            //give the new root all of the old 
            //root's children
            replacement.rightChild = root.rightChild;
            replacement.leftChild = root.leftChild;
          } 
          else {

            //just assign the children
            replacement.rightChild = root.rightChild;
          }

          //officially assign new root
          root = replacement;
      }        

    //non-root values
    } 
    else {
      switch (childCount){
        case 0:
          //if the current key is less than its 
          //parent's, null out the leftChild pointer
          if (current.key < parent.key){
            parent.leftChild = null;
            //if the current key is greater than its
            //parent's, null out the rightChild pointer
          } 
          else {
            parent.rightChild = null;
          }
          break;

        //one child, just reassign to parent
        case 1:
          //if the current key is less than its 
          //parent's, reset the leftChild pointer
          if (current.key < parent.key){
            parent.leftChild = (current.leftChild === null ? 
            current.rightChild : current.leftChild);

            //if the current key is greater than its 
            //parent's, reset the rightChild pointer
          } 
          else {
            parent.rightChild = (current.leftChild === null ? 
            current.rightChild : current.leftChild);
          }
          break;    
        //two children, a bit more complicated
        case 2:

          //reset pointers for new traversal
          var replacement = current.leftChild;
          var replacementParent = current;

          //find the rightChild-most node
          while(replacement.rightChild !== null){
            replacementParent = replacement;
            replacement = replacement.rightChild;
          }

          replacementParent.rightChild = replacement.leftChild;

          //assign children to the replacement
          replacement.rightChild = current.rightChild;
          replacement.leftChild = current.leftChild;

          //place the replacement in the rightChild spot
          if (current.key < parent.key){
            parent.leftChild = replacement;
          } else {
            parent.rightChild = replacement;
          }          

          //no default
      }
    }
  },

  /*
   * Private Method: insertNode
   *
   * Insert into a binary tree.
   *
   * Parameters:
   *     node - the node to search on.
   *     key - the key to insert (as an integer).
   *     value - the value to associate with the key (any type of 
   *             object).
   *
   * Returns:
   *     true.
   *
   */
   insertNode = function (node, key, value, parent) {
    if (node.key === null) {
      node.leftChild = new Node();
      node.key = key;
      node.value = value;
      node.rightChild = new Node();
      node.parent = parent;
      node.size = 1;
      var recurseToRoot = node;
      while(recurseToRoot.parent != null){
        recurseToRoot.parent.size++;
        recurseToRoot = recurseToRoot.parent;
      }
      return true;
    }

    var nodeKey = parseInt(node.key, 10);

    if (key < nodeKey) {
      insertNode(node.leftChild, key, value, node);
    } 
    else if (key > nodeKey) {
      insertNode(node.rightChild, key, value, node);
    } 
    else { // key is equal to node key, update the value
      node.value = value;
      return true;
    }
  },

  /*
   * Private Method: traverseNode
   *
   * Call a function on each node of a binary tree.
   *
   * Parameters:
   *     node - the node to traverse.
   *     callback - the function to call on each node, this function 
   *                takes a key and a value as parameters.
   *
   * Returns:
   *     true.
   *
   */
  traverseNode = function (node, callback) {
    if (node.key !== null) {
      traverseNode(node.leftChild, callback);
      callback(node.key, node.value);
      traverseNode(node.rightChild, callback);
    }

    return true;
  },
  
  /*
   * Private Method: minNode
   *
   * Find the key of the node with the lowest key number.
   *
   * Parameters:
   *     node - the node to traverse.
   *
   * Returns: the key of the node with the lowest key number.
   *
   */
  minNode = function (node) {
    while (node.leftChild.key !== null) {
      node = node.leftChild;
    }

    return node;
  },

  /*
   * Private Method: maxNode
   *
   * Find the key of the node with the highest key number.
   *
   * Parameters:
   *     node - the node to traverse.
   *
   * Returns: the key of the node with the highest key number.
   *
   */
  maxNode = function (node) {
    while (node.rightChild.key !== null) {
      node = node.rightChild;
    }

    return node;
  },
  
  /*
   * Private Method: successorNode
   *
   * Find the key that successes the given node.
   *
   * Parameters:
   *		node - the node to find the successor for
   *
   * Returns: the node that successes the given node.
   *
   */
  successorNode = function (node) {
    var parent;

    if (node.rightChild.key !== null) {
      return minNode(node.rightChild);
    }

    parent = node.parent;
    while (parent.key !== null && node == parent.rightChild) {
      node = parent;
      parent = parent.parent;
    }

    return parent
  },
  /*
  * Private Method: selectNode
  *
  * find the i'th smallest element stored in the tree
  *
  * Parameters:
  *      node - initially root
  *      i - index
  *
  * Returns: find the i'th smallest element stored in the tree
  *
  */
  selectNode = function (i, node) {
    var l = node.leftChild.size
    if(i = l)
      return node
    else if(i < l)
      return select(i, node.leftChild)
    else
      return select(i - (l+1), node.rightChild)
  },
  /*
  * Private Method: rankNode
  *
  * find the rank of node x in the tree, i.e. its index in the sorted list of elements of the tree
  *
  * Parameters:
  *      x - Node
  *
  * Returns: the rank of x
  *
  */
  rankNode = function (x) {
    var l = x.leftChild.size + 1;
    var iter = x;
    var r = 1;
    while(iter != root){
      if(iter == iter.parent.rightChild)
        r = r + iter.parent.leftChild.size + 1;
      iter = iter.parent;
    }
    return r;
  },

  /*
   * Private Method: predecessorNode
   *
   * Find the key that preceeds the given node.
   *
   * Parameters:
   *		node - the node to find the predecessor for
   *
   * Returns: the node that preceeds the given node.
   *
   */
  predecessorNode = function (node) {
    var parent;

    if (node.leftChild.key !== null) {
      return maxNode(node.leftChild);
    }

    parent = node.parent;
    while (parent.key !== null && node == parent.leftChild) {
      node = parent;
      parent = parent.parent;
    }

    return parent;
  };
  
  return {
    /*
     * Method: search
     *
     * Search through a binary tree.
     *
     * Parameters:
     *     key - the key to search for.
     *
     * Returns:
     *     the node,
     *     or null if no node was found,
     *     or undefined if no key was specified.
     *
     */
    search: function (key) {
      var keyInt = parseInt(key, 10);

      if (isNaN(keyInt)) {
        return undefined; // key must be a number
      } 
      else {
        return searchNode(root, keyInt);
      }
    },
    /*
     * Method: select
     *
     * find the i'th smallest element stored in the tree
     *
     * Parameters:
     *     i - index
     * 
     *
     * Returns:
     *     the node,
     *     or undefined if i > size of tree
     *
     */
    select: function (i) {
      if(root.size < i)
        return undefined
      else
        return selectNode(i, root)
    },
    /*
     * Method: rank
     *
     * find the rank of element x in the tree, i.e. its index in the sorted list of elements of the tree
     * 
     *
     * Parameters:
     *     x - element
     * 
     *
     * Returns:
     *     rank of x (one-indexed!!!! i.e. 1,2,3...)
     *     or undefined if x is undefined
     *
     */
    rank: function (x) {
      return rankNode(x);
    },
    /*
     * Method: insert
     *
     * Insert into a binary tree.
     *
     * Parameters:
     *     key - the key to search for.
     *     value - the value to associate with the key (any type of 
     *             object).
     *
     * Returns:
     *     true,
     *     or undefined if no key was specified.
     *
     */
    insert: function (key, value) {
      var keyInt = parseInt(key, 10);

      if (isNaN(keyInt)) {
        return undefined; // key must be a number
      } 
      else {
        return insertNode(root, keyInt, value, null);
      }
    }, 
    /*
     * Method: delete
     *
     * Deletes Node x
     *
     * Parameters:
     *     x - the Node to delete (of type Node)
     *
     * Returns:
     *     true.
     *
     */
    delete: function (x) {
      return deleteNode(x.key,x);
    },   
    /*
     * Method: traverse
     *
     * Call a function on each node of a binary tree.
     *
     * Parameters:
     *     callback - the function to call on each node, this function 
     *                takes a key and a value as parameters. If no 
     *                callback is specified, print is called.
     *
     * Returns:
     *     true.
     *
     */
    traverse: function (callback) {
      if (typeof callback === "undefined") {
        callback = function (key, value) {
          print(key + ": " + value);
        };
      }

      return traverseNode(root, callback);
    },

    /*
     * Method: min
     *
     * Find the key of the node with the lowest key number.
     *
     * Parameters: none
     *
     * Returns: the node with the lowest key number.
     *
     */
    min: function () {
      return minNode(root);
    },

    /*
     * Method: max
     *
     * Find the key of the node with the highest key number.
     *
     * Parameters: none
     *
     * Returns: the node with the highest key number.
     *
     */
    max: function () {
      return maxNode(root);
    },
    // Returns the root node
    getRoot: function() {
      return root;
    },
    /*
     * Method: successor
     *
     * Find the key that successes the root node.
     *
     * Parameters: none
     *
     * Returns: the node that successes the root node.
     *
     */
    successor: function () {
      return successorNode(root);
    },
    /*
     * Method: predecessor
     *
     * Find the key that preceeds the root node.
     *
     * Parameters: none
     *
     * Returns: the node that preceeds the root node.
     *
     */
    predecessor: function () {
      return predecessorNode(root);
    }
  };
};