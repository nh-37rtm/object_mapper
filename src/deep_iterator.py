

import typing as t
from dataclasses import dataclass
from queue import SimpleQueue


@dataclass
class SafeDeepIteratorNode:
    
    reference: dict|list
    depth: int
    parents: dict['SafeDeepIteratorNode']
    childs: dict['SafeDeepIteratorNode']
    relative_id: str
    
    def __init__(self, reference: dict|list):
        super.__init__(self)
        self.parents = dict()
        self.childs = dict()
        self.reference = reference
        depth = None
        

class SafeDeepIterator(t.Iterator):
       
    _iterating_queue: SimpleQueue[] = None
    
    
    def __init__(self, base_node_element_reference: dict|list) -> None:        
        self._iterating_queue = SimpleQueue[]
        self._iterating_queue.put(base_node_element_reference)

    def __next__(self) -> Any:
        super().__next__()
        while not self._iterating_queue.empty() :
            current_element = self._iterating_queue.get()
            match current_element:
                case dict():
                    current_element: dict
                    for id, value in current_element.items():
                        wrapped_child = SafeDeepIteratorNode(reference=value)
                        wrapped_child.relative_id = id
                        self._iterating_queue.put(value)
                case list():
                    current_element: list
                    for element in current_element:
                        wrapped_child = None
                    

