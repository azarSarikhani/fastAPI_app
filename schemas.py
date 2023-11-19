from pydantic import BaseModel
import json

#{"id" : 1, "size" : "s", "color" : "green", "group" : "kids"},
class ShirtInput(BaseModel):
	size: str | None = "free size"
	color: str
	group: str | None = "kids"

	class Config:
		schema_extra = {
			"example":{
				"size": "free size",
				"color": "white",
				"group": "unisex"
			}
		}

class ShirtOutput(ShirtInput):
	id :int 

def load_db() -> list[ShirtOutput]:
	"""Load a list of Shirt objects from a JSON file"""
	with open("shirts.json") as f:
		#return [Shirt.parse_obj(obj) for obj in json.load(f)]
		data = json.load(f)
	shirt_list = []
	for obj in data:
		shirt_list.append(ShirtOutput.model_validate(obj))
	return shirt_list

def save_db(shirts: list[ShirtOutput]):
	with open("shirts.json", "w") as f:
		json.dump([shirt.dict() for shirt in shirts], f, indent=4)
	
def save_new(shirt: ShirtOutput):
	with open("new_shirts.json", "w") as f:
		json.dump(shirt.dict(), f, indent=4)


if __name__ == "__main__":
	result = load_db()
	print(len(result))
	print(type(result))
	#for item in result :
	#	print(type(item))


	# result_type = [type(item) for item in result if type(item) == int]
	# print(result_type)
