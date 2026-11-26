class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

    def __del__(self):
        pass

    def get_name(self):
        return self.name

    def get_extension(self):
        return self.extension

    def get_size(self):
        return self.size

    def set_name(self, name):
        self.name = name

    def set_extension(self, extension):
        self.extension = extension

    def set_size(self, size):
        self.size = size

    def show(self):
        print(self.name + "." + self.extension, self.size)

class Folder:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __del__(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add(self, item):
        self.items.append(item)

    def show_tree(self):
        print(self.name)

        for item in self.items:
            if isinstance(item, Folder):
                item.show_tree()
            else:
                item.show()

    def find_longest_path(self, path=""):
        current_path = path + "/" + self.name
        longest_path = current_path

        for item in self.items:
            if isinstance(item, Folder):
                result = item.find_longest_path(current_path)
            else:
                result = (
                    current_path + "/" + item.get_name()
                    + "." + item.get_extension()
                )

            if len(result) > len(longest_path):
                longest_path = result

        return longest_path


def main():
    root = Folder("Root")

    root.add(File("File1", "txt", 10))
    root.add(File("File2", "pdf", 20))
    root.add(File("File3", "png", 30))

    root.show_tree()
    print(root.find_longest_path())


if __name__ == "__main__":
    main()
