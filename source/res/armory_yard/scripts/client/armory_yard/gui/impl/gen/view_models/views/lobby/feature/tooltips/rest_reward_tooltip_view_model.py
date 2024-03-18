from typing import List

# Create a new RestRewardTooltipViewModel and initialize it with some rewards
rewards = [
    ItemBonusModel(item_id=1, value=10),
    ItemBonusModel(item_id=2, value=5),
    ItemBonusModel(item_id=3, value=20),
]
view_model = RestRewardTooltipViewModel(rewards=rewards)

# Display the tooltip with the view model as its data source
tooltip = Tooltip(view_model=view_model)
tooltip.show()
