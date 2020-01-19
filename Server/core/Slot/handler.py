try:
	from .slot import Slot
except ModuleNotFoundError:
	from slot import Slot
	
class SlotHandler:
	def __init__(self):
		# Liste des slots utilisées
		self.slots_list = {}

	def new_slot(self,data):
		""" Créé un nouveau slot"""
		slot_id = data["slot"] = str(len(self.slots_list) + 1)

		self.slots_list[data['ip']] = Slot(**data)

		return slot_id


if __name__ == "__main__":
	handler = SlotHandler()

	handler.new_slot({
		"name":1,
		"type":2,
		"ip":3,
		"protocol":4
	})

	print(str(handler.slots_list["1"]))

