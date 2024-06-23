# Implementing Python Data Structures 🧱

<img src="https://github.com/pgnikolov/implementing-python-data-structures/assets/151896883/e21970fa-c162-4dea-aef6-f5d46585b818" width="720" height="420"/>

This project demonstrates the implementation of various Python data structures including lists, dictionaries, sets, tuples, stacks, and queues. Each data structure is implemented in its own class with methods to perform common operations. This repository provides a collection of Python functions for commonly used data structures, including:

## Project Structure

The project consists of the following files:

* `lists.py`
* `dictionary.py`
* `setss.py`
* `tuples.py`
* `stack.py`
* `queue.py`
* `main.py`

## Class Implementations

1. **Lists**
    
    * File: `lists.py`
      
    * Methods: `handle_append`, `handle_extend`, `handle_insert`, `handle_remove`, `handle_pop`, `handle_clear`, `handle_index`, `handle_count`, `handle_sort`, `handle_reverse`, `handle_copy`

2. **Dictionary**
    
    * File: `dictionary.py`
  
    * Methods: `handle_pop`, `handle_items`, `handle_get`, `handle_copy`, `handle_clear`, `handle_keys`, `handle_values`, `handle_update`, `handle_popitem`, `handle_setdefault`

3. **Sets**
    
    * File: `setss.py`
    
    * Methods: `handle_add`, `handle_remove`, `handle_discard`, `handle_pop`, `handle_clear`, `handle_union`, `handle_intersection`, `handle_difference`, `handle_copy`, `handle_issuperset`, `handle_issubset`, `handle_symmetric_difference`
  
4. **Tuples**

    * File: `tuples.py`
    
    * Methods: `handle_count`, `handle_index`

5. **Stack**

    * File: `stack.py`
    
    * Methods:  `push`, `pop`, `peek`, `size`
  
6. **Queue**

    * File: `queue.py`
    
    * Methods: `handle_enqueue`, `handle_dequeue`, `handle_peek`, `handle_size`, `handle_rotate`
  
   
  
### Main Script

The `main.py` script provides a command-line interface to interact with each of the data structures. Users can choose a data structure and perform various operations through a menu-driven interface.


## How to Run 🏃‍♂️

1. Clone the repository 🥡
   
```bash
git clone https://github.com/yourusername/implementing-python-data-structures.git
cd implementing-python-data-structures
```

2. Run the main script:

```bash
python main.py
```

3. Follow the on-screen instructions to interact with the data structures.

## Example Usage

Here are some examples of how to use the implemented data structures through the command-line interface:

### List Operations 🎟️

1. Append an element to a list:

```bash
Choose Data Structure:
1. List
Enter your choice (1-4): 1

Enter initial list values (comma-separated): 1, 2, 3
Choose a list operation:
1. Append
Enter your choice (1-12): 1
Enter element to be appended: 4
[1, 2, 3, 4]
```

### Dictionary Operations 📖

1. Pop an element from dictionary: 

```bash
Choose Data Structure:
2. Dictionary
Enter key: value pair like this ("key1: value1, key2: value2"): a: 1, b: 2
Choose option:
1. Pop
Enter a choice: 1
Enter a key which you want to pop: a
1
```

### Stack Operations 📚

1. Push an element onto a stack:

```bash
Choose Data Structure:
5. Stack
Enter initial list values (comma-separated): 1, 2, 3
Choose option:
1. Push
Enter a choice: 1
Enter element to push: 4
[4, 1, 2, 3]
```

## Contributing 🤝
Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License 📝
This project is licensed under the MIT License.

## Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)

