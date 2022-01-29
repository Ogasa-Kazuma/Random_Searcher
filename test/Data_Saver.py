
import Data_Saver
import importlib
import Pickle_Reader

importlib.reload(Data_Saver)


saver = Data_Saver.DataSaver()
indexs = ["x", "y"]
values = [[3, 9], [3.0 ,3 ,3]]
path = "SearchingDataLog/SaveTestLog.pkl"

saver.Save(indexs, values, path)
pklReader = Pickle_Reader.PickleReader()
pklReader.Read("SearchingDataLog/0.pkl")
