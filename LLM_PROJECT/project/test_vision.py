from vision.inference import predict_image

monument, confidence = predict_image("gettyimages-79730659-612x612.jpeg")

print("Predicted:", monument)
print("Confidence:", confidence)
