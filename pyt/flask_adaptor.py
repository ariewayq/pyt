"""Contains a class that can be used as adaptor."""
from framework_adaptor import Adaptor


class FlaskAdaptor(Adaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def is_flask_route_function(self, function):
        """Check whether function uses a decorator."""
        return any(decorator for decorator in function.decorator_list if decorator.func.value.id == 'app' and decorator.func.attr == 'route')

    def find_flask_route_functions(self, functions):
        """Find all flask functions with decorators."""
        for func in functions.items():
            if self.is_flask_route_function(func[1]):
                yield func[1]

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        self.cfg_list.extend(self.find_flask_route_functions(self.cfg_list[0].functions))