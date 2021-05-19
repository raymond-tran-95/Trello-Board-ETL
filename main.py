import pandas as pd
import json

# Returns the list of cards from the board JSON
def get_cards(board):
	return board["cards"]

# Iterate through the list of cards and get card details
def card_details(cards):
	card_details = []
	for card in cards:
		card_details.append(flatten_card(card))
	return card_details

# Flatten the card from JSON board
def flatten_card(card):
	return {
		"id": card["id"],
		"CardName": card["name"],
		"Description": card["desc"],
		"idList": card["idList"]
	}

# Returns the list names and ids
def get_lists(board):
	return board["lists"]

# Iterate through the list of lists and get list details
def list_details(lists):
	list_details = []
	for list_item in lists:
		list_details.append(flatten_list(list_item))
	return list_details

# Flatten the list details from JSON board
def flatten_list(list_item):
	return {
		"idList": list_item["id"],
		"ListName": list_item["name"],
		"Closed": list_item["closed"],
		"Position": list_item["pos"]
	}

with open("Trello_Board.json", "r") as f:
	trello_board = json.load(f)

flattened_list = list_details(get_lists(trello_board))
flattened_cards = card_details(get_cards(trello_board))

# Stores the lists ids and names into a data frame
data_lists = pd.DataFrame(flattened_list)
data_lists.to_csv('Flattened_list.csv')

# Stores the card ids, name and description into a data frame
data_cards = pd.DataFrame(flattened_cards)
data_cards.to_csv('data_cards.csv')

# Joins the card and list dataframes against their corresponding listIDs
data_card_list = pd.merge(data_cards, data_lists, on='idList', how='inner')
data_card_list.to_csv('data_cards_list.csv')