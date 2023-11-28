from pathlib import Path 

class ComponentWalker:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.component_dir = None

    def find_component_directory(self, component_dir="components"):
        """Find, set and return the `components` directory inside the root directory."""
        if self.component_dir is not None:
            return self.component_dir
        
        for directory in self.root_dir.rglob(component_dir):
            if directory.is_dir():
                self.component_dir = directory
                return directory
            
        raise FileNotFoundError(f"The '{component_dir}' directory is not found inside the project.")
            

    def print_comp_tree(self, directory=None, prefix="", filetype="js"):
        if self.component_dir is not None:
            if directory is None:
                directory = self.component_dir
            print(f"{prefix}{directory.name}/")
            prefix += "    "  # Increase indentation for child items
            for item in sorted(directory.iterdir()):
                if item.is_dir():
                    self.print_comp_tree(item, prefix)
                elif filetype == "js" and (item.name.endswith(".js") or (item.name.endswith(".jsx"))):
                    print(f"{prefix}--{item.name}")
                elif filetype == "ts" and (item.name.endswith(".ts") or (item.name.endswith(".tsx"))):
                    print(f"{prefix}--{item.name}")