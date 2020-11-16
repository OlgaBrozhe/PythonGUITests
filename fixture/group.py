from model.group_form import GroupForm


class GroupHelper:

    def __init__(self, app):
        self.app = app

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
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        pass

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group)
        input.type_keys("\n")
        self.close_group_editor()
