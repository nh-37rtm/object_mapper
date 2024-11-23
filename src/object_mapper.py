


import typing as t 


T= t.TypeVar('T')


class IObjectMapper(t.Generic[T]):
    
    __destination_class: t.Type
    
    def __init__(self, destination_class: t.Type):
        self.__destination_class = destination_class
        
    def do_map(self, source: dict, destination: t.Type[T], check_attributes = True) -> None:
        pass
    def do_map_to_new(self, source: dict) -> type[T]:
        return_value: T = self.__destination_class()
        self.do_map(source= source, destination= return_value)
        return return_value
    def do_map_to(self, source: dict) -> t.Type[T]:
        pass

class CallbackObjectMapper(IObjectMapper[T]):
    __field_mapper_callback: t.Callable[ [str], str] = None
    
    def __init__(self, callback: t.Callable[ [str], str], destination_class: t.Type):
        super().__init__(destination_class)
        self.__field_mapper_callback = callback
    
    def do_map(self, source: dict, destination: type[T]) -> None:
        super().do_map(source, destination)
        
        for source_field_name, source_field_value in source.items():
            transformed_destination_field_name = self.__field_mapper_callback(source_field_name)
            setattr(destination, transformed_destination_field_name, source_field_value)

class FieldToFieldMappingBasedObjectMapper(IObjectMapper[T]):
    
    __fields_definition_mapping: dict[str, str] = None
    
    def __init__(self, field_definition_mapping: dict, destination_class: t.Type) -> None:
        super().__init__(destination_class)
        self.__fields_definition_mapping = field_definition_mapping
    
    def do_map(self, source: dict, destination: type[T], check_attributes = True) -> None:
        super().do_map(source, destination)
        
        for source_field_name, destination_field_name in self.__fields_definition_mapping.items():
            
            if check_attributes is True:
                if not source_field_name in source:
                    raise AttributeError(f"source as no attribute {source_field_name}")
                if not hasattr(destination, destination_field_name):
                    raise AttributeError(f"destination as no attribute {destination_field_name}")
            
            setattr(destination, destination_field_name, source[source_field_name])
        
