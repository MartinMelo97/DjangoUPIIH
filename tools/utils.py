from datetime import datetime

def tools_form_validations(form, tool, actual_tool = None):

    # Validate if the form says that the tool has been in maintaince
    # If not, we set the mainteance_date to null (None in Python)
    if not form.cleaned_data['has_been_in_mainteance']:
        tool.mainteance_date = None

    # Validate if the forms says that the tool has tracked
    # If not, we set the tracked if to null (None in Python)
    if not form.cleaned_data['has_tracker']:
        tool.tracker_id = None

    # If the tool is in mainteance, but in the update this boolean value
    # Is changed from true to false, this means that the tools has been mainteanced
    # We need to change the mainteance_date to now
    # Only in the update cases (when actual_tool is not none)

    print('actual_tool', actual_tool)
    if actual_tool is not None:
        if actual_tool \
        and not form.cleaned_data['is_in_maintain']:
            tool.has_been_in_mainteance = True
            tool.mainteance_date = datetime.now()

    return tool