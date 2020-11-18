class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.group_editor = self.app.application.window(title="Group editor")
        self.delete_group_editor = self.app.application.window(title="Delete group")

    def get_groups_list(self):
        self.open_group_editor()
        # Get groups from window 'Group editor'
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        groups_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return groups_list

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input_group_name = self.group_editor.window(class_name="Edit")
        input_group_name.set_text(group)
        input_group_name.type_keys("\n")
        self.close_group_editor()

    def del_group(self, group):
        self.open_group_editor()
        # Select a group in the tree
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root().text()
        tree.get_item(("\{}\{}").format(root, group)).click_input()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group_editor.wait("visible")
        self.delete_group_editor.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()
