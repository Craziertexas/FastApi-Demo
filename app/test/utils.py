class TestUtils():

    def GetResponseTypes(json:dict):
            json = json.copy()
            for Key in json.keys():
                if (type(json[Key]) == dict):
                    json[Key] = TestUtils.GetResponseTypes(json[Key])
                else:
                    json[Key] = type(json[Key])
            return json