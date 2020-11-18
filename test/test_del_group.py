def test_del_group(app):
    old_groups_list = app.group.get_groups_list()
    group = "TestGroup"
    if group not in old_groups_list:
        app.group.add_new_group(group)
    app.group.del_group(group)
    new_groups_list = app.group.get_groups_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_groups_list.remove("TestGroup")
    # Check match of UI and DB lists
    assert sorted(old_groups_list) == sorted(new_groups_list)