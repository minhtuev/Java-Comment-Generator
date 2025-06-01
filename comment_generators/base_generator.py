from abc import ABC, abstractmethod

class BaseCommentGenerator(ABC):
    @abstractmethod
    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        pass

    @abstractmethod
    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        pass
