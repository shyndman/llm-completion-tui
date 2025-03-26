# import importlib
# import os
# import sys
# from collections import defaultdict


# def get_package_contents(package_name):
#     """Recursively get all modules in a package."""
#     try:
#         package = importlib.import_module(package_name)
#         package_path = getattr(package, "__path__", None)

#         if package_path:
#             modules = set()
#             for path in package_path:
#                 if os.path.exists(path):
#                     for root, dirs, files in os.walk(path):
#                         rel_path = os.path.relpath(root, path)
#                         rel_path = "" if rel_path == "." else rel_path

#                         for file in files:
#                             if file.endswith(".py") and not file.startswith("_"):
#                                 module_path = os.path.join(rel_path, file[:-3])
#                                 module_path = module_path.replace(os.sep, ".")
#                                 full_name = (
#                                     f"{package_name}.{module_path}"
#                                     if module_path
#                                     else package_name
#                                 )
#                                 modules.add(full_name)

#                         for dir_name in dirs:
#                             if not dir_name.startswith("_"):
#                                 init_file = os.path.join(root, dir_name, "__init__.py")
#                                 if os.path.exists(init_file):
#                                     module_path = os.path.join(rel_path, dir_name)
#                                     module_path = module_path.replace(os.sep, ".")
#                                     full_name = (
#                                         f"{package_name}.{module_path}"
#                                         if module_path
#                                         else package_name
#                                     )
#                                     modules.add(full_name)
#                                     try:
#                                         modules.update(get_package_contents(full_name))
#                                     except:
#                                         pass
#             return modules
#         return set()
#     except:
#         return set()


# def build_complete_module_tree():
#     tree = defaultdict(list)
#     # Get base packages but allow underscore modules when they're submodules
#     base_packages = {
#         name.split(".")[0]
#         for name in sys.modules.keys()
#         if name and (not name.startswith("_") or "." in name)
#     }

#     for package_name in sorted(base_packages):
#         if package_name not in tree[""]:
#             tree[""].append(package_name)
#             try:
#                 modules = {
#                     name: mod
#                     for name, mod in sys.modules.items()
#                     if name.startswith(package_name + ".")
#                 }

#                 for module_name in sorted(modules):
#                     parts = module_name.split(".")
#                     for i in range(len(parts)):
#                         parent = ".".join(parts[:i]) if i > 0 else ""
#                         child = ".".join(parts[: i + 1])
#                         if child not in tree[parent]:
#                             tree[parent].append(child)
#             except:
#                 pass

#     return tree


# def print_module_tree(tree, parent="", level=0, loaded_only=False, file=sys.stdout):
#     if level == 0:
#         for module in sorted(tree[""]):
#             is_loaded = module in sys.modules
#             loaded_indicator = "*" if is_loaded else " "
#             if not loaded_only or is_loaded:
#                 print(f"├── {module} {loaded_indicator}", file=file)
#                 print_module_tree(tree, module, level + 1, loaded_only, file=file)
#     else:
#         prefix = "│   " * (level - 1) + "├── "
#         for module in sorted(tree[parent]):
#             if module != parent:
#                 module_part = module.split(".")[-1]
#                 is_loaded = module in sys.modules
#                 loaded_indicator = "*" if is_loaded else " "
#                 if not loaded_only or is_loaded:
#                     print(f"{prefix}{module_part} {loaded_indicator}", file=file)
#                     print_module_tree(tree, module, level + 1, loaded_only, file=file)


# def print_package_hierarchy(loaded_only=False, file=sys.stdout):
#     print("Module Hierarchy:", file=file)
#     print("================", file=file)
#     print("* indicates module is currently loaded\n", file=file)
#     tree = build_complete_module_tree()
#     print_module_tree(tree, loaded_only=loaded_only, file=file)


# with open("./kitten.log", "w") as f:
#     print_package_hierarchy(loaded_only=False, file=f)


# # from kittens.tui.handler import kitten_ui


# # @kitten_ui(allow_remote_control=True)
# def main(args: list[str]) -> None:
#     pass


# #     # get the result of running kitten @ ls
# #     cp = main.remote_control(["ls"], capture_output=True)
# #     if cp.returncode != 0:
# #         sys.stderr.buffer.write(cp.stderr)
# #         raise SystemExit(cp.returncode)
# #     output = json.loads(cp.stdout)
# #     pprint(output)
# #     # open a new tab with a title specified by the user
# #     title = input("Enter the name of tab: ")
# #     window_id = main.remote_control(
# #         ["launch", "--type=tab", "--tab-title", title], check=True, capture_output=True
# #     ).stdout.decode()
# #     return window_id
