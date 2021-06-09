import os
import pickle
from build_tree import add_file_to_tree
from node import *
from source import *


def create_tree():
    s = Source("", 0, 0)
    root = Node("1", None, s)
    return root


def export_desc_files(rootdir):
    root = create_tree()
    with open('data_tree.pkl', 'wb') as pkl_file:
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                # print (os.path.join(subdir, file))
                filepath = subdir + os.sep + file

                if filepath.endswith(".txt"):
                    print (filepath)
                    add_file_to_tree(root, filepath)
        print("export:")
        pickle.dump(root, pkl_file, protocol=pickle.HIGHEST_PROTOCOL)


def import_tree():
    with open('data_tree.pkl', 'rb') as handle:
        tree = pickle.load(handle)
        return tree


if __name__=='__main__':
    # export('text.txt')

    # tree = import_tree()
    # utils.print_dict(tree)

    export_desc_files("Archive")
