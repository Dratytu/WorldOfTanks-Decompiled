from typing import List  # Importing the List type from the typing module

# Create a list of ItemBonusModel objects, each with an item_id and a value attribute
rewards = [
    ItemBonusModel(item_id=1, value=10),
    ItemBonusModel(item_id=2, value=5),
    ItemBonusModel(item_id=3, value=20),
]

# Create a new RestRewardTooltipViewModel object and initialize it with the rewards list as its data
view_model = RestRewardTooltipViewModel(rewards=rewards)

# Create a new Tooltip object and initialize it with the RestRewardTooltipViewModel object as its data source
tooltip = Tooltip(view_model=view_model)

# Display the Tooltip on the screen
tooltip.show()
