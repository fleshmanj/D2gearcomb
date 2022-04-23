import logging

class Setbonus:

    def __init__(self,data):
        if key in item_py.sets.keys():
            logging.debug(f"value is {value}")
            logging.debug(f"add func is {item['add func']}")
            property_num = 0
            for keys in item.keys():
                if str(keys).startswith("aprop"):
                    property_num += 1
                    globals()[f"var{property_num}"] = keys.strip(f'aprop{property_num}_')
                    exec(f"var{property_num} = keys.strip(f'aprop{property_num}_')")
                    logging.debug(globals()[f"var{property_num}"])
                # TODO need to add additional stats from set bonus and set item bonus
                if self.stats[f"{key}"] == item["add func"]:
                    logging.debug(f"set bonus enabled tier 1")
                    self.stats[globals()[f"var1"]] = self.stats[globals()[f"var1"]] + item[
                        f"aprop{1}_{globals()[f'var1']}"]
                    print(self.stats[globals()[f"var1"]])
        pass
