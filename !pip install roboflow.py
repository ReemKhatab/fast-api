from roboflow import Roboflow
rf = Roboflow(api_key="TnS1xT7Tgm1gOrarQl7F")
project = rf.workspace("cairo-university-tito4").project("hats-detection-3nx7h")
dataset = project.version(1).download("yolov5")
