# Create a new RestRewardTooltipViewModel
view_model = RestRewardTooltipViewModel()

# Add some rewards to the view model
rewards = [
    ItemBonusModel(item_id=1, value=10),
    ItemBonusModel(item_id=2, value=5),
    ItemBonusModel(item_id=3, value=20),
]
view_model.setRewards(rewards)

# Display the tooltip with the view model as its data source
tooltip = Tooltip(view_model=view_model)
tooltip.show()
