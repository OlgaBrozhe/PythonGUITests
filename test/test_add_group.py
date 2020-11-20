def test_add_group(app, excel_data_groups):
    old_groups_list = app.group.get_groups_list()
    group = excel_data_groups
    app.group.add_new_group(group)
    new_groups_list = app.group.get_groups_list()
    # Append old list with new item, clear and sort lists ascending and check if they are still equal
    old_groups_list.append(group)
    # Check match of UI and DB lists
    assert sorted(old_groups_list) == sorted(new_groups_list)
