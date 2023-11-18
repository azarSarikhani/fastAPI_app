from pydantic import BaseModel
import json

#{"id" : 1, "size" : "s", "color" : "green", "group" : "kids"},
class Shirt(BaseModel):
	id: int
	size: str | None = "free size"
	color: str
	group: str | None = "kids"

def load_db() -> list[Shirt]:
	"""Load a list of Car objects from a JSON file"""
	with open("shirts.json") as f:
		#return [Shirt.parse_obj(obj) for obj in json.load(f)]
		data = json.load(f)
	shirt_list = []
	for obj in data:
		shirt_list.append(Shirt.model_validate(obj))
	return shirt_list

if __name__ == "__main__":
	result = load_db()
	print(len(result))
	print(type(result))
	#for item in result :
	#	print(type(item))


	# result_type = [type(item) for item in result if type(item) == int]
	# print(result_type)
