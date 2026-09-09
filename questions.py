# ============================================================
# AI COGNITIVE LEARNING MAP - QUESTION BANK
# VERSION 2.0
# ============================================================

QUESTIONS = [

    # ========================================================
    # ARRAYS
    # ========================================================

    {
        "id": 1,
        "concept": "Arrays",
        "question": "Which data structure stores elements in contiguous memory?",
        "options": [
            "Linked List",
            "Array",
            "Tree",
            "Graph"
        ],
        "answer": "Array",
        "difficulty": "Easy",
        "prerequisite": None,
        "explanation": "Arrays store elements in contiguous memory locations."
    },

    {
        "id": 2,
        "concept": "Arrays",
        "question": "What is the typical time complexity of accessing an element by index in an array?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],
        "answer": "O(1)",
        "difficulty": "Medium",
        "prerequisite": "Arrays",
        "explanation": "Array elements can be accessed directly using their index."
    },

    {
        "id": 3,
        "concept": "Arrays",
        "question": "Which operation is generally expensive in the middle of an array?",
        "options": [
            "Accessing an element",
            "Reading the first element",
            "Inserting an element",
            "Checking the array length"
        ],
        "answer": "Inserting an element",
        "difficulty": "Medium",
        "prerequisite": "Arrays",
        "explanation": "Elements may need to be shifted when inserting into the middle."
    },


    # ========================================================
    # LINKED LISTS
    # ========================================================

    {
        "id": 4,
        "concept": "Linked Lists",
        "question": "Which pointer usually points to the next node in a linked list?",
        "options": [
            "Head",
            "Next",
            "Root",
            "Parent"
        ],
        "answer": "Next",
        "difficulty": "Easy",
        "prerequisite": None,
        "explanation": "The next pointer stores the reference to the following node."
    },

    {
        "id": 5,
        "concept": "Linked Lists",
        "question": "What is the typical time complexity of inserting a node at the beginning of a linked list?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],
        "answer": "O(1)",
        "difficulty": "Medium",
        "prerequisite": "Linked Lists",
        "explanation": "Insertion at the beginning only requires updating the head pointer."
    },

    {
        "id": 6,
        "concept": "Linked Lists",
        "question": "Which structure does a linked-list node commonly contain?",
        "options": [
            "Only data",
            "Only a pointer",
            "Data and a pointer",
            "Only an index"
        ],
        "answer": "Data and a pointer",
        "difficulty": "Easy",
        "prerequisite": "Linked Lists",
        "explanation": "A basic linked-list node stores data and a reference to another node."
    },


    # ========================================================
    # STACK & QUEUE
    # ========================================================

    {
        "id": 7,
        "concept": "Stack & Queue",
        "question": "Which data structure follows the LIFO principle?",
        "options": [
            "Queue",
            "Stack",
            "Array",
            "Graph"
        ],
        "answer": "Stack",
        "difficulty": "Easy",
        "prerequisite": None,
        "explanation": "LIFO means Last In, First Out, which is the principle used by stacks."
    },

    {
        "id": 8,
        "concept": "Stack & Queue",
        "question": "Which data structure follows the FIFO principle?",
        "options": [
            "Stack",
            "Tree",
            "Queue",
            "Heap"
        ],
        "answer": "Queue",
        "difficulty": "Easy",
        "prerequisite": "Stack & Queue",
        "explanation": "FIFO means First In, First Out, which is the principle used by queues."
    },

    {
        "id": 9,
        "concept": "Stack & Queue",
        "question": "Which operation removes an element from the top of a stack?",
        "options": [
            "Push",
            "Pop",
            "Enqueue",
            "Insert"
        ],
        "answer": "Pop",
        "difficulty": "Medium",
        "prerequisite": "Stack & Queue",
        "explanation": "Pop removes the most recently added element from a stack."
    },


    # ========================================================
    # RECURSION
    # ========================================================

    {
        "id": 10,
        "concept": "Recursion",
        "question": "What must a recursive function eventually have?",
        "options": [
            "A loop",
            "A base case",
            "A database",
            "A queue"
        ],
        "answer": "A base case",
        "difficulty": "Easy",
        "prerequisite": None,
        "explanation": "A base case stops recursive calls from continuing indefinitely."
    },

    {
        "id": 11,
        "concept": "Recursion",
        "question": "What can happen if a recursive function has no reachable base case?",
        "options": [
            "It becomes faster",
            "It may cause infinite recursion",
            "It automatically becomes iterative",
            "It always returns zero"
        ],
        "answer": "It may cause infinite recursion",
        "difficulty": "Medium",
        "prerequisite": "Recursion",
        "explanation": "Without a reachable stopping condition, recursive calls can continue until the call stack is exhausted."
    },

    {
        "id": 12,
        "concept": "Recursion",
        "question": "Which memory structure keeps track of active recursive function calls?",
        "options": [
            "Queue",
            "Heap",
            "Call stack",
            "Hash table"
        ],
        "answer": "Call stack",
        "difficulty": "Medium",
        "prerequisite": "Recursion",
        "explanation": "Each recursive call creates a stack frame on the call stack."
    },


    # ========================================================
    # TREES
    # ========================================================

    {
        "id": 13,
        "concept": "Trees",
        "question": "What is the topmost node of a tree called?",
        "options": [
            "Leaf",
            "Child",
            "Root",
            "Edge"
        ],
        "answer": "Root",
        "difficulty": "Easy",
        "prerequisite": None,
        "explanation": "The root is the topmost node of a tree."
    },

    {
        "id": 14,
        "concept": "Trees",
        "question": "What is a node with no children called?",
        "options": [
            "Root",
            "Parent",
            "Leaf",
            "Edge"
        ],
        "answer": "Leaf",
        "difficulty": "Easy",
        "prerequisite": "Trees",
        "explanation": "A leaf node has no children."
    },

    {
        "id": 15,
        "concept": "Trees",
        "question": "Which traversal visits the left subtree, root, and then right subtree?",
        "options": [
            "Preorder",
            "Inorder",
            "Postorder",
            "Level order"
        ],
        "answer": "Inorder",
        "difficulty": "Medium",
        "prerequisite": "Trees",
        "explanation": "Inorder traversal follows Left → Root → Right."
    },


    # ========================================================
    # GRAPHS
    # ========================================================

    {
        "id": 16,
        "concept": "Graphs",
        "question": "Which data structure is commonly used to represent a graph?",
        "options": [
            "Adjacency list",
            "Single variable",
            "Stack only",
            "String only"
        ],
        "answer": "Adjacency list",
        "difficulty": "Easy",
        "prerequisite": "Trees",
        "explanation": "An adjacency list represents each vertex and its connected vertices."
    },

    {
        "id": 17,
        "concept": "Graphs",
        "question": "Which algorithm commonly uses a queue for graph traversal?",
        "options": [
            "DFS",
            "BFS",
            "Binary Search",
            "Merge Sort"
        ],
        "answer": "BFS",
        "difficulty": "Medium",
        "prerequisite": "Stack & Queue",
        "explanation": "Breadth-First Search uses a queue to explore nodes level by level."
    },

    {
        "id": 18,
        "concept": "Graphs",
        "question": "Which traversal commonly uses a stack or recursion?",
        "options": [
            "BFS",
            "DFS",
            "Linear Search",
            "Bubble Sort"
        ],
        "answer": "DFS",
        "difficulty": "Medium",
        "prerequisite": "Recursion",
        "explanation": "Depth-First Search can be implemented using recursion or an explicit stack."
    }

]